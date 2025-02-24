from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_interface import Ui_MainWindow
import subprocess
import socket

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('IT-Helper')

        #Connect buttons to switch to different page
        self.failureBtn.clicked.connect(self.switch_to_failure_pagePC)
        self.mailBtn.clicked.connect(self.switch_to_failure_pageMail)
        self.browserBtn.clicked.connect(self.switch_to_failure_pageBrowser)
        self.printBtn.clicked.connect(self.switch_to_failure_pagePrint)
        self.documentBtn.clicked.connect(self.switch_to_failure_pageDocument)
        self.phishingBtn.clicked.connect(self.switch_to_failure_pagePhishing)
        self.vpnBtn.clicked.connect(self.switch_to_failure_pageVpn)
        #buttons main pages
        self.openDownloadPcBtn.clicked.connect(self.open_download_folderPc)
        self.openRecycleFolderPcBtn.clicked.connect(self.open_RecyclefolderPc)
        self.get_system_info()


    #switch actions stackedWidget
    def switch_to_failure_pagePC(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_failure_pageMail(self):
        self.stackedWidget.setCurrentIndex(6)
    def switch_to_failure_pageBrowser(self):
        self.stackedWidget.setCurrentIndex(5)
    def switch_to_failure_pagePrint(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_to_failure_pageDocument(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_failure_pagePhishing(self):
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_failure_pageVpn(self):
        self.stackedWidget.setCurrentIndex(4)

    #actions button pages
    def open_download_folderPc(self):
        subprocess.Popen(["powershell","Start-Process $env:USERPROFILE\Downloads"],stdout=subprocess.PIPE)

    def open_RecyclefolderPc(self):
        subprocess.Popen(["powershell", "Start-Process shell:RecycleBinFolder"], stdout=subprocess.PIPE)

    def get_system_info(self):
        hostName = socket.gethostname()
        result = hostName or 'not name';
        self.ipBottom.setText(result)


