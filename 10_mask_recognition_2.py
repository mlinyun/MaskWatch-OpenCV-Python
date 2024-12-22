import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./images/output_09", exist_ok=True)

# 识别瞳孔的级联分类器
eyes_cascade = cv2.CascadeClassifier("./cascade_classifier/haarcascade_eye_tree_eyeglasses.xml")


# 定义一个检测口罩的函数，传入图像的BGR像素数组，输出识别结果
def mask_detect(img):
    # HSV色彩空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 拆分色彩通道
    H, S, V = cv2.split(hsv)
    skin = cv2.inRange(H, 3, 12)
    # 高斯滤波
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # 灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 识别眼睛
    eyes = eyes_cascade.detectMultiScale(gray, 1.3, 5)
    # 口罩与眼部面积初始化
    skin_area_mask = 0
    # 如果识别到两只眼睛
    if len(eyes) == 2:
        # 检测口罩
        x1, y1, w1, h1 = eyes[0]
        x2, y2, w2, h2 = eyes[1]
        # 区分左眼，右眼 以便确定坐标，定义瞳孔区域
        if x1 < x2:
            left_eye = (x1, y1, w1, h1)
            right_eye = (x2, y2, w2, h2)
        else:
            left_eye = (x2, y2, w2, h2)
            right_eye = (x1, y1, w1, h1)
        # 定义瞳孔区域 其中(x,y)是左上角坐标，w和h是宽和高
        x, y, w, h = (left_eye[0], left_eye[1], right_eye[0] - left_eye[0] + right_eye[2], int(0.5 * (h1 + h2)))
        # 定义口罩区域 相比瞳孔区域，水平方向上边界不变，竖直方向上向下移动1.5倍h长度
        mask_area = skin[int(y + 1.5 * h):int(y + 2.5 * h), int(x):int(x + w)]
        # 定义口罩区域面积标准
        area_standard = w * h * 0.1
        # 寻找皮肤 使用轮廓检测的方法
        contours, hierarchy = cv2.findContours(mask_area, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cont in contours:
            Area = cv2.contourArea(cont)
            skin_area_mask += Area
        print("skin_area_mask=", skin_area_mask)
        # 判断是否有口罩 如果检测到皮肤面积大于口罩区域面积的1/10则认为无口罩
        if skin_area_mask > area_standard:
            print("您没有佩戴口罩，请佩戴口罩!")
            cv2.putText(img, "No Mask", (300, 600), cv2.FONT_HERSHEY_TRIPLEX, 3, (0, 0, 255), 2)
        else:
            print("已佩戴口罩，感谢您的配合!")
            cv2.putText(img, "Have Mask", (300, 600), cv2.FONT_HERSHEY_TRIPLEX, 3, (0, 255, 0), 2)
    # 如果识别到眼睛数量不为2，则pass
    else:
        pass
    return img


if __name__ == '__main__':
    image1 = cv2.imread("./images/p2.jpg")
    image2 = cv2.imread("./images/p3.jpg")
    image3 = cv2.imread("./images/p4.jpg")
    image4 = cv2.imread("./images/p5.jpg")
    result5 = mask_detect(image1)
    result6 = mask_detect(image2)
    result7 = mask_detect(image3)
    result8 = mask_detect(image4)
    cv2.imwrite("./images/output_09/result5.jpg", result5)
    cv2.imwrite("./images/output_09/result6.jpg", result6)
    cv2.imwrite("./images/output_09/result7.jpg", result7)
    cv2.imwrite("./images/output_09/result8.jpg", result8)
