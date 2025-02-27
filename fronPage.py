import os
import subprocess
import socket
import time
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_interface import Ui_MainWindow
from clearFirefox import clear_firefox_local, clear_firefox_cookies
from command import (comandProblemPc, comandSignature, comandClearTemp, comandNetCache, comandCookies,
                    comandClearEdge, commandStopOutlook, comandClearYandex, commandChangeCartridge, commandAddNewPrinterSpp)

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
        self.clearCashePcBtn.clicked.connect(self.clear_cacheHandler)
        self.problemSppPcBtn.clicked.connect(self.link_sppProblemPc)
        #buttons mail
        self.securityOutMailBtn.clicked.connect(self.runOutlookSecurity)
        self.runOutMailBtn.clicked.connect(self.runOutlook)
        self.fixOutMailBtn.clicked.connect(self.fixOutlookView)
        self.signatureMailBtn.clicked.connect(self.moveInstructionSignature)
        #buttons browser
        self.edgeBrowserBtn.clicked.connect(self.clearEdge)
        self.firefoxBrowserBtn.clicked.connect(self.clearFirefox)
        self.yandexBrowserBtn.clicked.connect(self.clearYandex)
        #buttons printers
        self.cartridgePrintBtn.clicked.connect(self.changeCartridge)
        self.connectPrintBtn.clicked.connect(self.helpAddnewPrinterSpp)
        self.myPrintersPrintBtn.clicked.connect(self.viewMyPrinter)
        self.addPrinterPrintBtn.clicked.connect(self.addPrinter)
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

    #run ps shell
    def run_command(self, command):
        with subprocess.Popen(["powershell", command]) as proc:
            try:
                proc.wait(3)
                print("run script")
            except:
                proc.terminate()
                proc.wait()

    #handler PC pages
    def open_download_folderPc(self):
        self.run_command("Start-Process $env:USERPROFILE\Downloads")

    def open_RecyclefolderPc(self):
        self.run_command("Start-Process shell:RecycleBinFolder")

    def link_sppProblemPc(self):
        self.run_command(comandProblemPc)

    def clear_cacheHandler(self):
        self.run_command(comandClearTemp)
        self.run_command(comandNetCache)
        self.run_command(comandCookies)

    #handler Mail pages
    def runOutlookSecurity(self):
        self.run_command(commandStopOutlook)
        self.run_command("Start-Process outlook.exe /safe")

    def runOutlook(self):
        self.run_command("Start-Process outlook.exe")

    def fixOutlookView(self):
        self.run_command(commandStopOutlook)
        self.run_command("Start-Process outlook.exe /cleanviews")

    def moveInstructionSignature(self):
        self.run_command(comandSignature)

    #handler browser pages
    def clearEdge(self):
        self.run_command("Get-Process msedge -ErrorAction SilentlyContinue | Stop-Process -Force")
        self.run_command(comandClearEdge)

    def clearFirefox(self):
        self.run_command("Get-Process firefox -ErrorAction SilentlyContinue | Stop-Process -Force")
        clear_firefox_cookies()
        time.sleep(2)
        clear_firefox_local()


    def clearYandex(self):
        self.run_command("Get-Process browser -ErrorAction SilentlyContinue | Stop-Process -Force")
        self.run_command(comandClearYandex)

    #handler print pages
    def changeCartridge(self):
        self.run_command(commandChangeCartridge)

    def helpAddnewPrinterSpp(self):
        self.run_command(commandAddNewPrinterSpp)

    def viewMyPrinter(self):
        self.run_command("Start-Process 'control.exe' '/name Microsoft.DevicesAndPrinters'")

    def addPrinter(self):
        pass

    #actions for get system information
    def get_hostName(self, hostname):
        self.pcNameBottom.setText(hostname)

    def get_IpAddress(self, hostname):
        ipaddr = socket.gethostbyname(hostname)
        self.ipBottom.setText(ipaddr)

    def get_userName(self):
        self.userBottom.setText(os.getlogin())



