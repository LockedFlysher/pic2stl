import cv2
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("img.png")

# 调整图像大小，使长边为300像素
height, width = img.shape[:2]
if width > height:
    new_width = 300
    new_height = int(height * (300 / width))
else:
    new_height = 300
    new_width = int(width * (300 / height))

img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

# 转换为灰度图
img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

# 应用阈值处理得到二值图
_, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 创建高度图（将黑色部分凸起）
height_map = np.zeros((binary.shape[0], binary.shape[1]), dtype=float)
height_map[binary == 0] = 1  # 将黑色部分设置为高度1

# 创建3D网格
x, y = np.meshgrid(range(binary.shape[1]), range(binary.shape[0]))


# 合并相邻的相同高度的点
def merge_adjacent(height_map):
    merged = np.zeros_like(height_map, dtype=bool)
    vertices = []
    faces = []

    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            if not merged[i, j]:
                h = height_map[i, j]
                x_start, y_start = j, i
                x_end, y_end = j, i

                # 向右扩展
                while x_end + 1 < height_map.shape[1] and height_map[i, x_end + 1] == h and not merged[i, x_end + 1]:
                    x_end += 1

                # 向下扩展
                can_expand_down = True
                while can_expand_down and y_end + 1 < height_map.shape[0]:
                    for x in range(x_start, x_end + 1):
                        if height_map[y_end + 1, x] != h or merged[y_end + 1, x]:
                            can_expand_down = False
                            break
                    if can_expand_down:
                        y_end += 1

                # 标记为已合并
                merged[y_start:y_end + 1, x_start:x_end + 1] = True

                # 添加顶点和面
                v0 = len(vertices)
                vertices.extend([
                    [x_start, y_start, h],
                    [x_end + 1, y_start, h],
                    [x_start, y_end + 1, h],
                    [x_end + 1, y_end + 1, h]
                ])
                faces.extend([
                    [v0, v0 + 2, v0 + 1],
                    [v0 + 1, v0 + 2, v0 + 3]
                ])

    return np.array(vertices), np.array(faces)


vertices_top, faces_top = merge_adjacent(height_map)

# 添加底部顶点和面
vertices_bottom = vertices_top.copy()
vertices_bottom[:, 2] = 0  # 设置z坐标为0
vertices = np.vstack((vertices_top, vertices_bottom))

faces_bottom = faces_top.copy()
faces_bottom += len(vertices_top)  # 调整索引
faces_bottom = faces_bottom[:, [0, 2, 1]]  # 翻转法线方向

# 添加侧面
side_faces = []
for i in range(len(faces_top)):
    for j in range(3):
        v0 = faces_top[i][j]
        v1 = faces_top[i][(j + 1) % 3]
        v2 = v0 + len(vertices_top)
        v3 = v1 + len(vertices_top)
        side_faces.extend([[v0, v1, v2], [v1, v3, v2]])

# 合并所有面
faces = np.vstack((faces_top, faces_bottom, side_faces))

# 创建mesh对象
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j], :]


# 验证模型是否封闭
def is_closed_mesh(mesh_obj):
    edges = {}
    for face in mesh_obj.vectors:
        for i in range(3):
            edge = tuple(sorted([tuple(face[i]), tuple(face[(i + 1) % 3])]))
            if edge in edges:
                edges[edge] += 1
            else:
                edges[edge] = 1
    return all(count == 2 for count in edges.values())


is_closed = is_closed_mesh(cube)
print(f"模型是否封闭: {'是' if is_closed else '否'}")

# 保存STL文件
cube.save('model.stl')

# 显示原始图像、调整大小后的图像和二值图
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(132)
plt.imshow(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')
plt.subplot(133)
plt.imshow(binary, cmap='gray')
plt.title('Binary Image')
plt.show()

print(f"原始图像大小: {img.shape}")
print(f"调整后图像大小: {img_resized.shape}")
print("STL文件已保存为 'model.stl'")
