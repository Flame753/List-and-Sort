# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

import sys
from PyQt5.QtWidgets import QApplication


class MainWindow(QMainWindow):
    pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
