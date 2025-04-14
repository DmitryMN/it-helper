import sys

from PySide6.QtWidgets import QApplication
from frontPage import MySideBar
import ctypes

myappid = 'it-helper'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)

window = MySideBar()

window.show()
sys.exit(app.exec())