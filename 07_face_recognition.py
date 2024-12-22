import cv2
import numpy as np

# 加载识别人脸的级联分类器
faceCascade = cv2.CascadeClassifier("./cascade_classifier/haarcascade_frontalface_default.xml")

# 先读取训练集的图像 这里只用了三张图像，每个人只对应一张图。实际应用时可以为每个人收集多张对应同一标签的图像，以提高准确率。
img1 = cv2.imread("./images/p1.jpg", 0)
img2 = cv2.imread("./images/p2.jpg", 0)
img3 = cv2.imread("./images/p3.jpg", 0)
# 以600*600为基准，将图像也都调整为该大小。无论是训练集还是测试集，图像的尺寸大小都必须保持一致才行。这一步不能忽略。
img1 = cv2.resize(img1, (600, 600))
img2 = cv2.resize(img2, (600, 600))
img3 = cv2.resize(img3, (600, 600))

# 将样本图像和标签依次存储进列表中
photos = list()
lables = list()
photos.append(img1)
lables.append(0)
photos.append(img2)
lables.append(1)
photos.append(img3)
lables.append(2)
# 用字典匹配每个人的名字和上边设定的标签，而上边先使用序号作为人与人之间的标识，这样做的好处是避免了重名带来的影响。
names = {"0": "Allen", "1": "Tom", "2": "Lucy"}

# 三种识别器任选其一即可，其区别在于对应的算法逻辑不同
# 创建特征脸识别器
# recognizer = cv2.face.EigenFaceRecognizer_create()
# 创建线性判别分析识别器
# recognizer = cv2.face.FisherFaceRecognizer_create()
# 创建 LBPH人脸识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 识别器开始训练
recognizer.train(photos, np.array(lables))

# 读取测试集图像 这里为了方便展示，还使用了训练集中的p2进行测试。大家调试时可以用训练集中同一人物的不同图片进行调试。
img = cv2.imread("./images/p2.jpg", 0)
# 调整为一致的大小600*600 这一点必须不能忽略
img = cv2.resize(img, (600, 600))
# 开始识别
label, confidence = recognizer.predict(img)
# 打印识别结果
print("confidence = " + str(confidence))
print("识别结果:", names[str(label)])
