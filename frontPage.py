import os
import socket
import platform
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from ui_interface import Ui_MainWindow
from clearFirefox import clear_firefox_local, clear_firefox_cookies
from runCommand import run_command, run_lazy_command
from addNewPrinter import add_new_printer
from mail_utils import send_mail, reboot_information
from getExpiryDays import get_expiry_days
from const import PATH_PC, PATH_SERVER
from utils import create_empty_file, create_folder, find_directory, get_path, logging, get_path_home
from command import (comandProblemPc, comandSignature, comandClearTemp, comandNetCache, comandCookies,
                     comandClearEdge, commandStopOutlook, comandClearYandex, commandChangeCartridge,
                     comandClearJava, commandAddNewPrinterSpp, commandRejectCitrixSpp, commandBidRemote,
                     commandProblemRemote, commandSettingsRemote, commandIBConfluence, commandProblemScanPrint,
                     commandArchive, commandAutoReplay, commandOfflineMode, commandItEnvironment, commandForNewUser,
                     commandAllConfluence, commandAdaptation)

icon_filename = os.path.join(
    os.path.dirname(__file__), "icon\logo_main.ico"
)


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('IT-Helper')
        self.setWindowIcon(QIcon(icon_filename))
        # fix window size
        self.setFixedSize(860, 640)
        # hostname
        self.hostName = platform.uname().node
        # login
        self.login = os.getlogin()
        # ipaddr
        self.ipaddr = socket.gethostbyname(self.hostName)
        # file path
        self.file_path = f'{self.hostName}.txt'
        # next staked mail
        self.next_mail = 0
        # next staked print
        self.next_print = 0
        #self timer
        self.close_timer = QTimer()
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(self.close_application)
        self.close_timer.start(1800000)

        # Connect buttons to switch to different page
        self.failureBtn.clicked.connect(self.switch_to_failure_pagePC)
        self.mailBtn.clicked.connect(self.switch_to_failure_pageMail)
        self.browserBtn.clicked.connect(self.switch_to_failure_pageBrowser)
        self.printBtn.clicked.connect(self.switch_to_failure_pagePrint)
        self.documentBtn.clicked.connect(self.switch_to_failure_pageDocument)
        self.phishingBtn.clicked.connect(self.switch_to_failure_pagePhishing)
        self.vpnBtn.clicked.connect(self.switch_to_failure_pageVpn)
        self.learningBtn.clicked.connect(self.switch_to_failure_pageLearning)
        # switch mail stacked
        self.nextMailBtn.clicked.connect(self.next_mail_staked)
        self.returnMailBtn.clicked.connect(self.return_mail_staked)
        # switch print stacked
        self.nextPrintBtn.clicked.connect(self.next_print_staked)
        self.returnPrintBtn.clicked.connect(self.next_print_staked)
        # buttons pc pages
        self.openDownloadPcBtn.clicked.connect(self.open_download_folderPc)
        self.openRecycleFolderPcBtn.clicked.connect(self.open_RecyclefolderPc)
        self.clearCashePcBtn.clicked.connect(self.clear_cacheHandler)
        self.problemSppPcBtn.clicked.connect(self.link_sppProblemPc)
        # buttons mail
        self.securityOutMailBtn.clicked.connect(self.runOutlookSecurity)
        self.runOutMailBtn.clicked.connect(self.runOutlook)
        self.fixOutMailBtn.clicked.connect(self.fixOutlookView)
        self.signatureMailBtn.clicked.connect(self.moveInstructionSignature)
        self.archiveMailBtn.clicked.connect(self.move_archive_mail)
        self.autoReplayMailBtn.clicked.connect(self.move_auto_replay_mail)
        self.offlineModeMailBtn.clicked.connect(self.move_offline_mode)
        # buttons browser
        self.edgeBrowserBtn.clicked.connect(self.clearEdge)
        self.firefoxBrowserBtn.clicked.connect(self.clearFirefox)
        self.yandexBrowserBtn.clicked.connect(self.clearYandex)
        # buttons printers
        self.cartridgePrintBtn.clicked.connect(self.changeCartridge)
        self.connectPrintBtn.clicked.connect(self.helpAddnewPrinterSpp)
        self.myPrintersPrintBtn.clicked.connect(self.viewMyPrinter)
        self.addPrinterPrintBtn.clicked.connect(self.addPrinter)
        self.problemScanPrintBtn.clicked.connect(self.problem_scan_print)
        # button documentum
        self.javaDocumentBtn.clicked.connect(self.clear_java_cache)
        self.citrixDocumentBtn.clicked.connect(self.rerun_citrix)
        self.clearCitrixDocumentBtn.clicked.connect(self.refresh_session_citrix)
        # button phishing
        self.reportIbPhishingBtn.clicked.connect(self.send_mail_ib)
        self.teachIbCorsePhishingBtn.clicked.connect(self.teach_course_ib)
        # button VPN
        self.bidRemoteVpnBtn.clicked.connect(self.send_bid_remote)
        self.problemVpnBtn.clicked.connect(self.link_problem_vpn)
        self.refreshVpnBtn.clicked.connect(self.refresh_vpn)
        self.settingVpnBtn.clicked.connect(self.settings_vpn)
        #button learning
        self.newUserLearningBtn.clicked.connect(self.link_for_new_user)
        self.courseLearningBtn.clicked.connect(self.link_it_environment)
        self.confluenceLearningBtn.clicked.connect(self.link_all_confluence)
        self.adaptationLearningBtn.clicked.connect(self.link_adaptation)
        # buttons help
        self.feedbackBtn.clicked.connect(self.feedback)
        self.portalSppBtn.clicked.connect(self.link_PortalSpp)
        # get system information
        self.set_hostName(self.hostName)
        self.set_IpAddress(self.ipaddr)
        self.set_userName()
        self.set_reloadInformation()
        QTimer.singleShot(2000, lambda: self.init_password_expiry())
        # create folder and file
        self.create_file_pc(self.file_path)
        self.create_file_server(self.file_path)
        # start log
        self.write_log('ithelper-start', self.login, self.hostName, self.ipaddr)

    # switch handler stackedWidget
    def switch_to_failure_pagePC(self):
        self.mainStacked.setCurrentIndex(0)

    def switch_to_failure_pageMail(self):
        self.mainStacked.setCurrentIndex(6)

    def switch_to_failure_pageBrowser(self):
        self.mainStacked.setCurrentIndex(5)

    def switch_to_failure_pagePrint(self):
        self.mainStacked.setCurrentIndex(1)

    def switch_to_failure_pageDocument(self):
        self.mainStacked.setCurrentIndex(2)

    def switch_to_failure_pagePhishing(self):
        self.mainStacked.setCurrentIndex(3)

    def switch_to_failure_pageVpn(self):
        self.mainStacked.setCurrentIndex(4)

    def switch_to_failure_pageLearning(self):
        self.mainStacked.setCurrentIndex(7)

    #close application
    def close_application(self):
        QApplication.quit()

    def init_password_expiry(self):
        result = get_expiry_days(self.login)
        if result == 0:
            self.expiryDays.setText('Ошибка, домен не найден!')
        else:
            self.expiryDays.setText(str(result))

    #switch handler mail staked
    def next_mail_staked(self):
        if self.next_mail == 1:
            self.mailStacked.setCurrentIndex(self.next_mail - 1)
            self.next_mail = 0
        else:
            self.mailStacked.setCurrentIndex(1)
            self.next_mail = 1

    def return_mail_staked(self):
        if self.next_mail == 0:
            self.mailStacked.setCurrentIndex(self.next_mail + 1)
            self.next_mail = 1
        else:
            self.mailStacked.setCurrentIndex(0)
            self.next_mail = 0
    #switch handler print staked
    def next_print_staked(self):
        if self.next_print == 1:
            self.printStacked.setCurrentIndex(self.next_print - 1)
            self.next_print = 0
        else:
            self.printStacked.setCurrentIndex(1)
            self.next_print = 1

    def return_print_staked(self):
        if self.next_print == 0:
            self.printStacked.setCurrentIndex(self.next_print + 1)
            self.next_print = 1
        else:
            self.printStacked.setCurrentIndex(0)
            self.next_print = 0

    # change informationField with timeout
    def loader(self, text, time=0):
        QTimer.singleShot(time, lambda: self.informationField.setText(text))

    # create folder and file for logging
    def create_file_pc(self, file_name):
        if not find_directory(get_path(PATH_PC)):
            create_folder(get_path(PATH_PC))
            create_empty_file(get_path(PATH_PC, file_name))
        else:
            if find_directory(get_path(PATH_PC, file_name)):
                return
            else:
                create_empty_file(get_path(PATH_PC, file_name))

    def create_file_server(self, file_name):
        if find_directory(get_path(PATH_SERVER)):
            if not find_directory(get_path(PATH_SERVER, file_name)):
                create_empty_file(get_path(PATH_SERVER, file_name))

    # write log
    def write_log(self, command, login, hostname, ip):
        logging(get_path(PATH_PC, self.file_path), command, login, hostname, ip)
        if find_directory(get_path(PATH_SERVER, self.file_path)):
            logging(get_path(PATH_SERVER, self.file_path), command, login, hostname, ip)

    # handler PC pages
    def open_download_folderPc(self):
        self.loader("Выполняется...")
        run_command("Start-Process $env:USERPROFILE\Downloads")
        self.loader('', 3000)
        self.write_log('Button-Downloads', self.login, self.hostName, self.ipaddr)

    def open_RecyclefolderPc(self):
        self.loader("Выполняется...")
        run_command("Start-Process shell:RecycleBinFolder")
        self.loader('', 3000)
        self.write_log('Button-Recycle', self.login, self.hostName, self.ipaddr)

    def link_sppProblemPc(self):
        self.loader("Выполняется...")
        run_command(comandProblemPc)
        self.loader('', 3000)
        self.write_log('Link-ProblemPC', self.login, self.hostName, self.ipaddr)

    def clear_cacheHandler(self):
        self.loader("Выполняется...")
        run_command(comandClearTemp)
        run_command(comandNetCache)
        run_command(comandCookies)
        self.loader('', 3000)
        self.write_log('Button-CachePC', self.login, self.hostName, self.ipaddr)

    # handler Mail pages
    def runOutlookSecurity(self):
        self.loader("Выполняется...")
        run_command(commandStopOutlook)
        run_command("Start-Process outlook.exe /safe")
        self.loader('', 3000)
        self.write_log('Button-OutlookSafe', self.login, self.hostName, self.ipaddr)

    def runOutlook(self):
        self.loader("Выполняется...")
        run_command("Start-Process outlook.exe")
        self.loader('', 3000)
        self.write_log('Button-OutlookNormal', self.login, self.hostName, self.ipaddr)

    def fixOutlookView(self):
        self.loader("Выполняется...")
        run_command(commandStopOutlook)
        run_command("Start-Process outlook.exe /cleanviews")
        self.loader('', 3000)
        self.write_log('Button-Outlook-cleanview', self.login, self.hostName, self.ipaddr)

    def moveInstructionSignature(self):
        self.loader("Выполняется...")
        run_command(comandSignature)
        self.loader('', 3000)
        self.write_log('Link-Outlook-signature', self.login, self.hostName, self.ipaddr)

    def move_archive_mail(self):
        self.loader("Выполняется...")
        run_command(commandArchive)
        self.loader('', 3000)
        self.write_log('Link-Outlook-archive', self.login, self.hostName, self.ipaddr)

    def move_auto_replay_mail(self):
        self.loader("Выполняется...")
        run_command(commandAutoReplay)
        self.loader('', 3000)
        self.write_log('Link-Outlook-reply', self.login, self.hostName, self.ipaddr)

    def move_offline_mode(self):
        self.loader("Выполняется...")
        run_command(commandOfflineMode)
        self.loader('', 3000)
        self.write_log('Link-Outlook-offline', self.login, self.hostName, self.ipaddr)

    # handler browser pages
    def clearEdge(self):
        self.loader("Выполняется очистка кэша EDGE...")
        run_command("Get-Process msedge -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command(comandClearEdge)
        self.loader('Кэш очищен!', 2000)
        self.loader('', 5000)
        run_lazy_command("Start-Process msedge", 4000)
        self.write_log('Button-CacheEdge', self.login, self.hostName, self.ipaddr)

    def clearFirefox(self):
        self.loader("Выполняется очистка кэша Firefox...")
        run_command("Get-Process firefox -ErrorAction SilentlyContinue | Stop-Process -Force")
        clear_firefox_cookies()
        clear_firefox_local()
        self.loader('Кэш очищен!', 2000)
        self.loader('', 5000)
        run_lazy_command("Start-Process firefox", 4000)
        self.write_log('Button-CacheFirefox', self.login, self.hostName, self.ipaddr)

    def clearYandex(self):
        if find_directory(r'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe') or \
                find_directory(get_path_home(r'AppData\Local\Yandex\YandexBrowser\Application\browser.exe')):
            self.loader("Выполняется очистка кэша Yandex...")
            run_command("Get-Process browser -ErrorAction SilentlyContinue | Stop-Process -Force")
            run_command(comandClearYandex)
            self.loader('Кэш очищен!', 2000)
            self.loader('', 5000)
            self.write_log('Button-CacheYandex', self.login, self.hostName, self.ipaddr)
            if find_directory(r'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe'):
                run_command(r"Start-Process 'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe'")
            else:
                browser_path = get_path_home(r'AppData\Local\Yandex\YandexBrowser\Application\browser.exe')
                run_command(f"Start-Process {browser_path}")
        else:
            self.loader("Yandex браузер не установлен!")
            self.loader('', 5000)

    # handler print pages
    def changeCartridge(self):
        self.loader("Выполняется...")
        run_command(commandChangeCartridge)
        self.loader('', 3000)
        self.write_log('Link-PrintCartridge', self.login, self.hostName, self.ipaddr)

    def helpAddnewPrinterSpp(self):
        self.loader("Выполняется...")
        run_command(commandAddNewPrinterSpp)
        self.loader('', 3000)
        self.write_log('Link-NetworkPrinter', self.login, self.hostName, self.ipaddr)

    def viewMyPrinter(self):
        self.loader("Выполняется...")
        run_command("Start-Process 'control.exe' '/name Microsoft.DevicesAndPrinters'")
        self.loader('', 3000)
        self.write_log('Button-ShowLocalPrinters', self.login, self.hostName, self.ipaddr)

    def addPrinter(self):
        self.write_log('Button-AddPrinter', self.login, self.hostName, self.ipaddr)
        if len(self.hostName) != 0:
            self.loader("Подождите, идет подключение...")
            slice_hostname = self.hostName[4:6]
            message = add_new_printer(slice_hostname)
            if message is None:
                self.loader('', 4000)
            else:
                self.loader(message)
                self.loader('', 4000)
        else:
            self.loader("Имя ПК отсутствует...")
            self.loader('', 3000)

    def problem_scan_print(self):
        run_command(commandProblemScanPrint)
        self.write_log('Link-ProblemPrintScan', self.login, self.hostName, self.ipaddr)

    # handler documentum,1C page
    def clear_java_cache(self):
        self.loader("Выполняется...")
        run_command("Get-Process java -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command(comandNetCache)
        run_command(comandCookies)
        run_command(comandClearJava)
        run_command("Start-Process java")
        self.loader('', 2000)
        self.loader("Выполняется очистка кэша EDGE...", 3000)
        run_command("Get-Process msedge -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command(comandClearEdge)
        self.loader('Кэш очищен!', 4000)
        self.loader('', 5000)
        run_lazy_command("Start-Process msedge", 5000)
        self.write_log('Button-CacheJava+CacheEdge', self.login, self.hostName, self.ipaddr)

    def rerun_citrix(self):
        self.loader("Выполняется...")
        run_command("Get-Process concentr -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process receiver -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process wfcrun32 -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process pnamain -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process wfica32 -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command('Start-Process "C:\Program Files (x86)\Citrix\ICA Client\pnagent.exe"')
        self.loader('', 3000)
        self.write_log('Button-CitrixRestart', self.login, self.hostName, self.ipaddr)

    def refresh_session_citrix(self):
        self.loader("Выполняется...")
        run_command(commandRejectCitrixSpp)
        self.loader('', 3000)
        self.write_log('Link-CitrixSessionRestart', self.login, self.hostName, self.ipaddr)

    # handler phishing page
    def send_mail_ib(self):
        self.loader("Выполняется...")
        send_mail(self.login, 'inc@sogaz.ru', 'Письмо по теме ИБ')
        self.loader('', 3000)
        self.write_log('Message-Fishing', self.login, self.hostName, self.ipaddr)

    def teach_course_ib(self):
        self.loader("Выполняется...")
        run_command(commandIBConfluence)
        self.loader('', 3000)
        self.write_log('Link-Course-Ib', self.login, self.hostName, self.ipaddr)

    # handler Vpn page
    def send_bid_remote(self):
        self.loader("Выполняется...")
        run_command(commandBidRemote)
        self.loader('', 3000)
        self.write_log('Link-VPN', self.login, self.hostName, self.ipaddr)

    def link_problem_vpn(self):
        self.loader("Выполняется...")
        run_command(commandProblemRemote)
        self.loader('', 3000)
        self.write_log('Link-VPN-Problem', self.login, self.hostName, self.ipaddr)

    def refresh_vpn(self):
        self.loader("Выполняется...")
        send_mail(self.login, 'help@sogaz.ru', 'Сброс 2 фактора')
        self.loader('', 3000)
        self.write_log('Message-VPNSecondFactor', self.login, self.hostName, self.ipaddr)

    def settings_vpn(self):
        self.loader("Выполняется...")
        run_command(commandSettingsRemote)
        self.loader('', 3000)
        self.write_log('Link-VPN-Instuctions', self.login, self.hostName, self.ipaddr)

    # handler learning page
    def link_it_environment(self):
        self.loader("Выполняется...")
        run_command(commandItEnvironment)
        self.loader('', 3000)
        self.write_log('Link-It-Environment', self.login, self.hostName, self.ipaddr)

    def link_for_new_user(self):
        self.loader("Выполняется...")
        run_command(commandForNewUser)
        self.loader('', 3000)
        self.write_log('Link-new-user', self.login, self.hostName, self.ipaddr)

    def link_all_confluence(self):
        self.loader("Выполняется...")
        run_command(commandAllConfluence)
        self.loader('', 3000)
        self.write_log('Link-all-confluence', self.login, self.hostName, self.ipaddr)

    def link_adaptation(self):
        self.loader("Выполняется...")
        run_command(commandAdaptation)
        self.loader('', 3000)
        self.write_log('Link-adaptation', self.login, self.hostName, self.ipaddr)

    # handler help btn
    def link_PortalSpp(self):
        self.loader("Выполняется...")
        run_command(r'Start-Process https://help')
        self.loader('', 3000)
        self.write_log('Link-PortalSpp', self.login, self.hostName, self.ipaddr)

    def feedback(self):
        self.loader("Выполняется...")
        send_mail(self.login, '00-38.selfservicehelp@sogaz.ru', 'Обратная связь')
        self.loader('', 3000)
        self.write_log('Message-Feedback', self.login, self.hostName, self.ipaddr)

    # actions for get system information
    def set_hostName(self, hostname):
        self.pcNameBottom.setText(hostname)

    def set_IpAddress(self, ipaddr):
        self.ipBottom.setText(ipaddr)

    def set_userName(self):
        self.userBottom.setText(self.login)

    def set_reloadInformation(self):
        self.reloadInformation.setText(reboot_information())
