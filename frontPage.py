import os
import subprocess
import socket
import time
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_interface import Ui_MainWindow
from clearFirefox import clear_firefox_local, clear_firefox_cookies
from runCommand import run_command
from addNewPrinter import add_new_printer
from mail_utils import send_mail
from command import (comandProblemPc, comandSignature, comandClearTemp, comandNetCache, comandCookies,
                    comandClearEdge, commandStopOutlook, comandClearYandex, commandChangeCartridge,
                     comandClearJava, commandAddNewPrinterSpp, commandRejectCitrixSpp, commandBidRemote,
                     commandProblemRemote, commandSettingsRemote)

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('IT-Helper')
        self.setFixedSize(860,640)
        #hostname
        self.hostName = socket.gethostname()
        #login
        self.login =os.getlogin()

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
        #button documentum
        self.javaDocumentBtn.clicked.connect(self.clear_java_cache)
        self.citrixDocumentBtn.clicked.connect(self.rerun_citrix)
        self.clearCitrixDocumentBtn.clicked.connect(self.refresh_session_citrix)
        #button phishing
        self.reportIbPhishingBtn.clicked.connect(self.send_mail_ib)
        self.teachIbCorsePhishingBtn.clicked.connect(self.teach_course_ib)
        #button VPN
        self.bidRemoteVpnBtn.clicked.connect(self.send_bid_remote)
        self.problemVpnBtn.clicked.connect(self.link_problem_vpn)
        self.refreshVpnBtn.clicked.connect(self.refresh_vpn)
        self.settingVpnBtn.clicked.connect(self.settings_vpn)
        #get system information
        self.set_hostName(self.hostName)
        self.set_IpAddress(self.hostName)
        self.set_userName()

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
        run_command("Start-Process $env:USERPROFILE\Downloads")

    def open_RecyclefolderPc(self):
        run_command("Start-Process shell:RecycleBinFolder")

    def link_sppProblemPc(self):
        run_command(comandProblemPc)

    def clear_cacheHandler(self):
        run_command(comandClearTemp)
        run_command(comandNetCache)
        run_command(comandCookies)

    #handler Mail pages
    def runOutlookSecurity(self):
        run_command(commandStopOutlook)
        run_command("Start-Process outlook.exe /safe")

    def runOutlook(self):
        run_command("Start-Process outlook.exe")

    def fixOutlookView(self):
        run_command(commandStopOutlook)
        run_command("Start-Process outlook.exe /cleanviews")

    def moveInstructionSignature(self):
        run_command(comandSignature)

    #handler browser pages
    def clearEdge(self):
        run_command("Get-Process msedge -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command(comandClearEdge)

    def clearFirefox(self):
        self.run_command("Get-Process firefox -ErrorAction SilentlyContinue | Stop-Process -Force")
        clear_firefox_cookies()
        time.sleep(2)
        clear_firefox_local()

    def clearYandex(self):
        run_command("Get-Process browser -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command(comandClearYandex)

    #handler print pages
    def changeCartridge(self):
        run_command(commandChangeCartridge)

    def helpAddnewPrinterSpp(self):
        run_command(commandAddNewPrinterSpp)

    def viewMyPrinter(self):
        run_command("Start-Process 'control.exe' '/name Microsoft.DevicesAndPrinters'")

    def addPrinter(self):
        if(len(self.hostName) != 0):
            slice_hostname = self.hostName[:6].upper()
            add_new_printer(slice_hostname)
        else:
            print("Name pc is absent")

    #handler documentum,1C page
    def clear_java_cache(self):
        run_command("Get-Process java -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process msedge -ErrorAction SilentlyContinue | Stop-Process -Force")
        time.sleep(2)
        run_command(comandClearEdge)
        run_command(comandNetCache)
        run_command(comandCookies)
        run_command(comandClearJava)
        run_command("Start-Process java")
        run_command("Start-Process msedge")

    def rerun_citrix(self):
        run_command("Get-Process concentr -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process receiver -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process wfcrun32 -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process pnamain -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process wfica32 -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command('Start-Process "C:\Program Files (x86)\Citrix\ICA Client\pnagent.exe"')

    def refresh_session_citrix(self):
        run_command(commandRejectCitrixSpp)

    # handler phishing page
    def send_mail_ib(self):
        send_mail(self.login, 'inc@sogaz.ru')

    def teach_course_ib(self):
        print("Teach course")

    #handler Vpn page
    def send_bid_remote(self):
        run_command(commandBidRemote)
    def link_problem_vpn(self):
        run_command(commandProblemRemote)
    def refresh_vpn(self):
        send_mail(self.login, 'help@sogaz.ru')
    def settings_vpn(self):
        run_command(commandSettingsRemote)
    #actions for get system information
    def set_hostName(self, hostname):
        self.pcNameBottom.setText(hostname)

    def set_IpAddress(self, hostname):
        ipaddr = socket.gethostbyname(hostname)
        self.ipBottom.setText(ipaddr)

    def set_userName(self):
        self.userBottom.setText(self.login)



