import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./images/output_09", exist_ok=True)


def skin(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 拆分HSV色彩通道 使用cv2.split()方法更为快捷
    H, S, V = cv2.split(img_hsv)
    img_skin = cv2.inRange(H, 3, 12)
    return img_skin


img1 = cv2.imread("./images/p3.jpg")
img2 = cv2.imread("./images/p5.jpg")
cv2.imwrite("./images/output_09/p3_h.jpg", skin(img1))
cv2.imwrite("./images/output_09/p5_h.jpg", skin(img2))
