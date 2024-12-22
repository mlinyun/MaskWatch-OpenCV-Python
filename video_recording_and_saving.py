import os

import cv2

# 确保保存路径的文件夹存在
os.makedirs("./video/output", exist_ok=True)

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 设定编码格式
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
# 保存每一帧
output = cv2.VideoWriter("./video/output/new_Video.avi", fourcc, 20, (640, 480))
while capture.isOpened():
    retval, frame = capture.read()
    if retval == True:
        output.write(frame)
        cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    # 如果按下Esc键 则停止录制
    if key == 27:
        break
# 关闭摄像头
capture.release()
# 释放VideoWriter类对象 销毁窗口
output.release()
cv2.destroyAllWindows()
