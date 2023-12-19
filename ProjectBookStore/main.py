import Windows
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


if __name__ == '__main__':
    application = QApplication(sys.argv)
    stylesheet = open("MainStyle.qss", "r").read()
    application.setStyleSheet(stylesheet)
    start_window = Windows.StartWindow()
    start_window.show()
    application.exec()
