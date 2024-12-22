import cv2

# 读取视频文件
video = cv2.VideoCapture("./video/video.mp4")
# 获取视频帧数
frame_Count = video.get(cv2.CAP_PROP_FRAME_COUNT)
# 设置帧数
i = 0

while (video.isOpened()):
    retval, image1 = video.read()  # 原图像
    image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 灰度
    image3 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)  # 转到HSV色彩空间
    t4, image4 = cv2.threshold(image2, 127, 255, cv2.THRESH_TOZERO)  # 低于阈值零处理
    t5, image5 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)  # 二值化处理
    image6 = cv2.Canny(image1, 10, 50)  # 阈值为10-50的Canny边缘检测
    image7 = cv2.Canny(image1, 200, 400)  # 阈值为200-400的Canny边缘检测
    # 设置“Video”窗口 并调整大小
    cv2.namedWindow("video_1", 0)
    cv2.resizeWindow("video_1", 426, 240)
    cv2.namedWindow("video_2", 0)
    cv2.resizeWindow("video_2", 426, 240)
    cv2.namedWindow("video_3", 0)
    cv2.resizeWindow("video_3", 426, 240)
    cv2.namedWindow("video_4", 0)
    cv2.resizeWindow("video_4", 426, 240)
    cv2.namedWindow("video_5", 0)
    cv2.resizeWindow("video_5", 426, 240)
    cv2.namedWindow("video_6", 0)
    cv2.resizeWindow("video_6", 426, 240)
    cv2.namedWindow("video_7", 0)
    cv2.resizeWindow("video_7", 426, 240)
    # 播放视频
    if retval == True:
        cv2.imshow("video_1", image1)
        cv2.imshow("video_2", image2)
        cv2.imshow("video_3", image3)
        cv2.imshow("video_4", image4)
        cv2.imshow("video_5", image5)
        cv2.imshow("video_6", image6)
        cv2.imshow("video_7", image7)
    else:
        break
    # 窗口的图像刷新时间为10毫秒 则帧速率为100帧/秒
    key = cv2.waitKey(10)
    # 按空格键暂停播放
    if key == 32:  # 数字 32 表示空格键
        cv2.waitKey(0)
        continue
    # 按Esc键关闭窗口（停止播放）
    if key == 27:  # 数字 27 表示Esc键
        break
    i += 1
    if i == frame_Count:
        break

# 销毁窗口
video.release()
cv2.destroyAllWindows()
