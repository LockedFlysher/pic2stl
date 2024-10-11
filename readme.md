# Pic2STL: 2D图像到3D STL模型转换器 / 2D Image to 3D STL Model Converter

这个项目包含一个Python脚本，可以将2D图像转换为3D STL模型。它演示了如何处理图像、创建高度图，并生成可用于3D打印的STL文件。

This project contains a Python script that converts 2D images to 3D STL models. It demonstrates how to process images, create height maps, and generate STL files suitable for 3D printing.

## 功能 / Features

- 读取2D图像 / Read 2D images
- 调整图像大小以保持比例（长边300像素）/ Resize image while maintaining aspect ratio (longest side 300 pixels)
- 将图像转换为灰度图和二值图 / Convert image to grayscale and binary
- 基于二值图创建高度图 / Create height map based on binary image
- 生成3D网格 / Generate 3D mesh
- 保存为STL文件格式 / Save as STL file format
- 可视化原始图像、调整后的图像和二值图 / Visualize original image, resized image, and binary image

## 依赖 / Dependencies

本项目依赖以下Python库：
This project depends on the following Python libraries:

- OpenCV (cv2)
- NumPy
- Matplotlib
- numpy-stl

## 安装 / Installation

1. 克隆此仓库：/ Clone this repository:
   ```
   git clone https://github.com/LockedFlysher/pic2stl.git
   cd pic2stl
   ```

2. 运行安装脚本：/ Run the installation script:
   ```
   bash install_dependencies.sh
   ```

## 使用方法 / Usage

1. 确保已安装所有依赖。/ Ensure all dependencies are installed.
2. 将您想要转换的图像命名为 `img.png` 并放在脚本同一目录下。/ Name your image to be converted as `img.png` and place it in the same directory as the script.
3. 运行 `pic2stl.py` 脚本：/ Run the `pic2stl.py` script:
   ```
   python pic2stl.py
   ```
4. 脚本将处理图像，并生成一个名为 `model.stl` 的STL文件。/ The script will process the image and generate an STL file named `model.stl`.
5. 同时，它会显示原始图像、调整大小后的图像和二值图的可视化。/ It will also display visualizations of the original image, resized image, and binary image.

## 注意事项 / Notes

- 确保您的系统上安装了Python 3.x。/ Ensure you have Python 3.x installed on your system.
- 对于大型或复杂的图像，处理时间可能会较长。/ Processing time may be longer for large or complex images.
- 生成的STL文件可以用于3D打印或进一步的3D建模。/ The generated STL file can be used for 3D printing or further 3D modeling.
- 默认情况下，黑色区域将被拉伸为3D模型的突起部分。/ By default, black areas will be extruded as raised parts of the 3D model.

## 贡献 / Contributing

欢迎提出改进建议或直接贡献代码。请随时创建issue或提交pull request。

Suggestions for improvements or direct code contributions are welcome. Feel free to create issues or submit pull requests.

## 许可 / License

本项目采用开源许可。关注B站 "晴糖豆" 即可任意修改分发，但请勿用于商业盈利目的。

This project is open source. Follow "晴糖豆" on Bilibili for permission to modify and distribute, but please do not use for commercial profit purposes.

## 联系方式 / Contact

如有任何问题或建议，请在GitHub上创建issue或直接联系项目维护者。

If you have any questions or suggestions, please create an issue on GitHub or contact the project maintainer directly.

---

祝您使用愉快！/ Happy using!