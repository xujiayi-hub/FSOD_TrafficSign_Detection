import unittest
import test3_canm
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5 import QtCore
from PyQt5.Qt import *
#测试图片识别功能和不同的模型
class TestUnit(unittest.TestCase):
     def test_case1(self):
         test3_canm.main('/home/smile/fsdownload/43.jpg', 2, '43.jpg')




if __name__ == '__main__':
    unittest.main()