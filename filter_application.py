# 导包
import os

import cv2
import numpy as np

# 确保保存路径的文件夹存在
os.makedirs("./images/output_05", exist_ok=True)

# 读取 cloud.jpg
img = cv2.imread("./images/cloud.jpg")

"""
均值滤波
均值滤波器是一种线性滤波器，通过对图像局部邻域内的像素值取平均值来实现滤波。
工作原理：使用一个滑动窗口（核），在每个像素位置，计算窗口内所有像素值的平均值，并用该值替换中心像素值。
效果：均值滤波器可以有效地去除图像中的噪声，但是会使图像变得模糊。
适用场景：去除均匀分布的噪声，但会引起图像模糊。
均值滤波是一种线性滤波，它的模板是一个矩形，模板的大小由 ksize 参数决定，该参数是一个元组。
cv2.blur() 函数可以实现均值滤波, 其中 src 是输入图像，ksize 是模板的大小，ksize 为 (n, m) 时，表示模板的宽度为 n，高度为 m。
"""
# 均值滤波 (9*9) 表示滤波核的大小为 9*9
blur_img = cv2.blur(img, (9, 9))
# 保存均值滤波后的图像
cv2.imencode('.jpg', blur_img)[1].tofile("./images/output_05/均值滤波.jpg")

"""
中值滤波
中值滤波器是一种非线性滤波器，通过取局部邻域内像素值的中值来替代中心像素值。
工作原理：在滑动窗口内，将所有像素值排序，取中间值作为新的像素值。
效果：对椒盐噪声（salt-and-pepper noise）特别有效，能够在去噪的同时较好地保留图像边缘细节。
适用场景： 去除图像中的随机噪声（尤其是椒盐噪声）。
中值滤波是一种非线性滤波，它的模板是一个矩形，模板的大小由 ksize 参数决定，该参数是一个整数。
cv2.medianBlur() 函数可以实现中值滤波, 其中 src 是输入图像，ksize 是模板的大小，ksize 为 n 时，表示模板的大小为 n*n。
"""
# 中值滤波，继续对 cloud.jpg 做中值滤波，滤波核大小为 9×9
median_img = cv2.medianBlur(img, 9)
# 保存中值滤波后的图像
cv2.imencode('.jpg', median_img)[1].tofile("./images/output_05/中值滤波.jpg")

"""
高斯滤波
高斯滤波器是一种线性滤波器，使用高斯分布的权值对邻域像素值加权平均，权值随距离减小。
工作原理：使用一个高斯核（Gaussian kernel）进行加权平均，权值由高斯函数计算，高斯核的大小和标准差决定了滤波的平滑程度。
效果：在去噪的同时比均值滤波保留更多边缘细节，提供平滑效果，不会像均值滤波器那样完全模糊边缘。
适用场景： 通常用来去除图像的高频噪声，同时适合于计算机视觉任务中的预处理。
使用高斯滤波时，涉及了两个其他参数：sigmaX 和 sigmaY。修改 sigmaX 和 sigmaY 都会改变卷积核中的权重值。
具体则涉及卷积方面的知识，较为复杂，这里我们对其应用方式有所了解即可
"""
# 高斯滤波，继续对 cloud.jpg 做高斯滤波，滤波核大小为 9×9
gaussian_img = cv2.GaussianBlur(img, (9, 9), 0, 0)
# 保存高斯滤波后的图像
cv2.imencode('.jpg', gaussian_img)[1].tofile("./images/output_05/高斯滤波.jpg")

"""
双边滤波器
双边滤波器是一种高级滤波器，用于同时去除噪声和保留图像边缘。与普通的线性滤波器不同，双边滤波结合了空间信息和像素强度信息，通过加权平均处理邻域像素
工作原理：
    滤波权值由两部分组成：空间权值 (Spatial Weight): 根据像素之间的空间距离，距离越近的像素权值越高。
    颜色权值 (Range Weight): 根据像素值之间的差异，像素值越接近，权值越高。
    只有在距离接近且像素值相似的像素才对结果有较大贡献。
效果：能够很好地平滑图像噪声，同时保留边缘细节，与传统滤波器相比，双边滤波不会模糊边缘，因为边缘的像素值差异较大，颜色权值较低。
适用场景：图像去噪，同时保持边缘清晰，计算机视觉和图像处理中的预处理步骤，例如边缘检测、纹理分析等。
双边滤波的方法是 cv2.bilateralFilter()，除了被处理图像和滤波核大小两个参数外，双边滤波还需要指定 sigmaColor 和 sigmaSpace两个参数。
sigmaColor表示参与滤波处理的像素的范围（小于这个值才会参与计算、处理），sigmaSpace 则表示坐标空间的 σ 值，σ 越大，参与计算的像素数量就越多
"""
# 双边滤波，继续对 cloud.jpg 做双边滤波，滤波核大小为 9×9，sigmaColor 为 125，sigmaSpace 为 200
bilateral_img = cv2.bilateralFilter(img, 9, 125, 200)
# 保存双边滤波后的图像
cv2.imencode('.jpg', bilateral_img)[1].tofile("./images/output_05/双边滤波.jpg")