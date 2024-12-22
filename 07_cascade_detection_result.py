import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./images/output_07", exist_ok=True)

# 读取图片 img3.jpg
img1 = cv2.imread("./images/img3.jpg")

"""
人脸检测
"""
# 加载识别人脸的级联分类器 "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier("./cascade_classifier/haarcascade_frontalface_default.xml")
# 识别出所有人脸
faces = faceCascade.detectMultiScale(img1, 1.3)
# 将识别出的人脸用矩形描出
for (x, y, w, h) in faces:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 5)

cv2.imwrite("./images/output_07/faces.jpg", img1)

"""
瞳孔检测
"""
# 加载识别瞳孔的级联分类器 "haarcascade_eye_tree_eyeglasses.xml"
faceCascade = cv2.CascadeClassifier("./cascade_classifier/haarcascade_eye_tree_eyeglasses.xml")
# 高斯滤波 5*5滤波核
image = cv2.GaussianBlur(img1, (5, 5), 0)
# 灰度处理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 识别出所有瞳孔
eyes = faceCascade.detectMultiScale(gray, 1.1, 5)
print(eyes)
# 将识别出的人脸用矩形描出
for (x, y, w, h) in eyes:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 5)
cv2.imwrite("./images/output_07/eyes.jpg", img1)
