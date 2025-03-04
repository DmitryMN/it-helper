import os
import sys
from PySide6.QtWidgets import QApplication
from frontPage import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()