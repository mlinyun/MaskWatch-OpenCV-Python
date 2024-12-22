import cv2

capture = cv2.VideoCapture(0)
while (capture.isOpened()):
    # 读取每一帧画面
    retval, image = capture.read()
    cv2.imshow("Video", image)
    # 窗口的图像刷新时间为1毫秒
    key = cv2.waitKey(1)
    if key == 32:  # 数字 32 表示空格键
        break
# 最后一定要记得，及时销毁窗口
capture.release()
cv2.destroyAllWindows()
