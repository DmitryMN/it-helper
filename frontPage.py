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
from const import PATH_LOCAL, PATH_ROAMING
from utils import find_directory, create_file_local, get_path_home, write_log, create_file_on_server, clear_directory
from command import (comandProblemPc, comandSignature, comandClearTemp, comandNetCache, comandCookies,
                     comandClearEdge, commandStopOutlook, comandClearYandex, commandChangeCartridge,
                     comandClearJava, commandAddNewPrinterSpp, commandRejectCitrixSpp, commandBidRemote,
                     commandProblemRemote, commandSettingsRemote, commandIBConfluence, commandProblemScanPrint,
                     commandArchive, commandAutoReplay, commandOfflineMode, commandItEnvironment, commandForNewUser,
                     commandAllConfluence, commandAdaptation, commandLinkNewArm, commandLinkMoveArm, commandLinkAddEquip,
                     commandLinkMobile, commandLinkPhoneSetting, commandLinkRedirectCall, commandLinkDdoSod, commandLinkOrd)
from worker import Worker

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
        self.setFixedSize(870, 680)
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
        self.documentBtn.clicked.connect(self.switch_to_failure_pageDocumentum)
        self.phishingBtn.clicked.connect(self.switch_to_failure_pagePhishing)
        self.vpnBtn.clicked.connect(self.switch_to_failure_pageVpn)
        self.learningBtn.clicked.connect(self.switch_to_failure_pageLearning)
        self.armBtn.clicked.connect(self.switch_to_failure_pageArm)
        self.oneCBtn.clicked.connect(self.switch_to_failure_pageOneC)
        self.callingBtn.clicked.connect(self.switch_to_failure_pagePhones)
        # switch mail stacked
        self.nextMailBtn.clicked.connect(self.next_mail_staked)
        self.returnMailBtn.clicked.connect(self.return_mail_staked)
        # switch print stacked
        self.nextPrintBtn.clicked.connect(self.next_print_staked)
        self.returnPrintBtn.clicked.connect(self.next_print_staked)
        # buttons pc page
        self.openDownloadPcBtn.clicked.connect(self.open_download_folderPc)
        self.openRecycleFolderPcBtn.clicked.connect(self.open_RecyclefolderPc)
        self.clearCashePcBtn.clicked.connect(self.clear_cacheHandler)
        self.problemSppPcBtn.clicked.connect(self.link_sppProblemPc)
        # buttons mail page
        self.securityOutMailBtn.clicked.connect(self.runOutlookSecurity)
        self.runOutMailBtn.clicked.connect(self.runOutlook)
        self.fixOutMailBtn.clicked.connect(self.fixOutlookView)
        self.signatureMailBtn.clicked.connect(self.moveInstructionSignature)
        self.archiveMailBtn.clicked.connect(self.move_archive_mail)
        self.autoReplayMailBtn.clicked.connect(self.move_auto_replay_mail)
        self.offlineModeMailBtn.clicked.connect(self.move_offline_mode)
        # buttons browser page
        self.edgeBrowserBtn.clicked.connect(self.clearEdge)
        self.firefoxBrowserBtn.clicked.connect(self.clearFirefox)
        self.yandexBrowserBtn.clicked.connect(self.clearYandex)
        # buttons printer page
        self.cartridgePrintBtn.clicked.connect(self.changeCartridge)
        self.connectPrintBtn.clicked.connect(self.helpAddnewPrinterSpp)
        self.myPrintersPrintBtn.clicked.connect(self.viewMyPrinter)
        self.addPrinterPrintBtn.clicked.connect(self.addPrinter)
        self.problemScanPrintBtn.clicked.connect(self.problem_scan_print)
        # buttons documentum page
        self.javaDocumentBtn.clicked.connect(self.clear_java_cache)
        self.moveOrdDocumentBtn.clicked.connect(self.link_ord)
        self.moveSodDocumentBtn.clicked.connect(self.link_ddo_sod)
        # buttons 1c page
        self.clearCasheOneCBtn.clicked.connect(self.clear_cache_one_c)
        self.clearCitrixOneCBtn.clicked.connect(self.refresh_session_citrix)
        self.refreshCitrixOneCBtn.clicked.connect(self.rerun_citrix)
        # buttons phishing page
        self.reportIbPhishingBtn.clicked.connect(self.send_mail_ib)
        self.teachIbCorsePhishingBtn.clicked.connect(self.teach_course_ib)
        # buttons VPN page
        self.bidRemoteVpnBtn.clicked.connect(self.send_bid_remote)
        self.problemVpnBtn.clicked.connect(self.link_problem_vpn)
        self.refreshVpnBtn.clicked.connect(self.refresh_vpn)
        self.settingVpnBtn.clicked.connect(self.settings_vpn)
        # buttons learning page
        self.newUserLearningBtn.clicked.connect(self.link_for_new_user)
        self.courseLearningBtn.clicked.connect(self.link_it_environment)
        self.confluenceLearningBtn.clicked.connect(self.link_all_confluence)
        self.adaptationLearningBtn.clicked.connect(self.link_adaptation)
        # buttons phone page
        self.newSettingPhoneBtn.clicked.connect(self.link_setting_phone)
        self.redirectPhoneBtn.clicked.connect(self.link_redirect_phone)
        self.mobilePhoneBtn.clicked.connect(self.link_mobile_phone)
        # buttons arm page
        self.createTaskArm.clicked.connect(self.link_new_arm)
        self.relocationTaskArm.clicked.connect(self.link_move_arm)
        self.equipmentTaskArm.clicked.connect(self.link_adding_equip)
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
        create_file_local(self.file_path)
        create_file_on_server(self.file_path)
        # start log
        self._run_log_worker(write_log, self.file_path,'ithelper-start', self.login, self.hostName, self.ipaddr)

    # switch handler stackedWidget
    def switch_to_failure_pagePC(self):
        self.mainStacked.setCurrentIndex(0)

    def switch_to_failure_pagePrint(self):
        self.mainStacked.setCurrentIndex(1)

    def switch_to_failure_pageDocumentum(self):
        self.mainStacked.setCurrentIndex(3)

    def switch_to_failure_pagePhishing(self):
        self.mainStacked.setCurrentIndex(6)

    def switch_to_failure_pageVpn(self):
        self.mainStacked.setCurrentIndex(7)

    def switch_to_failure_pageBrowser(self):
        self.mainStacked.setCurrentIndex(8)

    def switch_to_failure_pageMail(self):
        self.mainStacked.setCurrentIndex(9)

    def switch_to_failure_pageLearning(self):
        self.mainStacked.setCurrentIndex(10)

    def switch_to_failure_pageOneC(self):
        self.mainStacked.setCurrentIndex(2)

    def switch_to_failure_pageArm(self):
        self.mainStacked.setCurrentIndex(4)

    def switch_to_failure_pagePhones(self):
        self.mainStacked.setCurrentIndex(5)

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
    def switch_mail_stacked(self, page: int):
        if page == 1:
            self.mailStacked.setCurrentIndex(self.next_mail - 1)
            self.next_mail = 0
        else:
            self.mailStacked.setCurrentIndex(self.next_mail + 1)
            self.next_mail = 1

    def next_mail_staked(self):
        self.switch_mail_stacked(self.next_mail)

    def return_mail_staked(self):
        self.switch_mail_stacked(self.next_mail)

    # worker
    def _run_log_worker(self, func, *args, **kwargs):
        self._worker = Worker(func, *args, **kwargs)
        self._worker.start()
        self._worker.wait()

    def _get_result(self, result):
        self.loader(result, 2000)

    def _run_worker(self, func, *args, **kwargs):
        self._worker = Worker(func, *args, **kwargs)
        self._worker.result.connect(self._get_result)
        self._worker.finished.connect(self._finished_worker)
        self._worker.start()
        self._worker.wait()

    def _finished_worker(self):
        self.loader('', 4000)

    #switch handler print staked
    def switch_print_staked(self, page: int):
        if page == 1:
            self.printStacked.setCurrentIndex(self.next_print - 1)
            self.next_print = 0
        else:
            self.printStacked.setCurrentIndex(self.next_print + 1)
            self.next_print = 1

    def next_print_staked(self):
        self.switch_print_staked(self.next_print)

    def return_print_staked(self):
        self.switch_print_staked(self.next_print)

    # change informationField with timeout
    def loader(self, text, time=0):
        QTimer.singleShot(time, lambda: self.informationField.setText(text))

    # handler PC pages
    def open_download_folderPc(self):
        self.openDownloadPcBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command("Start-Process $env:USERPROFILE\Downloads")
        self.loader('', 3000)
        self.openDownloadPcBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-Downloads', self.login, self.hostName, self.ipaddr)

    def open_RecyclefolderPc(self):
        self.openRecycleFolderPcBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command("Start-Process shell:RecycleBinFolder")
        self.loader('', 3000)
        self.openRecycleFolderPcBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-Recycle', self.login, self.hostName, self.ipaddr)

    def link_sppProblemPc(self):
        self.problemSppPcBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(comandProblemPc)
        self.loader('', 3000)
        self.problemSppPcBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-ProblemPC', self.login, self.hostName, self.ipaddr)

    def clear_cacheHandler(self):
        self.clearCashePcBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(comandClearTemp)
        run_command(comandNetCache)
        run_command(comandCookies)
        self.clearCashePcBtn.setEnabled(True)
        self.loader('', 3000)
        self._run_log_worker(write_log, self.file_path,'Button-CachePC', self.login, self.hostName, self.ipaddr)

    # handler Mail pages
    def runOutlookSecurity(self):
        self.securityOutMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandStopOutlook)
        run_command("Start-Process outlook.exe /safe")
        self.loader('', 3000)
        self.securityOutMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-OutlookSafe', self.login, self.hostName, self.ipaddr)

    def runOutlook(self):
        self.runOutMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command("Start-Process outlook.exe")
        self.loader('', 3000)
        self.runOutMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-OutlookNormal', self.login, self.hostName, self.ipaddr)

    def fixOutlookView(self):
        self.fixOutMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandStopOutlook)
        run_command("Start-Process outlook.exe /cleanviews")
        self.loader('', 3000)
        self.fixOutMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-Outlook-cleanview', self.login, self.hostName, self.ipaddr)

    def moveInstructionSignature(self):
        self.signatureMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(comandSignature)
        self.loader('', 3000)
        self.signatureMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-Outlook-signature', self.login, self.hostName, self.ipaddr)

    def move_archive_mail(self):
        self.archiveMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandArchive)
        self.loader('', 3000)
        self.archiveMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-Outlook-archive', self.login, self.hostName, self.ipaddr)

    def move_auto_replay_mail(self):
        self.autoReplayMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandAutoReplay)
        self.loader('', 3000)
        self.autoReplayMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-Outlook-reply', self.login, self.hostName, self.ipaddr)

    def move_offline_mode(self):
        self.offlineModeMailBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandOfflineMode)
        self.loader('', 3000)
        self.offlineModeMailBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-Outlook-offline', self.login, self.hostName, self.ipaddr)

    # handler browser pages
    def clearEdge(self):
        self.edgeBrowserBtn.setEnabled(False)
        self.loader("Выполняется очистка кэша EDGE...")
        run_command("Get-Process msedge -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command(comandClearEdge)
        run_command(comandNetCache)
        run_command(comandCookies)
        self.loader('Кэш очищен!', 2000)
        self.loader('', 5000)
        run_lazy_command("Start-Process msedge", 4000)
        self.edgeBrowserBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-CacheEdge', self.login, self.hostName, self.ipaddr)

    def clearFirefox(self):
        self.firefoxBrowserBtn.setEnabled(False)
        self.loader("Выполняется очистка кэша Firefox...")
        run_command("Get-Process firefox -ErrorAction SilentlyContinue | Stop-Process -Force")
        self._run_worker(clear_firefox_local)
        self._run_worker(clear_firefox_cookies)
        run_lazy_command("Start-Process firefox", 6000)
        self.firefoxBrowserBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-CacheFirefox', self.login, self.hostName, self.ipaddr)

    def clearYandex(self):
        self.yandexBrowserBtn.setEnabled(False)
        if find_directory(r'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe') or \
                find_directory(get_path_home(r'AppData\Local\Yandex\YandexBrowser\Application\browser.exe')):
            self.loader("Выполняется очистка кэша Yandex...")
            run_command("Get-Process browser -ErrorAction SilentlyContinue | Stop-Process -Force")
            run_command(comandClearYandex)
            self.loader('Кэш очищен!', 2000)
            self.loader('', 5000)
            self._run_log_worker(write_log, self.file_path,'Button-CacheYandex', self.login, self.hostName, self.ipaddr)
            if find_directory(r'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe'):
                run_command(r"Start-Process 'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe'")
            else:
                browser_path = get_path_home(r'AppData\Local\Yandex\YandexBrowser\Application\browser.exe')
                run_command(f"Start-Process {browser_path}")
        else:
            self.loader("Yandex браузер не установлен!")
            self.loader('', 5000)
        self.yandexBrowserBtn.setEnabled(True)

    # handler print pages
    def changeCartridge(self):
        self.cartridgePrintBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandChangeCartridge)
        self.loader('', 3000)
        self.cartridgePrintBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-PrintCartridge', self.login, self.hostName, self.ipaddr)

    def helpAddnewPrinterSpp(self):
        self.connectPrintBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandAddNewPrinterSpp)
        self.loader('', 3000)
        self.connectPrintBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-NetworkPrinter', self.login, self.hostName, self.ipaddr)

    def viewMyPrinter(self):
        self.myPrintersPrintBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command("Start-Process 'control.exe' '/name Microsoft.DevicesAndPrinters'")
        self.loader('', 3000)
        self.myPrintersPrintBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-ShowLocalPrinters', self.login, self.hostName, self.ipaddr)

    def addPrinter(self):
        self.addPrinterPrintBtn.setEnabled(False)
        self._run_log_worker(write_log, self.file_path,'Button-AddPrinter', self.login, self.hostName, self.ipaddr)
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
        self.addPrinterPrintBtn.setEnabled(True)

    def problem_scan_print(self):
        self.problemScanPrintBtn.setEnabled(False)
        run_command(commandProblemScanPrint)
        self.problemScanPrintBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-ProblemPrintScan', self.login, self.hostName, self.ipaddr)

    # handler documentum page
    def clear_java_cache(self):
        self.javaDocumentBtn.setEnabled(False)
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
        self. loader('Кэш очищен!', 4000)
        self.loader('', 5000)
        run_lazy_command("Start-Process msedge", 5000)
        self.javaDocumentBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-CacheJava+CacheEdge', self.login, self.hostName, self.ipaddr)

    def link_ddo_sod(self):
        self.moveSodDocumentBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkDdoSod)
        self.loader('', 3000)
        self.moveSodDocumentBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-ddo-sod', self.login, self.hostName, self.ipaddr)

    def link_ord(self):
        self.moveOrdDocumentBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkOrd)
        self.loader('', 3000)
        self.moveOrdDocumentBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-ord', self.login, self.hostName, self.ipaddr)

    # handler phishing page
    def send_mail_ib(self):
        self.reportIbPhishingBtn.setEnabled(False)
        self.loader("Выполняется...")
        send_mail(self.login, 'inc@sogaz.ru', 'Письмо по теме ИБ')
        self.loader('', 3000)
        self.reportIbPhishingBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Message-Fishing', self.login, self.hostName, self.ipaddr)

    def teach_course_ib(self):
        self.teachIbCorsePhishingBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandIBConfluence)
        self.loader('', 3000)
        self.teachIbCorsePhishingBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-Course-Ib', self.login, self.hostName, self.ipaddr)

    # handler Vpn page
    def send_bid_remote(self):
        self.bidRemoteVpnBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandBidRemote)
        self.loader('', 3000)
        self.bidRemoteVpnBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-VPN', self.login, self.hostName, self.ipaddr)

    def link_problem_vpn(self):
        self.problemVpnBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandProblemRemote)
        self.loader('', 3000)
        self.problemVpnBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-VPN-Problem', self.login, self.hostName, self.ipaddr)

    def refresh_vpn(self):
        self.refreshVpnBtn.setEnabled(False)
        self.loader("Выполняется...")
        send_mail(self.login, 'help@sogaz.ru', 'Сброс 2 фактора')
        self.loader('', 3000)
        self.refreshVpnBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Message-VPNSecondFactor', self.login, self.hostName, self.ipaddr)

    def settings_vpn(self):
        self.settingVpnBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandSettingsRemote)
        self.loader('', 3000)
        self.settingVpnBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-VPN-Instuctions', self.login, self.hostName, self.ipaddr)

    # handler learning page
    def link_it_environment(self):
        self.courseLearningBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandItEnvironment)
        self.loader('', 3000)
        self.courseLearningBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-It-Environment', self.login, self.hostName, self.ipaddr)

    def link_for_new_user(self):
        self.newUserLearningBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandForNewUser)
        self.loader('', 3000)
        self.newUserLearningBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-new-user', self.login, self.hostName, self.ipaddr)

    def link_all_confluence(self):
        self.confluenceLearningBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandAllConfluence)
        self.loader('', 3000)
        self.confluenceLearningBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-all-confluence', self.login, self.hostName, self.ipaddr)

    def link_adaptation(self):
        self.adaptationLearningBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandAdaptation)
        self.loader('', 3000)
        self.adaptationLearningBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-adaptation', self.login, self.hostName, self.ipaddr)

    # handler arm btn
    def link_new_arm(self):
        self.createTaskArm.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkNewArm)
        self.loader('', 3000)
        self.createTaskArm.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-new-arm', self.login, self.hostName, self.ipaddr)

    def link_move_arm(self):
        self.relocationTaskArm.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkMoveArm)
        self.loader('', 3000)
        self.relocationTaskArm.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-move-arm', self.login, self.hostName, self.ipaddr)

    def link_adding_equip(self):
        self.equipmentTaskArm.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkAddEquip)
        self.loader('', 3000)
        self.equipmentTaskArm.setEnabled(True)
        self._run_log_worker(write_log,self.file_path, 'Link-add-equip-arm', self.login, self.hostName, self.ipaddr)

    # handler phones
    def link_setting_phone(self):
        self.newSettingPhoneBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkPhoneSetting)
        self.loader('', 3000)
        self.newSettingPhoneBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-setting-phone', self.login, self.hostName, self.ipaddr)

    def link_redirect_phone(self):
        self.redirectPhoneBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkRedirectCall)
        self.loader('', 3000)
        self.redirectPhoneBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-redirect-phone', self.login, self.hostName, self.ipaddr)

    def link_mobile_phone(self):
        self.mobilePhoneBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandLinkMobile)
        self.loader('', 3000)
        self.mobilePhoneBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path, 'Link-mobile-phone', self.login, self.hostName, self.ipaddr)

    # handler 1c
    def clear_cache_one_c(self):
        self.clearCasheOneCBtn.setEnabled(False)
        self.loader("Выполняется очистка кэша 1С")
        run_command("Get-Process 1cv8 -ErrorAction SilentlyContinue | Stop-Process -Force")
        self._run_worker(clear_directory, PATH_LOCAL, [''], '1C')
        self._run_worker(clear_directory, PATH_ROAMING, ['1CEStart'], '1C')
        run_lazy_command(r"Start-Process 'C:\Program Files\1cv8\common\1cestart.exe'", 6000)
        self.clearCasheOneCBtn.setEnabled(True)
        self._run_log_worker(write_log,self.file_path, 'Button-ClearCache-1C', self.login, self.hostName, self.ipaddr)

    def rerun_citrix(self):
        self.refreshCitrixOneCBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command("Get-Process concentr -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process receiver -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command("Get-Process wfcrun32 -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command( "Get-Process pnamain -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_command( "Get-Process wfica32 -ErrorAction SilentlyContinue | Stop-Process -Force")
        run_lazy_command('Start-Process "C:\Program Files (x86)\Citrix\ICA Client\pnagent.exe"', 3000)
        self.loader('Задача завершена!', 4000)
        self.loader('', 6000)
        self.refreshCitrixOneCBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Button-CitrixRestart', self.login, self.hostName, self.ipaddr)

    def refresh_session_citrix(self):
        self.clearCitrixOneCBtn.setEnabled(False)
        self.loader("Выполняется...")
        run_command(commandRejectCitrixSpp)
        self.loader('', 3000)
        self.clearCitrixOneCBtn.setEnabled(True)
        self._run_log_worker(write_log, self.file_path,'Link-CitrixSessionRestart', self.login, self.hostName, self.ipaddr)

    # handler help btn
    def link_PortalSpp(self):
        self.loader("Выполняется...")
        run_command(r'Start-Process https://help')
        self.loader('', 3000)
        self._run_log_worker(write_log,self.file_path, 'Link-PortalSpp', self.login, self.hostName, self.ipaddr)

    def feedback(self):
        self.loader("Выполняется...")
        send_mail(self.login, '00-38.selfservicehelp@sogaz.ru', 'Обратная связь')
        self.loader('', 3000)
        self._run_log_worker(write_log, self.file_path,'Message-Feedback', self.login, self.hostName, self.ipaddr)

    # actions for get system information
    def set_hostName(self, hostname):
        self.pcNameBottom.setText(hostname)

    def set_IpAddress(self, ipaddr):
        self.ipBottom.setText(ipaddr)

    def set_userName(self):
        self.userBottom.setText(self.login)

    def set_reloadInformation(self):
        self.reloadInformation.setText(reboot_information())
