# 导包
import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./images/output_02", exist_ok=True)

"""
BGR 色彩空间
BGR 色彩空间是我们使用 python 的 OpenCV 库读取一般彩色图像时默认的色彩空间。
包含 B、G、R 三个色彩通道

需求：读取img1.jpg，以左上角顶点为原点，并打印出第 5 行，第 10 个像素点的像素值
"""
# 读取 img1 图像
# 使用 cv2.imread() 函数读取的图像像素组，默认为 BGR 色彩空间下的像素组的形式
image1 = cv2.imread("./images/img1.jpg")

# 检查图像是否加载成功
if image1 is None:
    print("图像加载失败，请检查文件路径")
else:
    # 打印第五行，第十个像素点的像素值
    print("第 5 行，第 10 列像素值 (BGR):", image1[4, 9])

"""
BGRA 色彩空间
BGRA 色彩空间是一个四通道的色彩空间，在BGR的基础上增加了一个 A 色彩通道，
A 通道即 alpha 通道，表示透明度，A 通道的取值也是[0,255]，一般的图像默认都是 255，表示不透明。
数值越小越透明。0 表示完全透明，172 可用来表示半透明。
保存 BGRA 色彩空间下的图片时，要保存为png格式的图片，因为 png 文件即为
BGRA 四通道色彩空间的图像文件形式。而不能保存为jpg文件了，否则会体现不出透明度这一属性

需求：读取 img1.jpg，将 image1 转到 BGRA 色彩空间，打印出转换后的像素数组，
并将图像中任意一部分设置为完全透明，任意一部分设置为半透明，保存为文件 "bgra_image1.png"
"""
# 转换色彩空间的方法是cv2.cvtColor()。不同色彩空间之间的进行转换时，通常需要一个转换码参数
# 转 BGRA 色彩空间  转换码为 cv2.COLOR_BGR2BGRA
bgra_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2BGRA)
# 打印转 BGRA 色彩通道后的像素数组
print(bgra_image1)
# 将 bgra_image1 的第 [100, 200] 行，第[200, 300]列的像素的透明度设置为 0
bgra_image1[100:200, 200:300, 3] = 0
# 将 bgra_image1 的第 [250, 350] 行，第[200, 300]列的像素的透明度设置为 172
bgra_image1[250:350, 200:300, 3] = 172
# 保存 BGRA 图像为 jpg 文件 "bgra_image1.png"
cv2.imwrite("./images/output_02/bgra_image1.png", bgra_image1)

"""
GRAY 色彩空间
GRAY 色彩空间是灰度色彩空间，只有一个通道，表示灰度值，灰度值的范围是[0,255]，
每个数值表示从黑变白的颜色深浅程度。0 表示纯黑色，255 表示纯白色，数值越大越趋于白色。

需求：读取 img1.jpg，将 image1 转到 GRAY 色彩空间（即转为灰度图像），打印出转换后的像素数组。
并将转换后的灰度图保存为文件 gray_image1.png
"""
# 转到 GRAY 色彩空间 转换码为 cv2.COLOR_BGR2GRAY
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# 打印转 GRAY 色彩通道后的像素数组
print(gray_image1)
# 保存 GRAY 图像为 jpg 文件 "gray_image1.png"
cv2.imwrite("./images/output_02/gray_image1.png", gray_image1)

"""
HSV 色彩空间
HSV 色彩空间是一个重要且特殊的色彩空间，BGR 色彩空间是基于三基色（红，绿，蓝） 而言的，
而 HSV 色彩空间是基于色调(H)，饱和度(S)和亮度(V) 而言的。HSV 色彩空间有 H 、 S 、 V 三个色彩通道
H: 色调，取值范围为[0,180]，表示光的颜色，0 表示红色，30 表示黄色，60 表示绿色，120 表示蓝色
S: 饱和度，取值范围为[0,255]，表示色彩的深浅，0 表示灰色，255 表示最纯的颜色
V: 亮度，取值范围为[0,255]，表示光的明暗，亮度为 0 时，图像为纯黑色，亮度为 255 时，图像为纯白色，亮度越大，图像越亮

读取 img1.jpg，将 image1 转到 HSV 色彩空间，然后直接保存为 image1_hsv.jpg。再将转色彩空间后的图像，
H 分别调为 0，30，60 后，转回 BGR 色彩空间，再依次保存为 image1_h0.jpg，image1_h30.jpg，image1_h60.jpg
"""
# 转到 HSV 色彩空间 转换码为 cv2.COLOR_BGR2HSV
image1_hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
# 保存 HSV 图像为 jpg 文件 "image1_hsv.jpg"
cv2.imwrite("./images/output_02/image1_hsv.jpg", image1_hsv)

# 将 image1_hsv 的 H 通道设置为 0
image1_h0 = image1_hsv.copy()
image1_h0[:, :, 0] = 0
# 将 H 通道设置为 0 后的图像转回 BGR 色彩空间
image1_h0_bgr = cv2.cvtColor(image1_h0, cv2.COLOR_HSV2BGR)
# 保存 BGR 图像为 jpg 文件 "image1_h0.jpg"
cv2.imwrite("./images/output_02/image1_h0.jpg", image1_h0_bgr)

# 将 image1_hsv 的 H 通道设置为 30
image1_h30 = image1_hsv.copy()
image1_h30[:, :, 0] = 30
# 将 H 通道设置为 30 后的图像转回 BGR 色彩空间
image1_h30_bgr = cv2.cvtColor(image1_h30, cv2.COLOR_HSV2BGR)
# 保存 BGR 图像为 jpg 文件 "image1_h30.jpg"
cv2.imwrite("./images/output_02/image1_h30.jpg", image1_h30_bgr)

# 将 image1_hsv 的 H 通道设置为 60
image1_h60 = image1_hsv.copy()
image1_h60[:, :, 0] = 60
# 将 H 通道设置为 60 后的图像转回 BGR 色彩空间
image1_h60_bgr = cv2.cvtColor(image1_h60, cv2.COLOR_HSV2BGR)
# 保存 BGR 图像为 jpg 文件 "image1_h60.jpg"
cv2.imwrite("./images/output_02/image1_h60.jpg", image1_h60_bgr)
