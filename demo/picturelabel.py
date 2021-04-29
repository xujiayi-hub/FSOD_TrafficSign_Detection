from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
import os,sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("交通标志参考图")
        Form.resize(1200, 800)
        self.labellist=[]
        self.labellist_text = []
        for i in range(1,61):
            label=QtWidgets.QLabel(Form)
            label.setGeometry(QtCore.QRect(((i-1)%10)*110+10, int((i-1)/10)*120+40, 100, 80))
            label.setObjectName("label"+str(i))
            self.labellist.append(label)



        for i in range(1,61):
            label=QtWidgets.QLabel(Form)
            label.setGeometry(QtCore.QRect(((i-1)%10)*110+30, int((i-1)/10)*120+120, 70, 20))
            label.setObjectName("label"+str(i))
            self.labellist_text.append(label)


        #self.retranslateUi(Form)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        for i in range(0, 60):
             self.labellist_text[i].setText(_translate("Form", "TextLabel"+str(i)))


        QtCore.QMetaObject.connectSlotsByName(Form)


class window(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(window, self).__init__()
        #self.cwd = os.getcwd()
        self.setupUi(self)
        self.labels = self.labellist
        self.labels_text=self.labellist_text
        #self.slot_open_image()

    def slot_open_image(self,file):
        path='/home/smile/fsdownload/ToJIA'
        files = os.listdir(path)
        i=0
        for f in files:
            jpg = QtGui.QPixmap(path + '/' + f).scaled(self.labels[i].width(), self.labels[i].height())
            self.labels[i].setPixmap(jpg)
            _translate = QtCore.QCoreApplication.translate
            self.labels_text[i].setText(_translate("Form", f))
            ff=f.split('.')
            if ff[0] in file:
             self.labels_text[i].setStyleSheet("background-color:gold")
            else:
             self.labellist_text[i].setStyleSheet("background-color:transparent")
            i=i+1
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  my = window()
  my.show()
  sys.exit(app.exec_())
