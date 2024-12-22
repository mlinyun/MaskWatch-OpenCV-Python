# 导包
import os

import cv2
import numpy as np

# 确保保存路径的文件夹存在
os.makedirs("./images/output_04", exist_ok=True)

"""
绘制线段
cv2.line(img, pt1, pt2, color, thickness=None) 其中 img 指背景图像的像素数组，pt1 和 pt2 分别表示
线段两个端点的坐标，坐标要求以元组的形式传入，如(y,x)。thickness 表示线条的宽度

需求：使用 numpy 数组创建一个高 800，宽 600 的白板图像。在该图像上依次使用红、黄、蓝、绿四种颜色画出四条首尾
相连的线段（相邻的线段要求垂直），对应的线宽依次为 5, 10, 15, 20。其中第一条红色的线的 pt1 为(100,200)，
pt2为(500,200)。其他点的坐标请自行计算。最终结果保存为文件lines.jpg
"""
# 绘制线段
# 创建一个白板图像
canvas1 = np.ones((800, 600, 3), np.uint8) * 255
# 第一根线 红色 thickness=5
canvas1 = cv2.line(canvas1, (100, 200), (500, 200), (0, 0, 255), 5)
# 第二根线 黄色 thickness=10
canvas1 = cv2.line(canvas1, (500, 200), (500, 600), (0, 255, 255), 10)
# 第三根线 蓝色 thickness=15
canvas1 = cv2.line(canvas1, (500, 600), (100, 600), (255, 0, 0), 15)
# 第四根线 绿色 thickness=20
canvas1 = cv2.line(canvas1, (100, 600), (100, 200), (0, 255, 0), 20)
# 保存图像为"lines.jpg"
cv2.imwrite("./images/output_04/lines.jpg", canvas1)

"""
绘制矩形
cv2.rectangle(img, pt1, pt2, color, thickness=None) 其中 pt1 表示矩形左上角坐标，pt2 表示矩形右下角坐标。
其他参数同上。绘制图形默认为空心图形。thickness 如果为负数则表示所绘图形为实心图形

需求：绘制上例子中尺寸的白板图像，然后绘制一个红色空心矩形，pt1 为(100,100)，pt2 为(500,300)，线宽为 10。
绘制一个绿色实心矩形 pt1 为(100,500)，pt2 为(500,500)。最终图像保存为 rectangles.jpg
"""
# 绘制矩形
# 创建白色画布
canvas2 = np.ones((800, 600, 3), np.uint8) * 255
# 绘制红色空心矩形
canvas2 = cv2.rectangle(canvas2, (100, 100), (500, 300), (0, 0, 255), 10)
# 绘制绿色实心矩形
canvas2 = cv2.rectangle(canvas2, (100, 500), (500, 700), (0, 255, 0), -10)
# 保存图像为"rectangles.jpg"
cv2.imwrite("./images/output_04/rectangles.jpg", canvas2)

"""
绘制圆形
circle(img, center, radius, color, thickness=None) 其中 center 表示圆心坐标，radius 表示半径。其余同上

需求：绘制上例子中尺寸的白板图像，以(300,200)位置为圆心，100 为半径，绘制一个蓝色的空心圆，以(300,600)为圆心，
100 为半径绘制一个黄色的实心圆。最后将图像保存为 circles.jpg
"""
# 绘制圆形
# 创建白色画布
canvas3 = np.ones((800, 600, 3), np.uint8) * 255
# 绘制蓝色空心圆
canvas3 = cv2.circle(canvas3, (300, 200), 100, (255, 0, 0), 5)
# 绘制黄色实心圆
canvas3 = cv2.circle(canvas3, (300, 500), 100, (0, 255, 255), -5)
# 保存图像为"circles.jpg"
cv2.imwrite("./images/output_04/circles.jpg", canvas3)

"""
绘制多边形
polylines(img, pts, isClosed, color, thickness=None) 表示绘制多边形，pts 是一个列表，
列表内是一个 shape 为(n,2)的numpy 数组：形如[[a, b], [c, d], [e, f], [g, h], …]。
其中[a,b]，[c,d]等是每个顶点的坐标，绘制图形时对齐依次相连，所以这里的坐标传入时是要考虑顺序的

需求：在白色画布上绘制一个空心红色五边形，五个顶点的坐标依次为(300,100),(500,200),(400,370),(200,370),(100,200)。线宽为 5。最终将得到的图片文件保存为五边形.jpg
"""
# 绘制多边形(空心五边形)
# 创建白色画布
canvas4 = np.ones((800, 600, 3), np.uint8) * 255
# 创建顶点坐标的二维数组 (300,100),(500,200),(400,370),(200,370),(100,200)
pts = np.array([[300, 100], [500, 200], [400, 370], [200, 370], [100, 200]], np.int32)
# 绘制空心五边形
canvas4 = cv2.polylines(canvas4, [pts], True, (0, 0, 255), 5)
cv2.imencode('.jpg', canvas4)[1].tofile("./images/output_04/五边形.jpg")

"""
添加文字
Python 的 OpenCV 库中提供了添加文字的方法，cv2.putText() 。这个方法会比较常用，可以将某些我们需要的信息直观地标注在图像上。

需求：在白色画布上，选择 cv2.FONT_HERSHEY_TRIPLEX字体，使用绿色字体写出“Have Mask”，位置坐标为(150,200)，
使用红色 5 号字体写出“No Mask”，位置坐标为(150,400)。字体大小为 2，线条宽度为 5。最终保存为 “添加文字.jpg”
"""
# 图像添加文字
# 创建白色画布
canvas5 = np.ones((800, 600, 3), np.uint8) * 255
# 添加绿色文字 “Have Mask”
cv2.putText(canvas5, "Have Mask", (150, 200), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 5)
# 添加红色文字 "No Mask"
cv2.putText(canvas5, "No Mask", (150, 400), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 5)
# 保存图像为 “添加文字.jpg”
cv2.imencode('.jpg', canvas5)[1].tofile("./images/output_04/添加文字.jpg")
