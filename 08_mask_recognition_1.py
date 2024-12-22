import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./images/output_08", exist_ok=True)

# 识别瞳孔的级联识别器
eyes_cascade = cv2.CascadeClassifier("./cascade_classifier/haarcascade_eye_tree_eyeglasses.xml")
# 加载识别口罩的级联识别器
mask_detector = cv2.CascadeClassifier("./cascade_classifier/mask_cascade.xml")


# 定义一个检测口罩的函数，传入图像的BGR像素数组，输出识别结果
def mask_detect(img):
    # 高斯滤波
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # 灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 识别眼睛
    eyes = eyes_cascade.detectMultiScale(gray, 1.3, 5)
    # 如果识别到两只眼睛
    if len(eyes) == 2:
        # 检测口罩
        masks = mask_detector.detectMultiScale(gray, 1.1, 5)
        # 如果识别到口罩数量不为 0
        if len(masks) != 0:
            # 输出结果
            print("已佩戴口罩。")
            # 添加矩形框 和 "Have Mask"字体
            for (x, y, w, h) in masks:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img = cv2.putText(img, "Have Mask", (300, 600), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 2)

        else:
            # 添加 "No Mask" 字体
            img = cv2.putText(img, "No Mask", (300, 600), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2)
            print("未佩戴口罩。")
    else:
        # pass 不做任何响应
        pass
    # 返回添加有识别信息的图像
    return img


if __name__ == '__main__':
    # 读取图像
    image1 = cv2.imread("./images/p2.jpg")
    image2 = cv2.imread("./images/p3.jpg")
    image3 = cv2.imread("./images/p4.jpg")
    image4 = cv2.imread("./images/p5.jpg")
    # 调用口罩检测函数
    result1 = mask_detect(image1)
    result2 = mask_detect(image2)
    result3 = mask_detect(image3)
    result4 = mask_detect(image4)
    # 保存图像 依次为 'result1.jpg', 'result2.jpg', 'result3.jpg', 'result4.jpg'
    cv2.imwrite("./images/output_08/result1.jpg", result1)
    cv2.imwrite("./images/output_08/result2.jpg", result2)
    cv2.imwrite("./images/output_08/result3.jpg", result3)
    cv2.imwrite("./images/output_08/result4.jpg", result4)
