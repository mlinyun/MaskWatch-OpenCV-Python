import cv2

"""
二值化处理与反二值化处理
二值化处理，即对图像做非黑即白的处理。二值处理将图像在 GRAY 色彩空间中，大于阈值的像素值都变为 0（黑色），小于阈值的像素值都变为 255（白色）。
反二值化处理则刚好相反，也是非黑即白的处理，不同的是将大与阈值的像素处理为白色，小于阈值的像素处理为了黑色。
做二值化处理的 type 参数为 cv2.THRESH_BINARY。做反二值化处理的 type 参数为 cv2.THRESH_BINARY_INV。

需求：以 127 位阈值，对 img2.jpg 分别进行二值化处理和反二值化处理。并将文件保存为 "img2二值化处理.jpg" 和 "img2反二值化处理.jpg"
"""
# 将图像读成灰度图像
img = cv2.imread("./images/img2.jpg", cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE 的常量值为 0

# 二值化处理，阈值为 127。其中返回的 ret1 是阈值，thresh 是处理后的图像
ret1, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print("二值化处理的阈值：", ret1)
# 保存二值化处理后的图像
# 使用下面的方式保存图像，可以避免中文乱码问题
cv2.imencode('.jpg', thresh)[1].tofile("./images/img2二值化处理.jpg")

# 反二值化处理，阈值为 127。其中返回的 ret2 是阈值，thresh_inv 是处理后的图像
ret2, thresh_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
print("反二值化处理的阈值：", ret2)
# 保存反二值化处理后的图像
cv2.imencode('.jpg', thresh_inv)[1].tofile("./images/img2反二值化处理.jpg")

"""
截断处理
截断处理，就是将大与阈值的像素值设置得跟阈值一样，小于阈值的则保持不变。做截断处理的 type 参数为cv2.THRESH_TRUNC，其余部分基本不变。

需求：下边要求对 img2.jpg 做阈值为 127 的截断处理
"""
ret3, thresh_trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
print("截断处理的阈值：", ret3)
# 保存截断处理后的图像为 "img2截断处理.jpg"
cv2.imencode('.jpg', thresh_trunc)[1].tofile("./images/img2截断处理.jpg")

"""
零处理
零处理分为低阈值零处理和高阈值零处理。低阈值零处理将低于阈值的像素值变为 0，高阈值零处理则将高于阈值的像素值变为 0
低阈值零处理对应的 type 参数为cv2.THRESH_TOZERO，而高阈值零处理对应的 type 参数为cv2.THRESH_TOZERO_INV。

需求：下边要求对img2.jpg进行低阈值零处理和高阈值零处理。
"""
# 做低阈值零处理 并保存为 "img2低阈值零处理.jpg"
ret4, thresh_tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
print("低阈值零处理的阈值：", ret4)
cv2.imencode('.jpg', thresh_tozero)[1].tofile("./images/img2低阈值零处理.jpg")

# 做高阈值零处理 并保存为 "img2高阈值零处理.jpg"
ret5, thresh_tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
print("高阈值零处理的阈值：", ret5)
cv2.imencode('.jpg', thresh_tozero_inv)[1].tofile("./images/img2高阈值零处理.jpg")

"""
自适应阈值处理
自适应处理是一种经过改进的阈值处理技术，该方法是对图像区域中的某一正方形区域内的所有色素值使用指定的算法而得到的，
如平均法和高斯法，从而对图像的像素进行相应的处理。自适应处理本身不属于阈值处理方法，算是对阈值处理的改进，
其使用过程中可以选择使用二值化处理或反二值化处理的处理方式。进行自适应处理的方法是 cv2.adaptiveThreshold()方法。
自适应阈值处理的 type 参数为 cv2.ADAPTIVE_THRESH_MEAN_C 或 cv2.ADAPTIVE_THRESH_GAUSSIAN_C。
使用平均法的 type 参数为 cv2.ADAPTIVE_THRESH_MEAN_C，该方法对对一个正方形区域内的所有像素进行平均加权。
使用高斯法的 type 参数为 cv2.ADAPTIVE_THRESH_GAUSSIAN_C，该方法根据高斯函数按照像素与中心店的距离对一个正方形区域内的所有像素进行加权计算。
使用这两种算法时，都需要指定正方形区域的边长，即每条边上像素的个数。此外还需要指定一个常量，最终的阈值等于均值减去这个常量 或 加权值减去这个常量。
这两种方法得到的结果会有一定的差异

需求：要求以二值化处理为例，对 img2.jpg 分别使用平均法和高斯法进行自适应处理，正方形边长指定为 5
"""
# 自适应处理 以 img2.jpg 的二值化处理为例 正方形边长为5 常量为3
# 使用平均法
thresh_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
# 保存自适应处理的结果为 "img2均值法自适应处理.jpg"
cv2.imencode('.jpg', thresh_mean)[1].tofile("./images/img2均值法自适应处理.jpg.jpg")
# 使用高斯法
thresh_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
# 保存自适应处理的结果为 "img2高斯法自适应处理.jpg"
cv2.imencode('.jpg', thresh_gaussian)[1].tofile("./images/img2高斯法自适应处理.jpg")

"""
OTSU 方法
OTSU 方法是一种自动确定阈值的方法，该方法是一种全局阈值处理方法，其目的是找到一个阈值，使得分割后的两个类间方差最大。

需求：对 img2.jpg 使用 OTSU 的二值化处理，并将图片保存为 "img2_OTSU的二值化处理.jpg"
"""
# 使用 OTSU 方法进行二值化处理
ret6, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("OTSU 方法的阈值：", ret6)
# 保存 OTSU 方法处理的结果为 "img2_OTSU的二值化处理.jpg"
cv2.imencode('.jpg', thresh_otsu)[1].tofile("./images/img2_OTSU的二值化处理.jpg")

"""
以图像在 HSV 色彩空间中的色调（H值）的阈值为准，进行阈值处理，得到肤色图
"""
# 读取图片 img.jpg
img = cv2.imread("./images/img3.jpg")
# 转到 HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 拆分 HSV 色彩通道 使用 cv2.split() 方法更为快捷
H, S, V = cv2.split(img_hsv)
# 将 H 值大于 [3, 12] 的部分变为 255 其余的变为 0。
img_skin = cv2.inRange(H, 3, 12)
# 保存文件为 "img3_skin.jpg"
cv2.imwrite("./images/img3_skin.jpg", img_skin)
