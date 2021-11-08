import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(300, 300, 500, 300)  # start left corner (down,right,width, height)
    b.move(220, 130)  # move from top left corner (right, down)
    w.setWindowTitle("PyQt5")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
