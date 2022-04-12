# -*- coding: utf-8 -*-

import numpy as np
import cv2
import cv2 as cv
import os
import shutil
from PIL import Image


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QFileDialog


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(550, 280))
        MainWindow.setMaximumSize(QtCore.QSize(550, 280))
        MainWindow.setMouseTracking(True)

        # 窗口樣式
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #  檢測按鈕定義
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 165, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #  退出按鈕定義
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 160, 165, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        #  清空目录按鈕定義
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 220, 165, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        #  关于按鈕定義
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 220, 165, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        
        

        # width label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 25, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # high label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 75, 65, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 版本號label
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(420,230, 90, 45))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.label_3.setFont(font)
        # self.label_3.setObjectName("label_3")

        # 宽度 路徑框
        # self.lineEdit = FileEdit(self.centralwidget)
        self.lineEdit = QLineEdit(self.centralwidget)

        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 415, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('输入宽度')
        self.lineEdit.setText('1920')

        # 高度 路徑框
        # self.lineEdit_2 = FileEdit(self.centralwidget)
        self.lineEdit_2 = QLineEdit(self.centralwidget)


        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 415, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('输入高度')


        #  定義按鈕單擊事件
        self.pushButton.clicked.connect(self.Convert_To_Png_AndCut)
        self.pushButton_2.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.remove_file)
        self.pushButton_4.clicked.connect(self.msg_about)



        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #  UI 名稱
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image_Resize"))

        self.pushButton.setText(_translate("MainWindow", "Conversion"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "About"))
        self.label.setText(_translate("MainWindow", "Width:"))
        self.label_2.setText(_translate("MainWindow", "High:"))
        # self.label_3.setText(_translate("MainWindow", "  version:0.1"))


    # 结果弹窗
    def msg_about_y(self):
        QMessageBox.about(QtWidgets.QWidget(),"提示", "分割完成，图片已保存至 RS_Cut_Result")

    # 关于面板
    def msg_about(self):
        QMessageBox.about(QtWidgets.QWidget(), "关于",
                          "使用方法：\n"
                          "· 将需裁剪的tiff图像放到RS_TiffDir文件夹下（没有则需要新建）;\n"
                          "· 设置裁切的宽度和高度;\n"
                          "· 点击Conversion进行图像裁切;\n"
                          "· 裁切完后若需要再次裁切，需要拷贝裁切后的图像之后点击 Clear按钮;\n"
                          "\n"
                          "\n"
                          "注意事项：\n"
                          "· RS_TiffDir文件夹需要放到和本程序同级目录之下;\n"
                          "· 存放路径最好是全英文路径，避免运行时出错;\n"
                          "· 运行后会自动生成 RS_TiffDir_Cut 和 RS_Cut_Resul文件夹:\n"
                          "     - RS_TiffDir_Cut 文件夹下会生成tiff裁切图;\n"
                          "     - RS_Cut_Resul 文件夹下会生成最终png裁切图;\n"
                          )

    # 错误弹窗
    def msg_faild(self):
        QMessageBox.critical(QtWidgets.QWidget(), "错误", "好像没有输入宽度或高度呢~", QMessageBox.Yes)





    # 清空目录
    def remove_file(self):
        shutil.rmtree('./RS_Cut_Result/')
        os.mkdir('./RS_Cut_Result/')

        shutil.rmtree('./RS_TiffDir_Cut/')
        os.mkdir('./RS_TiffDir_Cut/')

    # 转换拼接逻辑
    def Convert_To_Png_AndCut(self):

        if not self.lineEdit.text() or not self.lineEdit_2.text():
            self.msg_faild()

        elif self.lineEdit.text() or self.lineEdit_2.text():

            dir = r'./RS_TiffDir/'
            print(dir,'文件夹读取成功')

            files = os.listdir(dir)
            print(files,'文件读取成功')

            # ResultPath2 = 'O:\\Dropbox\\Python_Project\\src\\project\\Image_Resize\\RS_TiffDir_Cut\\'  # 定义裁剪后的保存路径
            # ResultPath3 = 'O:\\Dropbox\\Python_Project\\src\\project\\Image_Resize\\RS_Cut_Result\\'  # 定义裁剪后的保存路径

            ResultPath2 = './RS_TiffDir_Cut/'  # 定义裁剪后的保存路径
            if not os.path.exists(ResultPath2):
                os.makedirs(ResultPath2)
            ResultPath3 = './RS_Cut_Result/'  # 定义裁剪后的保存路径
            if not os.path.exists(ResultPath3):
                os.makedirs(ResultPath3)

            for file in files:  # 遍历所有文件
                a, b = os.path.splitext(file)  # 拆分影像图的文件名称
                this_dir = os.path.join(dir + file)  # 构建保存 路径+文件名

                print(this_dir,'文件建构成功')

                # img = cv2.imread(this_dir, -1)  # 读取tiff影像
                img = cv2.imdecode(np.fromfile(this_dir, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

                # 第二个参数是通道数和位深的参数，
                # IMREAD_UNCHANGED = -1  # 不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
                # IMREAD_GRAYSCALE = 0  # 进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
                # IMREAD_COLOR = 1   # 进行转化为RGB三通道图像，图像深度转为8位
                # IMREAD_ANYDEPTH = 2  # 保持图像深度不变，进行转化为灰度图。
                # IMREAD_ANYCOLOR = 4  # 若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位


                #  ------------    裁切      ----------------

                hight = img.shape[0]  # opencv写法，获取宽和高
                width = img.shape[1]
                # 定义裁剪尺寸
                self.lineEdit_var = self.lineEdit.text()
                self.lineEdit_2_var = self.lineEdit_2.text()

                print(self.lineEdit_var,'宽度读取成功')
                print(self.lineEdit_2_var,'高度读取成功')


                w = int(self.lineEdit_var)  # 宽度
                h = int(self.lineEdit_2_var)  # 高度
                _id = 1  # 裁剪结果保存文件名：0 - N 升序方式
                i = 0

                num = 0
                tmp = True
                while tmp:
                    if (i + h <= hight):  # 控制高度,图像多余固定尺寸总和部分不要了
                        j = 0
                        while (j + w <= width):  # 控制宽度，图像多余固定尺寸总和部分不要了
                            cropped = img[i:i + h, 0:width]  # 裁剪坐标为[y0:y1, x0:x1]

                            # cropped = img[i:i + h, j:j + w]  #宽度、高度都不确定时
                            # cv.imwrite(ResultPath2 + a + "_" + str(_id) + b, cropped)
                            cv2.imencode(str(_id) + b, cropped)[1].tofile(
                                ResultPath2 + a + "_" + str(_id) + b)  # 保存为tiff格式 - 分段 ，中文
                            _id += 1
                            num += 1
                            j += w
                        i = i + h

                    if (hight - i) < h:
                        cropped_c = img[num * h:hight, 0:width]
                        cv2.imencode(str(_id) + b, cropped_c)[1].tofile(ResultPath2 + a + "_" + str(_id) + b)

                        # 创建空白图像
                        ResultPath_tmp = './temp/'  # 定义裁剪后的保存路径
                        if not os.path.exists(ResultPath_tmp):
                            os.makedirs(ResultPath_tmp)
                        print('创建缓存文件夹')

                        print('累积高度', i)
                        print('计数器2#', num)
                        print('剩余高度',hight - i * num)
                        print('补全高度',h - (hight - i * num))

                        img_extend = Image.new('RGBA', (width, h - (hight - h * num)), color=0)
                        # img.show()
                        img_extend.save('./temp/temp.png')  # 保存到缓存

                        tmp = False

                path = ResultPath2

            # 計數器  用來彈窗判斷
            num_files = 0
            for fn in os.listdir(path):
                num_files += 1
            print('计数器：',num_files)


            #  -------------转换逻辑

            files_cut_tiff = os.listdir(ResultPath2)

            numm = 1
            for file_cut in files_cut_tiff:
                m, n = os.path.splitext(file_cut)
                re_dir = os.path.join(ResultPath2 + file_cut)

                # img_cut = cv.imread(re_dir, 1)
                img_cut = cv2.imdecode(np.fromfile(re_dir, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

                if (img_cut is None) == False:
                    print(f'第{numm}个转换 ok')
                    numm += 1
                    # cv.imwrite(ResultPath3 + m + "_" + ".png", img_cut)  # 保存为png格式
                    cv2.imencode('.png', img_cut)[1].tofile(ResultPath3 + m + ".png")  # 保存为png格式 中文

                    num_files -= 1
                    if num_files == 0:
                        self.msg_about_y()

                else:
                    print('null')
                    break



            # 图像拼接逻辑
            mm = ResultPath3 + m + ".png"
            print('读取图像', mm)

            img1 = cv2.imdecode(np.fromfile(mm, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            img2 = cv2.imdecode(np.fromfile('./temp/temp.png', dtype=np.uint8), cv2.IMREAD_UNCHANGED)

            image = cv2.vconcat([img1, img2])
            print('图像拼接完成')


            # gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2ACES)
            # gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2ACES)
            # ====使用numpy的数组矩阵合并concatenate======

            # image = np.concatenate((gray1, gray2))
            # 纵向连接 image = np.vstack((gray1, gray2))
            # 横向连接 image = np.concatenate([gray1, gray2], axis=1)
            # image = np.array(df) # dataframe to ndarray

            # =============

            # filepahe = ResultPath2 + a + "_" + str(_id) + b

            # cv2.imshow('image', image)
            # cv2.imwrite(filepahe, image)  #只限英文  中文名报错
            cv2.imencode('.png', image)[1].tofile(ResultPath3 + m + ".png")
            print('图像存储完成')
            shutil.rmtree('./temp')
            print('缓存目录已删除')
            print('完成')



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
