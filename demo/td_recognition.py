# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'td_recognition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!



import argparse
import cv2
import time
from maskrcnn_benchmark.config import cfg
from predictor import COCODemo

import time

import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5 import QtCore
from PyQt5.Qt import *
stringdic=[
        'i10', 'i2', 'i4', 'i5', 'il100', 'il60', 'il80', 'il90', 'io', 'ip', 'p1', 'p10', 'p11', 'p12', 'p14', 'p18',
         'p19', 'p22', 'p23', 'p25', 'p26', 'p27', 'p3', 'p5', 'p6', 'p9', 'pa14', 'pb', 'pg', 'ph4', 'ph4.5', 'ph5',
         'pl100', 'pl120', 'pl15', 'pl20', 'pl30', 'pl40', 'pl5', 'pl50', 'pl60', 'pl70', 'pl80', 'pl90', 'pm20',
         'pm30', 'pm55', 'pn', 'pne', 'po', 'pr40', 'w13', 'w30', 'w32', 'w55', 'w57', 'w58', 'w59', 'w63', 'wo'
    ]
dict = { 'i10': 0, 'i2': 0, 'i4': 0, 'i5': 0, 'il100': 0, 'il60': 0, 'il80': 0, 'il90': 0, 'io': 0, 'ip': 0, 'p1': 0, 'p10': 0, 'p11': 0, 'p12': 0, 'p14': 0, 'p18': 0,
         'p19': 0, 'p22': 0, 'p23': 0, 'p25': 0, 'p26': 0, 'p27': 0, 'p3': 0, 'p5': 0, 'p6': 0, 'p9': 0, 'pa14': 0, 'pb': 0, 'pg': 0, 'ph4': 0, 'ph4.5': 0, 'ph5': 0,
         'pl100': 0, 'pl120': 0, 'pl15': 0, 'pl20': 0, 'pl30': 0, 'pl40': 0, 'pl5': 0, 'pl50': 0, 'pl60': 0, 'pl70': 0, 'pl80': 0, 'pl90': 0, 'pm20': 0,
         'pm30': 0, 'pm55': 0, 'pn': 0, 'pne': 0, 'po': 0, 'pr40': 0, 'w13': 0, 'w30': 0, 'w32': 0, 'w55': 0, 'w57': 0, 'w58': 0, 'w59': 0, 'w63': 0, 'wo': 0}
def main(filepath):
    for strr in stringdic:
        dict[strr]=0

    parser = argparse.ArgumentParser(description="PyTorch Object Detection Webcam Demo")
    parser.add_argument(
        "--config-file",
        default="../configs/caffe2/e2e_mask_rcnn_R_50_FPN_1x_caffe2.yaml",
        metavar="FILE",
        help="path to config file",
    )
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.7,
        help="Minimum score for the prediction to be shown",
    )
    parser.add_argument(
        "--min-image-size",
        type=int,
        default=1024,
        help="Smallest size of the image to feed to the model. "
            "Model was trained with 800, which gives best results",
    )
    parser.add_argument(
        "--show-mask-heatmaps",
        dest="show_mask_heatmaps",
        help="Show a heatmap probability for the top masks-per-dim masks",
        action="store_true",
    )
    parser.add_argument(
        "--masks-per-dim",
        type=int,
        default=2,
        help="Number of heatmaps per dimension to show",
    )
    parser.add_argument(
        "opts",
        help="Modify model config options using the command-line",
        default=None,
        nargs=argparse.REMAINDER,
    )

    args = parser.parse_args()

    # load config from file and command-line arguments
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()

    # prepare object that handles inference plus adds predictions on top of image
    coco_demo = COCODemo(
        cfg,
        confidence_threshold=args.confidence_threshold,
        show_mask_heatmaps=args.show_mask_heatmaps,
        masks_per_dim=args.masks_per_dim,
        min_image_size=args.min_image_size,
    )
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    boxes, scores, labels,composite = coco_demo.run_on_opencv_image(img)
    for box, score, label in zip(boxes, scores, labels):
        dict[label]=dict[label]+1
    cv2.imwrite('/home/smile/fsdownload/MPSR/1.jpg',composite)


def is_img(ext):
    if ext.endswith(".jpg") or  ext.endswith(".png") or  ext.endswith(".jpeg") or  ext.endswith(".bmp"):
        return True
    else:
        return False



class Ui_MainWindow(object):
   def setupUi(self, MainWindow):
        self.pngname=""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImgLabel.setGeometry(QtCore.QRect(299, 9, 600, 601))
        self.ImgLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ImgLabel.setText("")
        self.ImgLabel.setObjectName("ImgLabel")

        self.StartButton_5 = QtWidgets.QPushButton(self.centralwidget)

        self.StartButton_5.setGeometry(QtCore.QRect(70, 590, 151, 31))
        _translate = QtCore.QCoreApplication.translate
        self.StartButton_5.setText(_translate("MainWindow", "查看图片"))
        self.StartButton_5.setVisible(False)
        self.StartButton_5.setObjectName("StartButton_5")
        self.StartButton_5.clicked.connect(self.newwinshow)


        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(910, 20, 280, 461))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";")
        self.ResultLabel.setText("")


        self.ResultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ResultLabel.setWordWrap(True)
        self.ResultLabel.setObjectName("ResultLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(910, 470, 280, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.StartButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton_3.setGeometry(QtCore.QRect(980, 580, 151, 31))
        self.StartButton_3.setObjectName("StartButton_3")
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(170, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        #self.pushButton.setFont(font)
        #self.pushButton.setObjectName("pushButton")

        self.model01 = QFileSystemModel()
        # 进行筛选只显示文件夹，不显示文件和特色文件
        self.model01.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
        self.model01.setRootPath('')

        self.treeView1 = QtWidgets.QTreeView(self.centralwidget)

        self.treeView1.setModel(self.model01)
        for col in range(1, 4):
            self.treeView1.setColumnHidden(col, True)
        self.treeView1.doubleClicked.connect(self.initUI)


        self.treeView1.setGeometry(QtCore.QRect(0, 20, 291, 280))
        self.treeView1.setObjectName("treeView")

        self.model02 = QStandardItemModel()
        self.treeView2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView2.setModel(self.model02)
        self.treeView2.clicked.connect(self.initUI2)

        # 将创建的窗口进行添加
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.treeView1)
        self.layout.addWidget(self.treeView2)


        self.treeView2.setGeometry(QtCore.QRect(0, 320, 291, 270))
        self.treeView2.setObjectName("treeView2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


   def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小样本交通目标检测系统"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">待检测</span></p></body></html>"))
        self.StartButton_3.setText(_translate("MainWindow", "开始识别"))
        self.StartButton_3.clicked.connect(self.get_selected)
        #self.pushButton.setText(_translate("MainWindow", "ok"))
        #self.pushButton.clicked.connect(self.get_selected)



   def get_selected(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">开始识别</span></p></body></html>"))
        time.sleep(1)
        main(self.imagepath)

        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">识别完成</span></p></body></html>"))
        result_str=''
        for aa in stringdic:
            if dict[aa]!=0:
                result_str+="ID: "+aa+" 数量: "+str(dict[aa])
                result_str+='\n'
        #jpg = QtGui.QPixmap('/home/smile/fsdownload/MPSR/1.jpg')
        self.imagepath='/home/smile/fsdownload/MPSR/1.jpg'
        self.image = QtGui.QPixmap(self.imagepath)
        self.ResultLabel.setText(result_str)
        self.ImgLabel.setScaledContents(True)
        self.ImgLabel.setPixmap(self.image)
        self.StartButton_5.setVisible(True)
        self.newWin = NewWindow()
   def newwinshow(self):
       self.newWin.show()
   def initUI2(self,index):
        PathDataName = self.model02.invisibleRootItem()
        row,col = index.row(), index.column()
        self.imagepath=self.pngname+"/"+PathDataName.child(row,col).text()
        print(self.pngname+"/"+PathDataName.child(row,col).text())
        #jpg = QtGui.QPixmap(self.pngname+"/"+PathDataName.child(row,col).text())
        self.image=QtGui.QPixmap(self.pngname+"/"+PathDataName.child(row,col).text())
        self.ImgLabel.setScaledContents(True)
        self.ImgLabel.setPixmap(self.image)

   def initUI(self, Qmodelidx):
            # 每次点击清空右边窗口数据
            self.model02.clear()
            # 定义一个数组存储路径下的所有文件
            PathData = []
            # 获取双击后的指定路径
            filePath = self.model01.filePath(Qmodelidx)
            #print(self.pngname)
            # List窗口文件赋值
            PathDataName = self.model02.invisibleRootItem()
            # 拿到文件夹下的所有文件
            PathDataSet = os.listdir(filePath)
            # 进行将拿到的数据进行排序
            PathDataSet.sort()
            # 遍历判断拿到的文件是文件夹还是文件，Flase为文件，True为文件夹
            for Data in range(len(PathDataSet)):
                if os.path.isdir(filePath + '\\' + PathDataSet[Data]) == False:
                    PathData.append(PathDataSet[Data])
                    self.pngname=filePath
                #elif os.path.isdir(filePath + '\\' + PathDataSet[Data]) == True:
                    #print('2')
            # 将拿到的所有文件放到数组中进行右边窗口赋值。
            for got in range(len(PathData)):
                if is_img(PathData[got]):
                   gosData = QStandardItem(PathData[got])
                   PathDataName.setChild(got, gosData)


class NewWindow(QMainWindow):
 def __init__(self):
    super().__init__()
    f = QFont("ZYSong18030", 12)
    self.setFont(f)

    self.setWindowTitle("Image Processor")
    self.imageLabel = QLabel()
    self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    self.imageLabel.setScaledContents(True)

    self.setCentralWidget(self.imageLabel)
    self.image = QImage()
    if self.image.load("/home/smile/fsdownload/MPSR/1.jpg"):
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
        self.resize(self.image.width(), self.image.height())

    self.createActions()
    self.createMenus()
    self.createToolBars()


 def createActions(self):
    self.zoomInAction = QtWidgets.QAction(QIcon("image/fangda.gif"),
                                          self.tr("放大"), self)  # 不是QAction(QIcon, QString, QObject)
    self.zoomInAction.setShortcut("Ctrl+I")  # 设置快捷键
    self.zoomInAction.setStatusTip(self.tr("放大"))  # 设置标题栏
    #        self.connect(self.zoomInAction,SIGNAL("triggered()"),
    #                     self.slotZoomin)                              # PyQt4
    self.zoomInAction.triggered.connect(self.slotZoomIn)  # PyQt5

    self.zoomOutAction = QtWidgets.QAction(QIcon("image/suoxiao.gif"),
                                           self.tr("缩小"), self)  # 不是QAction(QIcon, QString, QObject)
    self.zoomOutAction.setShortcut("Ctrl+O")  # 设置快捷键
    self.zoomOutAction.setStatusTip(self.tr("缩小"))  # 设置标题栏
    #        self.connect(self.zoomOutAction,SIGNAL("triggered()"),
    #                     self.slotZoomOut)                              # PyQt4
    self.zoomOutAction.triggered.connect(self.slotZoomOut)  # PyQt5

    self.rotateAction = QtWidgets.QAction(QIcon("image/sun.gif"),
                                          self.tr("顺旋"), self)  # 不是QAction(QIcon, QString, QObject)
    self.rotateAction.setShortcut("Ctrl+R")  # 设置快捷键
    self.rotateAction.setStatusTip(self.tr("顺旋"))  # 设置标题栏
    #        self.connect(self.rotateAction,SIGNAL("triggered()"),
    #                     self.slotRotate)                               # PyQt4
    self.rotateAction.triggered.connect(self.slotRotate)  # PyQt5

    self.rotateAntiAction = QtWidgets.QAction(QIcon("image/ni.gif"),
                                              self.tr("逆旋"), self)  # 不是QAction(QIcon, QString, QObject)
    self.rotateAntiAction.setShortcut("Ctrl+E")  # 设置快捷键
    self.rotateAntiAction.setStatusTip(self.tr("逆旋"))  # 设置标题栏
    #        self.connect(self.rotateAntiAction,SIGNAL("triggered()"),
    #                     self.slotRotateAnti)                           # PyQt4
    self.rotateAntiAction.triggered.connect(self.slotRotateAnti)  # PyQt5


 '''创建菜单栏'''


 def createMenus(self):
    zoomMenu = self.menuBar().addMenu(self.tr("缩放"))  # 缩放菜单选项
    zoomMenu.addAction(self.zoomInAction)  # 放大子选项
    zoomMenu.addAction(self.zoomOutAction)  # 缩小子选项
    rotateMenu = self.menuBar().addMenu(self.tr("旋转"))  # 旋转菜单选项
    rotateMenu.addAction(self.rotateAction)  # 顺旋子选项
    rotateMenu.addAction(self.rotateAntiAction)  # 逆旋子选项


 '''创建工具栏'''


 def createToolBars(self):
    fileToolBar = self.addToolBar("Print")
    fileToolBar.addAction(self.zoomInAction)
    fileToolBar.addAction(self.zoomOutAction)
    fileToolBar.addAction(self.rotateAntiAction)
    fileToolBar.addAction(self.rotateAction)


 '''图片放大(倍数可设)'''


 def slotZoomIn(self):
    if self.image.isNull():  # 没图片,则不执行任何操作
        return
    #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
    transform = QTransform()  # PyQt5
    #        martix.scale(2,2)        # PyQt4,PyQt5中已废弃
    transform.scale(1.2, 1.2)  # PyQt5
    self.image = self.image.transformed(transform);  # 相应的matrix改为transform
    self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
    self.resize(self.image.width(), self.image.height())


 '''图片缩小(倍数可设)'''


 def slotZoomOut(self):
    if self.image.isNull():  # 没图片,则不执行任何操作
        return
    #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
    transform = QTransform()  # PyQt5
    #        martix.scale(2,2)        # PyQt4,PyQt5中已废弃
    transform.scale(0.8, 0.8)  # PyQt5
    self.image = self.image.transformed(transform);  # 相应的matrix改为transform
    self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
    self.resize(self.image.width(), self.image.height())


 '''图片顺旋(角度可设)'''


 def slotRotate(self):
    if self.image.isNull():  # 没图片,则不执行任何操作
        return
    #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
    transform = QTransform()  # PyQt5
    #        martix.rotate(90)        # PyQt4,PyQt5中已废弃
    transform.rotate(90)  # PyQt5
    self.image = self.image.transformed(transform);  # 相应的matrix改为transform
    self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
    self.resize(self.image.width(), self.image.height())


 '''图片逆旋(角度可设)'''


 def slotRotateAnti(self):
    if self.image.isNull():  # 没图片,则不执行任何操作
        return
    #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
    transform = QTransform()  # PyQt5
    #        martix.rotate(90)        # PyQt4,PyQt5中已废弃
    transform.rotate(-90)  # PyQt5
    self.image = self.image.transformed(transform);  # 相应的matrix改为transform
    self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
    self.resize(self.image.width(), self.image.height())







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())