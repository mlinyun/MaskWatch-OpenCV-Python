import cv2
import os
from datetime import datetime


class VideoCamera(object):
    def __init__(self):
        # 加载摄像头
        self.cap = cv2.VideoCapture(0)
        # 加载识别眼睛的级联分类器
        self.eyes_cascade = cv2.CascadeClassifier("./cascade_classifier/haarcascade_eye_tree_eyeglasses.xml")
        # 初始化上一次识别到的瞳孔个数为 0
        self.last_eyes_num = 0
        # 初始化上一次识别到的口罩情况
        self.last_result = ""
        # 初始化浮动字体的初始高度，为 500
        self.label_location = 500
        # 初始化要显示的画面，初始为空
        self.frame = []
        # 初始化肤色图
        self.skin = []
        # 创建存储图像的文件夹
        self.set_dir()

    # 创建存储图像的文件夹
    def set_dir(self):
        # 如果 images 文件夹不存在与当前目录，则创建该文件夹
        self.dir1 = "./images"
        if not os.path.exists(self.dir1):
            os.mkdir(self.dir1)
        date = datetime.now().strftime('%Y-%m-%d')
        self.dir2 = "./images/" + date
        if not os.path.exists(self.dir2):
            os.mkdir(self.dir2)
        # 分别存储有口罩和无口罩
        self.masked_dir = os.path.join(self.dir2, "masked")
        self.unmasked_dir = os.path.join(self.dir2, "unmasked")
        if not os.path.exists(self.masked_dir):
            os.mkdir(self.masked_dir)
        if not os.path.exists(self.unmasked_dir):
            os.mkdir(self.unmasked_dir)

    # 识别瞳孔
    def detect_eyes(self, frame):
        # 使用高斯滤波器对图像进行灰度处理
        image = cv2.GaussianBlur(frame, (5, 5), 0)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 使用级联分类器识别瞳孔
        return self.eyes_cascade.detectMultiScale(gray, 1.3, 5)

    # 分析口罩区域
    def analyze_mask_area(self, eyes):
        # 定义眼部范围
        x1, y1, w1, h1 = eyes[0]
        x2, y2, w2, h2 = eyes[1]
        if x1 < x2:
            left_eye = (x1, y1, w1, h1)
            right_eye = (x2, y2, w2, h2)
        else:
            left_eye = (x2, y2, w2, h2)
            right_eye = (x1, y1, w1, h1)
        x, y, w, h = (
            left_eye[0],
            left_eye[1],
            right_eye[0] - left_eye[0] + right_eye[2],
            int(0.5 * (h1 + h2)),
        )
        # 分析口罩区域
        mask_area = self.skin[int(y + 1.5 * h): int(y + 2.5 * h), int(x): int(x + w)]
        # 计算皮肤区域面积
        contours, _ = cv2.findContours(mask_area, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return sum(cv2.contourArea(cont) for cont in contours), (w * h * 0.1)

    # 保存检测结果
    def save_detection_result(self):
        now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        if self.last_result == "Have Mask":
            filename = os.path.join(self.masked_dir, now + ".jpg")
        else:
            filename = os.path.join(self.unmasked_dir, now + ".jpg")
        cv2.imwrite(filename, self.frame)

    # 获取画面，并调整为预期大小，并识别瞳孔
    def get_frame(self):
        ret, self.frame = self.cap.read()
        # 调整为竖屏（生活中常用的人脸识别机为竖屏界面） 且长480像素，高720像素（即放大了画面）
        self.frame = cv2.resize(self.frame[:, 160:480], (480, 720))
        # 生成肤色图
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        H, S, V = cv2.split(hsv)
        self.skin = cv2.inRange(H, 3, 12)

        # 如果上一次识别没有识别到瞳孔，则这一次继续正常识别
        if self.last_eyes_num == 0:
            # 识别瞳孔
            eyes = self.detect_eyes(self.frame)
            # 如果本次识别，识别到两只眼睛，则符合我们的预期，可以继续检测
            if len(eyes) == 2:
                # 记录本次识别到的瞳孔个数 2
                self.last_eyes_num = 2
                # 分析口罩区域
                skin_area_mask, area_standard = self.analyze_mask_area(eyes)
                self.last_result = " No Mask" if skin_area_mask > area_standard else "Have Mask"
                self.save_detection_result()
            # 如果本次仍然没有识别到瞳孔 ，则显示"Mask recognition platform is running" (口罩识别平台正在运行)
            else:
                # 如果识别到的不是2只眼睛，则一律按照0只眼睛的情况处理
                self.last_eyes_num = 0
                # 在画面上增加一个矩形的信息框来装饰我们的界面
                self.frame[530:630, 40:440] = [255, 204, 102]
                cv2.putText(self.frame, "Mask recognition", (80, 570), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 3)
                cv2.putText(self.frame, "Platform is running", (60, 610), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255),
                            3)

        # 如果上一帧识别到瞳孔了，则在接下来的几秒内不识别 （作为通行间隔），但播放动画
        else:
            # 如果上一次结果是有口罩
            if self.last_result == "Have Mask":
                label1 = "   Please "
                label2 = "  come in!"
                label_color = (0, 255, 0)
                h_value = 60
            # 如果上一次结果是无口罩
            else:
                label1 = "Please wear"
                label2 = " a  mask! "
                label_color = (0, 0, 255)
                h_value = 0

            # 使字体表现出浮动效果（从下向上浮动，对应从500位置到200位置）（浮动期间不识别）
            if self.label_location > 200:
                # 使用HSV加个滤镜效果，有口罩则加绿色滤镜，无口罩则加红色滤镜
                hsv_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
                h, s, v = cv2.split(hsv_frame)
                h[:, :] = h_value
                hsv = cv2.merge([h, s, v])
                self.frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

                # 在画面上增加一个矩形的信息框来装饰我们的界面
                self.frame[530:630, 40:440] = [255, 204, 102]
                cv2.putText(self.frame, label1, (40, self.label_location - 60), cv2.FONT_HERSHEY_TRIPLEX, 2,
                            label_color, 5)
                cv2.putText(self.frame, label2, (40, self.label_location), cv2.FONT_HERSHEY_TRIPLEX, 2, label_color, 5)
                cv2.putText(self.frame, self.last_result, (50, 600), cv2.FONT_HERSHEY_TRIPLEX, 2, label_color, 5)

                # 每过一帧，向上移动5个单位的像素
                self.label_location -= 5
            else:
                # 动画播放完毕后，还需要稍微间隔等待一下
                if self.label_location > 50:
                    self.frame[530:630, 40:440] = [255, 204, 102]
                    cv2.putText(self.frame, "Mask recognition", (80, 570), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255),
                                3)
                    cv2.putText(self.frame, "Platform is running", (60, 610), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                (255, 255, 255), 3)
                    self.label_location -= 5
                else:
                    self.frame[530:630, 40:440] = [255, 204, 102]
                    # 循环属性初始化
                    self.label_location = 500
                    self.last_eyes_num = 0


if __name__ == '__main__':
    video = VideoCamera()
    while True:
        video.get_frame()
        cv2.imshow("Mask real-time monitoring system", video.frame)
        key = cv2.waitKey(1)
        # 如果点击右上角的叉，则关闭、销毁窗口，循环停止
        if cv2.getWindowProperty("Mask real-time monitoring system", cv2.WND_PROP_VISIBLE) < 1:
            break
    video.cap.release()
    cv2.destroyAllWindows()
