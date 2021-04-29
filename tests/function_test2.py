import unittest
import test3_canm
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5 import QtCore
from PyQt5.Qt import *
#界面显示调用功能
class TestUnit(unittest.TestCase):
     def test_case1(self):
         test3_canm.main_()
         #sys.exit(app.exec_())



if __name__ == '__main__':
    unittest.main()