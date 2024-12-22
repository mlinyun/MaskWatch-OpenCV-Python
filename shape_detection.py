# 导包
import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./images/output_06", exist_ok=True)

# 读取图片 img4.jpg
img = cv2.imread("./images/img4.jpg")

"""
轮廓识别与描绘
"""
# 灰度处理
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化处理
ret, binary = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
# 查找轮廓：检测图像中出现的所有轮廓，记录轮廓中的每一个点
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 画出轮廓：绘制所有的轮廓，宽度为 5，颜色为红色。-1 作为轮廓的索引，表示绘制所有轮廓
contours_img = cv2.drawContours(img, contours, -1, (0, 0, 255), 5)
# 保存描绘轮廓后的图像
cv2.imencode('.jpg', contours_img)[1].tofile("./images/output_06/img4_所有轮廓.jpg")

"""
提取皮肤特征
轮廓检测还可以应用于检测皮肤的特征。结合我们前边讲到的对肤色图的绘制，这里将其与轮廓提取结合起来，便可以为口罩识别提供出思路
"""
# 读取图片 img3.jpg
img = cv2.imread("./images/img3.jpg")
# 转到 HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 拆分 HSV 色彩通道 使用 cv2.split() 方法更为快捷
H, S, V = cv2.split(img_hsv)
# 将 H 值大于 [3, 12] 的部分变为 255 其余的变为 0。
img_skin = cv2.inRange(H, 3, 12)
# 查找轮廓：检测图像中出现的所有轮廓，记录轮廓中的每一个点
contours2, hierarchy2 = cv2.findContours(img_skin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 画出轮廓：绘制所有的轮廓，宽度为 5，颜色为红色。-1 作为轮廓的索引，表示绘制所有轮廓
contours_img2 = cv2.drawContours(img, contours2, -1, (0, 0, 255), 5)
# 保存描绘轮廓后的图像
cv2.imencode('.jpg', contours_img2)[1].tofile("./images/output_06/img3_所有轮廓.jpg")

"""
Canny 边缘检测
Canny 边缘检测算法是John F.Canny在 1986 年开发的一个多级边缘检测算法。Canny 边缘检测算法通过像素的梯度变化寻找图像的边缘，
最终可以绘制出十分精细的二值边缘图像。不仅仅是在计算机识别方面，Canny 边缘检测得到的图像本身也就具有着很高的艺术效果，且用法简单
使用 Canny 边缘检测时存在两个阈值，关于这两个阈值怎么用，这涉及到了算法的底层逻辑。这里一种可以接受的解释是：
低于阈值 1 的像素点，会被认为不构成边缘，而高于阈值 2 的像素点，会被认为构成边缘
"""
# 以 img4.jpg 图像为例，分别选择三组阈值：(10, 50)，(100, 200)，(300, 500)，来使用 Canny 边缘检测
# 读取图片 img4.jpg
img = cv2.imread("./images/img4.jpg")
# 以 (10, 50) 为阈值进行 Canny 边缘检测
edges1 = cv2.Canny(img, 10, 50)
cv2.imwrite("./images/output_06/img4_Canny_10_50.jpg", edges1)
# 以 (100, 200) 为阈值进行 Canny 边缘检测
edges2 = cv2.Canny(img, 100, 200)
cv2.imwrite("./images/output_06/img4_Canny_100_200.jpg", edges2)
# 以 (300, 500) 为阈值进行 Canny 边缘检测
edges3 = cv2.Canny(img, 300, 500)
cv2.imwrite("./images/output_06/img4_Canny_300_500.jpg", edges3)
