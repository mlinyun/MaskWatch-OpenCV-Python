# 导包
import cv2
import numpy as np

# 读取 image1 并打印其像素组
image1 = cv2.imread("./images/img1.jpg")
print(image1)

# 取出image1的shape属性，并打印查看
image1_shape = image1.shape
print(image1_shape)

"""
需求一：需要对图像进行简单的处理并保存：将图像的右边的
一半变为绿色，然后在原目录下保存为文件img1_1.jpg 。
"""
# 将 image1 复制给 image2，然后对 image2 进行修改。以达到保留变量 image1 的目的
image2 = image1.copy()
# 计算图像水平方向上一半的位置，一定要取整数
half_width = image2.shape[1] // 2
# 将图像的右半边变为绿色
image2[:, half_width:, :] = [0, 255, 0]
# 保存图像
cv2.imwrite("./images/img1_1.jpg", image2)

"""
需求二：通过 OpenCV 的像素数组，创建出左上，右上，右下，左下
四个区域依次为相同面积的蓝色，绿色，红色，白色的图像，要求图像
分辨率为 600×400，每个区域分辨率为 300×200。（其中，600×400
表示，宽为 600，高为 400）。并保存，文件名为four_color.jpg。
"""
# 定义表示图像的宽度和高度的变量
width, height = 600, 400
# 首先创建一个全白（数组都为1）或全黑（数组都为0）的图像，然后在此基础上对其进行修改
image3 = np.ones((height, width, 3), np.uint8) * 255
# 计算每个区域的宽度和高度
region_width, region_height = width // 2, height // 2
print(region_height, region_width)
# 分别对四个区域进行修改
# 通过数组切片的方式，表示出图像的四个区域
# 左上角区域为蓝色 颜色通道为BGR，可以用列表或者元组表示
image3[:region_height, :region_width] = [255, 0, 0]
# 右上角区域为绿色
image3[:region_height, region_width:] = [0, 255, 0]
# 左下角区域为红色
image3[region_height:, region_width:] = [0, 0, 255]
# 右下角区域为白色
image3[region_height:, :region_width] = [255, 255, 255]
# 保存图像
cv2.imwrite("./images/four_color.jpg", image3)

# 显示图像，窗口标题为 img1，图像为 image1，按任意键退出
cv2.imshow("img1", image1)
# 因为窗口的显示是瞬间的，程序结束后窗口就会关闭
# 所以使用 cv2.imshow() 后常常需要添加一个时间约束，防止程序执行完毕后窗口关闭
# waitKey() 表示无限期等待一个键盘事件，如果键盘被点击，则窗口关闭，如果没有点击，则程序一直等待
cv2.waitKey(0) # 等待按键，参数为 0 表示无限等待
# 销毁所有窗口
cv2.destroyAllWindows()
