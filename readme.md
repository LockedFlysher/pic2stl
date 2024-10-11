# Pic2STL: 2D图像到3D STL模型转换器

这个项目包含一个Python脚本，可以将2D图像转换为3D STL模型。它演示了如何处理图像、创建高度图，并生成可用于3D打印的STL文件。

## 功能

- 读取2D图像
- 调整图像大小以保持比例（长边300像素）
- 将图像转换为灰度图和二值图
- 基于二值图创建高度图
- 生成3D网格
- 保存为STL文件格式
- 可视化原始图像、调整后的图像和二值图

## 依赖

本项目依赖以下Python库：

- OpenCV (cv2)
- NumPy
- Matplotlib
- numpy-stl

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/LockedFlysher/pic2stl.git
   cd pic2stl
   ```

2. 运行安装脚本：
   ```
   bash install_dependencies.sh
   ```

## 使用方法

1. 确保已安装所有依赖。
2. 将您想要转换的图像命名为 `img.png` 并放在脚本同一目录下。
3. 运行 `pic2stl.py` 脚本：
   ```
   python pic2stl.py
   ```
4. 脚本将处理图像，并生成一个名为 `model.stl` 的STL文件。
5. 同时，它会显示原始图像、调整大小后的图像和二值图的可视化。

## 注意事项

- 确保您的系统上安装了Python 3.x。
- 对于大型或复杂的图像，处理时间可能会较长。
- 生成的STL文件可以用于3D打印或进一步的3D建模。
- 默认情况下，黑色区域将被拉伸为3D模型的突起部分。

## 贡献

欢迎提出改进建议或直接贡献代码。请随时创建issue或提交pull request。

## 许可

本项目采用开源许可。关注B站 "晴糖豆" 即可任意修改分发，但请勿用于商业盈利目的。

## 联系方式

如有任何问题或建议，请在GitHub上创建issue或直接联系项目维护者。

---

祝您使用愉快！