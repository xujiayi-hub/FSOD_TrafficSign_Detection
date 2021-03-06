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
from picturelabel import window
import time

import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5 import QtCore
from PyQt5.Qt import *

piclabel = 1
stringdic = [
    'i10', 'i2', 'i4', 'i5', 'il100', 'il60', 'il80', 'il90', 'io', 'ip', 'p1', 'p10', 'p11', 'p12', 'p14', 'p18',
    'p19', 'p22', 'p23', 'p25', 'p26', 'p27', 'p3', 'p5', 'p6', 'p9', 'pa14', 'pb', 'pg', 'ph4', 'ph4.5', 'ph5',
    'pl100', 'pl120', 'pl15', 'pl20', 'pl30', 'pl40', 'pl5', 'pl50', 'pl60', 'pl70', 'pl80', 'pl90', 'pm20',
    'pm30', 'pm55', 'pn', 'pne', 'po', 'pr40', 'w13', 'w30', 'w32', 'w55', 'w57', 'w58', 'w59', 'w63', 'wo'
]
dict = {'i10': 0, 'i2': 0, 'i4': 0, 'i5': 0, 'il100': 0, 'il60': 0, 'il80': 0, 'il90': 0, 'io': 0, 'ip': 0, 'p1': 0,
        'p10': 0, 'p11': 0, 'p12': 0, 'p14': 0, 'p18': 0,
        'p19': 0, 'p22': 0, 'p23': 0, 'p25': 0, 'p26': 0, 'p27': 0, 'p3': 0, 'p5': 0, 'p6': 0, 'p9': 0, 'pa14': 0,
        'pb': 0, 'pg': 0, 'ph4': 0, 'ph4.5': 0, 'ph5': 0,
        'pl100': 0, 'pl120': 0, 'pl15': 0, 'pl20': 0, 'pl30': 0, 'pl40': 0, 'pl5': 0, 'pl50': 0, 'pl60': 0, 'pl70': 0,
        'pl80': 0, 'pl90': 0, 'pm20': 0,
        'pm30': 0, 'pm55': 0, 'pn': 0, 'pne': 0, 'po': 0, 'pr40': 0, 'w13': 0, 'w30': 0, 'w32': 0, 'w55': 0, 'w57': 0,
        'w58': 0, 'w59': 0, 'w63': 0, 'wo': 0}
def main_():
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
        default=224,
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
    cam = cv2.VideoCapture(0)
    while (1):
        start_time = time.time()
        ret_val, img = cam.read()
        oxes, scores, labels,result = coco_demo.run_on_opencv_image(img)
        print("Time: {:.2f} s / img".format(time.time() - start_time))
        cv2.imshow('COCO detections', result)
        k = cv2.waitKey(1)
        if not cv2.getWindowProperty('COCO detections', cv2.WND_PROP_VISIBLE):
            break
        if k == 27:  # Key code for ESC
            break

            #    break
    cv2.destroyAllWindows()

def main(filepath, model, picturename):
    for strr in stringdic:
        dict[strr] = 0

    parser = argparse.ArgumentParser(description="PyTorch Object Detection Webcam Demo")
    if model == 0:
        print(model)
        parser.add_argument(
            "--config-file",
            default="../configs/caffe2/e2e_mask_rcnn_R_50_FPN_1x_caffe2.yaml",
            metavar="FILE",
            help="path to config file",
        )
    elif model == 1:
        print(model)
        parser.add_argument(
            "--config-file",
            default="../configs/caffe2/e2e_mask_rcnn_R_50_FPN_1x_caffe2_.yaml",
            metavar="FILE",
            help="path to config file",
        )
    elif model == 2:
        print(model)
        parser.add_argument(
            "--config-file",
            default="../configs/caffe2/e2e_mask_rcnn_R_50_FPN_1x_caffe2_3.yaml",
            metavar="FILE",
            help="path to config file",
        )
    else:
        print(model)
        parser.add_argument(
            "--config-file",
            default="../configs/caffe2/e2e_mask_rcnn_R_50_FPN_1x_caffe2_4.yaml",
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
    boxes, scores, labels, composite = coco_demo.run_on_opencv_image(img)
    for box, score, label in zip(boxes, scores, labels):
        dict[label] = dict[label] + 1
    cv2.imwrite('/home/smile/fsdownload/MPSR/' + picturename + '.jpg', composite)


def is_img(ext):
    if ext.endswith(".jpg") or ext.endswith(".png") or ext.endswith(".jpeg") or ext.endswith(".bmp"):
        return True
    else:
        return False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.moxing = 0
        self.pngname = ""
        self.picturename = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImgLabel.setGeometry(QtCore.QRect(299, 9, 600, 701))
        self.ImgLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ImgLabel.setText("")
        self.ImgLabel.setObjectName("ImgLabel")
        self.labellist_ = []
        self.labellist_text_ = []
        self.StartButton_5 = QtWidgets.QPushButton(self.centralwidget)

        self.StartButton_5.setGeometry(QtCore.QRect(70, 610, 151, 25))
        _translate = QtCore.QCoreApplication.translate
        self.StartButton_5.setText(_translate("MainWindow", "????????????"))
        self.StartButton_5.setVisible(False)
        self.StartButton_5.setObjectName("StartButton_5")
        self.StartButton_5.clicked.connect(self.newwinshow)

        self.ResultLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel1.setGeometry(QtCore.QRect(910, 20, 100, 90))
        self.ResultLabel1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 9pt \"Arial\";")
        self.labellist_.append(self.ResultLabel1)

        self.ResultLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel2.setGeometry(QtCore.QRect(910, 110, 100, 90))
        self.ResultLabel2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 9pt \"Arial\";")
        self.labellist_.append(self.ResultLabel2)

        self.ResultLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel3.setGeometry(QtCore.QRect(910, 200, 100, 90))
        self.ResultLabel3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 9pt \"Arial\";")
        self.labellist_.append(self.ResultLabel3)

        self.ResultLabel4 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel4.setGeometry(QtCore.QRect(910, 290, 100, 90))
        self.ResultLabel4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 9pt \"Arial\";")
        self.labellist_.append(self.ResultLabel4)

        self.ResultLabel5 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel5.setGeometry(QtCore.QRect(910, 380, 100, 90))
        self.ResultLabel5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 9pt \"Arial\";")
        self.labellist_.append(self.ResultLabel5)
        self.ResultLabel1_1 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel1_1.setGeometry(QtCore.QRect(1010, 20, 180, 90))
        self.ResultLabel1_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"Arial\";")
        self.labellist_text_.append(self.ResultLabel1_1)

        self.ResultLabel2_2 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel2_2.setGeometry(QtCore.QRect(1010, 110, 180, 90))
        self.ResultLabel2_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"Arial\";")
        self.labellist_text_.append(self.ResultLabel2_2)

        self.ResultLabel3_3 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel3_3.setGeometry(QtCore.QRect(1010, 200, 180, 90))
        self.ResultLabel3_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"Arial\";")
        self.labellist_text_.append(self.ResultLabel3_3)
        self.ResultLabel4_4 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel4_4.setGeometry(QtCore.QRect(1010, 290, 180, 90))
        self.ResultLabel4_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"Arial\";")
        self.labellist_text_.append(self.ResultLabel4_4)
        self.ResultLabel5_5 = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel5_5.setGeometry(QtCore.QRect(1010, 380, 180, 90))
        self.ResultLabel5_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"Arial\";")
        self.labellist_text_.append(self.ResultLabel5_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        for aa in self.labellist_text_:
            font = QtGui.QFont()
            font.setFamily("Arial")  # ???????????????????????????????????????????????????
            font.setPointSize(18)  # ????????????????????????????????????????????????????????????
            aa.setFont(font)

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

        self.StartButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton_6.setGeometry(QtCore.QRect(980, 620, 151, 31))
        self.StartButton_6.setObjectName("StartButton_6")
        self.StartButton_6.clicked.connect(self.newwinshow_1)

        self.StartButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton_7.setGeometry(QtCore.QRect(980, 665, 151, 25))
        self.StartButton_7.setObjectName("StartButton_7")
        self.StartButton_7.clicked.connect(main_)
        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(20, 650, 70, 31))
        self.label_model.setText("???????????????")
        self.label_model.setObjectName("ImgLabel")

        self.cb = QComboBox(self.centralwidget)
        self.cb.move(95, 650)
        self.cb.addItem('model_10_shot')
        self.cb.addItem('model_30_shot')
        self.cb.addItem('model_10_shot(2)')
        self.cb.addItem('model_30_shot(2)')

        self.cb.currentIndexChanged[int].connect(self.print_value)

        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(170, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        # self.pushButton.setFont(font)
        # self.pushButton.setObjectName("pushButton")

        self.model01 = QFileSystemModel()
        # ???????????????????????????????????????????????????????????????
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

        # ??????????????????????????????
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

        self.my = window()
        filename = []
        self.my.slot_open_image(filename)



    def print_value(self, i):
        self.moxing = i

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????????????????????"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">?????????</span></p></body></html>"))
        self.StartButton_3.setText(_translate("MainWindow", "????????????"))
        self.StartButton_3.clicked.connect(self.get_selected)

        self.StartButton_6.setText(_translate("MainWindow", "????????????????????????"))
        self.StartButton_7.setText(_translate("MainWindow", "???????????????"))
        self.StartButton_6.clicked.connect(self.newwinshow_1)

    def get_selected(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">????????????</span></p></body></html>"))
        main(self.imagepath, self.moxing, self.picturename + str(self.moxing))

        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">????????????</span></p></body></html>"))
        result_str = ''
        filename = []
        for aa in stringdic:
            if dict[aa] != 0:
                result_str += aa + "," + str(dict[aa])
                result_str += '\n'
                filename.append(aa)
        # jpg = QtGui.QPixmap('/home/smile/fsdownload/MPSR/1.jpg')
        self.imagepath = '/home/smile/fsdownload/MPSR/' + self.picturename + str(self.moxing) + '.jpg'
        self.image = QtGui.QPixmap(self.imagepath)
        # self.ResultLabel1.setText(result_str)
        self.ImgLabel.setScaledContents(True)
        self.ImgLabel.setPixmap(self.image)
        self.StartButton_5.setVisible(True)
        global piclabel
        piclabel = self.imagepath
        self.newWin = Main()
        filename_ = '/home/smile/fsdownload/ToJIA'
        self.my.slot_open_image(filename)
        result_strr = result_str.splitlines()
        _translate = QtCore.QCoreApplication.translate
        shu_ = 0
        for aa in result_strr:
            aaa = aa.split(',')
            jpg = QtGui.QPixmap(filename_ + '/' + aaa[0]).scaled(100, 90)
            self.labellist_[shu_].setPixmap(jpg)
            self.labellist_text_[shu_].setText(_translate("Form", "  ??  " + aaa[1]))
            shu_ = shu_ + 1

    def newwinshow(self):
        self.newWin.show()

    def newwinshow_1(self):
        self.my.show()

    def initUI2(self, index):
        PathDataName = self.model02.invisibleRootItem()
        row, col = index.row(), index.column()
        self.imagepath = self.pngname + "/" + PathDataName.child(row, col).text()
        print(self.pngname + "/" + PathDataName.child(row, col).text())
        # jpg = QtGui.QPixmap(self.pngname+"/"+PathDataName.child(row,col).text())
        self.image = QtGui.QPixmap(self.pngname + "/" + PathDataName.child(row, col).text())
        self.picturename = PathDataName.child(row, col).text()
        self.ImgLabel.setScaledContents(True)
        self.ImgLabel.setPixmap(self.image)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">?????????</span></p></body></html>"))
        self.StartButton_5.setVisible(False)

    def initUI(self, Qmodelidx):
        # ????????????????????????????????????
        self.model02.clear()
        # ????????????????????????????????????????????????
        PathData = []
        # ??????????????????????????????
        filePath = self.model01.filePath(Qmodelidx)
        # print(self.pngname)
        # List??????????????????
        PathDataName = self.model02.invisibleRootItem()
        # ?????????????????????????????????
        PathDataSet = os.listdir(filePath)
        # ????????????????????????????????????
        PathDataSet.sort()
        # ??????????????????????????????????????????????????????Flase????????????True????????????
        for Data in range(len(PathDataSet)):
            if os.path.isdir(filePath + '\\' + PathDataSet[Data]) == False:
                PathData.append(PathDataSet[Data])
                self.pngname = filePath
            # elif os.path.isdir(filePath + '\\' + PathDataSet[Data]) == True:
            # print('2')
        # ??????????????????????????????????????????????????????????????????
        jishu = 0
        for got in range(len(PathData)):
            if is_img(PathData[got]):
                print(PathData[got])
                print(got)
                gosData = QStandardItem(PathData[got])
                PathDataName.setChild(jishu, gosData)
                jishu = jishu + 1


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = ImageWithMouseControl(self)
        self.widget.setGeometry(10, 10, 1600, 900)
        self.setWindowTitle('Image with mouse control')


class ImageWithMouseControl(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.img = QPixmap(piclabel)
        self.scaled_img = self.img.scaled(self.size())
        self.point = QPoint(0, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('????????????')

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.draw_img(painter)
        painter.end()

    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scaled_img)

    def mouseMoveEvent(self, e):  # ??????????????????
        if self.left_click:
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
        elif e.button() == Qt.RightButton:
            self.point = QPoint(0, 0)
            self.scaled_img = self.img.scaled(self.size())
            self.repaint()

    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            # ????????????
            self.scaled_img = self.img.scaled(self.scaled_img.width() - 50, self.scaled_img.height() - 50)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 50)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 50)
            self.point = QPoint(new_w, new_h)
            self.repaint()
        elif e.angleDelta().y() < 0:
            # ????????????
            self.scaled_img = self.img.scaled(self.scaled_img.width() + 50, self.scaled_img.height() + 50)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 50)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 50)
            self.point = QPoint(new_w, new_h)
            self.repaint()

    def resizeEvent(self, e):
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.point = QPoint(0, 0)
            self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())