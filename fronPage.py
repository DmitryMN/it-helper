import os
import subprocess
import socket
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_interface import Ui_MainWindow
from path_all import (path_temp, path_cookies, path_netCache)
from command import problemComndPc, signatureComndMail

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('IT-Helper')
        self.setFixedSize(860,640)
        #get hostname
        self.hostName = socket.gethostname()

        #Connect buttons to switch to different page
        self.failureBtn.clicked.connect(self.switch_to_failure_pagePC)
        self.mailBtn.clicked.connect(self.switch_to_failure_pageMail)
        self.browserBtn.clicked.connect(self.switch_to_failure_pageBrowser)
        self.printBtn.clicked.connect(self.switch_to_failure_pagePrint)
        self.documentBtn.clicked.connect(self.switch_to_failure_pageDocument)
        self.phishingBtn.clicked.connect(self.switch_to_failure_pagePhishing)
        self.vpnBtn.clicked.connect(self.switch_to_failure_pageVpn)
        #buttons pc pages
        self.openDownloadPcBtn.clicked.connect(self.open_download_folderPc)
        self.openRecycleFolderPcBtn.clicked.connect(self.open_RecyclefolderPc)
        self.clearCashePcBtn.clicked.connect(self.clear_cashHandler)
        self.problemSppPcBtn.clicked.connect(self.link_sppProblemPc)
        #buttons mail
        self.securityOutMailBtn.clicked.connect(self.runOutlookSecurity)
        self.runOutMailBtn.clicked.connect(self.runOutlook)
        self.fixOutMailBtn.clicked.connect(self.fixOutlookView)
        self.signatureMailBtn.clicked.connect(self.moveInstructionSignature)
        #get system information
        self.get_hostName(self.hostName)
        self.get_IpAddress(self.hostName)
        self.get_userName()


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

    #handler PC pages
    def open_download_folderPc(self):
        subprocess.Popen(["powershell","Start-Process $env:USERPROFILE\Downloads"],stdout=subprocess.PIPE)

    def open_RecyclefolderPc(self):
        subprocess.Popen(["powershell", "Start-Process shell:RecycleBinFolder"], stdout=subprocess.PIPE)

    def link_sppProblemPc(self):
        print("Run")
        subprocess.Popen(["powershell", problemComndPc], stdout=subprocess.PIPE)

    def clear_cache(self, path):
        command = f"Remove-Item {path} -Recurse -Force -ErrorAction SilentlyContinue"
        with subprocess.Popen(["powershell", command]) as proc:
            try:
                proc.wait(5)
            except:
                proc.terminate()
                proc.wait()

    #handler Mail pages
    def runOutlookSecurity(self):
        with subprocess.Popen(["powershell", "Stop-Process -Name OUTLOOK"]) as proc:
            try:
                proc.wait(5)
            except:
                proc.terminate()
                proc.wait()

        subprocess.Popen(["powershell", "Start-Process outlook.exe /safe"], stdout=subprocess.PIPE)

    def runOutlook(self):
        subprocess.Popen(["powershell", "Start-Process outlook.exe"], stdout=subprocess.PIPE)

    def fixOutlookView(self):
        with subprocess.Popen(["powershell", "Stop-Process -Name OUTLOOK"]) as proc:
            try:
                proc.wait(5)
            except:
                proc.terminate()
                proc.wait()

        subprocess.Popen(["powershell", "Start-Process outlook.exe /cleanviews"], stdout=subprocess.PIPE)

    def moveInstructionSignature(self):
        subprocess.Popen(["powershell", signatureComndMail], stdout=subprocess.PIPE)

    #handler clearCache
    def clear_cashHandler(self):
        self.clear_cache(path_temp)
        self.clear_cache(path_netCache)
        self.clear_cache(path_cookies)

    #actions for get system information
    def get_hostName(self, hostname):
        self.pcNameBottom.setText(hostname)

    def get_IpAddress(self, hostname):
        ipaddr = socket.gethostbyname(hostname)
        self.ipBottom.setText(ipaddr)

    def get_userName(self):
        self.userBottom.setText(os.getlogin())



