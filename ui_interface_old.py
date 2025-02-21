# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacekczbrR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 640)
        MainWindow.setStyleSheet(u"* {\n"
"    color: rgba(21, 33, 73, 1);\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}\n"
"\n"
"#MainWindow {\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"}\n"
"\n"
"#leftMenuContainer {\n"
"    background-color: rgba(26, 51, 115, 0.05);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding: 5px;\n"
"    color: rgba(21, 33, 73, 0.5);\n"
"}\n"
"#Title {\n"
"    color: rgba(21, 33, 73, 1);\n"
"}\n"
"#header {\n"
"    border-bottom: 1px solid rgba(21, 33, 73, 1);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"")
        self.Title = QLabel(self.header)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 10, 160, 28))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.header)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QWidget(self.main)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuContainer.setAutoFillBackground(False)
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.leftSubMenuContainer = QWidget(self.leftMenuContainer)
        self.leftSubMenuContainer.setObjectName(u"leftSubMenuContainer")
        self.leftSubMenuContainer.setMinimumSize(QSize(130, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftSubMenuContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftSubMenuContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.failureBtn = QPushButton(self.frame)
        self.failureBtn.setObjectName(u"failureBtn")
        self.failureBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.failureBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.failureBtn.setIcon(icon)
        self.failureBtn.setIconSize(QSize(24, 24))
        self.failureBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.failureBtn)

        self.mailBtn = QPushButton(self.frame)
        self.mailBtn.setObjectName(u"mailBtn")
        self.mailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mailBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mailBtn.setIcon(icon1)
        self.mailBtn.setIconSize(QSize(24, 24))
        self.mailBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.mailBtn)

        self.browserBtn = QPushButton(self.frame)
        self.browserBtn.setObjectName(u"browserBtn")
        self.browserBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.browserBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.browserBtn.setIcon(icon2)
        self.browserBtn.setIconSize(QSize(24, 24))
        self.browserBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.browserBtn)

        self.printBtn = QPushButton(self.frame)
        self.printBtn.setObjectName(u"printBtn")
        self.printBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.printBtn.setIcon(icon3)
        self.printBtn.setIconSize(QSize(24, 24))
        self.printBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.printBtn)

        self.documentBtn = QPushButton(self.frame)
        self.documentBtn.setObjectName(u"documentBtn")
        self.documentBtn.setMinimumSize(QSize(0, 0))
        self.documentBtn.setMaximumSize(QSize(16777215, 16777215))
        self.documentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.documentBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/shuffle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.documentBtn.setIcon(icon4)
        self.documentBtn.setIconSize(QSize(24, 24))
        self.documentBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.documentBtn)

        self.phishingBtn = QPushButton(self.frame)
        self.phishingBtn.setObjectName(u"phishingBtn")
        self.phishingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.phishingBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/alert-triangle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.phishingBtn.setIcon(icon5)
        self.phishingBtn.setIconSize(QSize(24, 24))
        self.phishingBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.phishingBtn)

        self.vpnBtn = QPushButton(self.frame)
        self.vpnBtn.setObjectName(u"vpnBtn")
        self.vpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.vpnBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/shield.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vpnBtn.setIcon(icon6)
        self.vpnBtn.setIconSize(QSize(24, 24))
        self.vpnBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.vpnBtn)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.leftSubMenuContainer, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainBody = QWidget(self.main)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.stackedWidget = QStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(9, 9, 615, 380))
        self.pagePC = QWidget()
        self.pagePC.setObjectName(u"pagePC")
        self.mainSectionPc = QFrame(self.pagePC)
        self.mainSectionPc.setObjectName(u"mainSectionPc")
        self.mainSectionPc.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionPc.setMinimumSize(QSize(0, 0))
        self.mainSectionPc.setMaximumSize(QSize(615, 380))
        self.mainSectionPc.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionPc.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainSectionPc)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sectionTittlePc = QFrame(self.mainSectionPc)
        self.sectionTittlePc.setObjectName(u"sectionTittlePc")
        self.sectionTittlePc.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittlePc.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.sectionTittlePc)

        self.sectionButtonPc = QFrame(self.mainSectionPc)
        self.sectionButtonPc.setObjectName(u"sectionButtonPc")
        self.sectionButtonPc.setStyleSheet(u"#sectionButtonPc > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionButtonPc > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.sectionButtonPc.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonPc.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.sectionButtonPc)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clearCashePcBtn = QPushButton(self.sectionButtonPc)
        self.clearCashePcBtn.setObjectName(u"clearCashePcBtn")
        self.clearCashePcBtn.setMaximumSize(QSize(16777215, 115))
        self.clearCashePcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearCashePcBtn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/broom.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearCashePcBtn.setIcon(icon7)
        self.clearCashePcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.clearCashePcBtn)

        self.openDownloadPcBtn = QPushButton(self.sectionButtonPc)
        self.openDownloadPcBtn.setObjectName(u"openDownloadPcBtn")
        self.openDownloadPcBtn.setMaximumSize(QSize(16777215, 115))
        self.openDownloadPcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openDownloadPcBtn.setIcon(icon8)
        self.openDownloadPcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.openDownloadPcBtn)

        self.openRecycleFolderPcBtn = QPushButton(self.sectionButtonPc)
        self.openRecycleFolderPcBtn.setObjectName(u"openRecycleFolderPcBtn")
        self.openRecycleFolderPcBtn.setMaximumSize(QSize(16777215, 115))
        self.openRecycleFolderPcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/trash-x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openRecycleFolderPcBtn.setIcon(icon9)
        self.openRecycleFolderPcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.openRecycleFolderPcBtn)

        self.problemSppPcBtn = QPushButton(self.sectionButtonPc)
        self.problemSppPcBtn.setObjectName(u"problemSppPcBtn")
        self.problemSppPcBtn.setMaximumSize(QSize(16777215, 115))
        self.problemSppPcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/headset.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.problemSppPcBtn.setIcon(icon10)
        self.problemSppPcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.problemSppPcBtn)


        self.verticalLayout_5.addWidget(self.sectionButtonPc)

        self.sectionQuestionPc = QFrame(self.mainSectionPc)
        self.sectionQuestionPc.setObjectName(u"sectionQuestionPc")
        self.sectionQuestionPc.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionPc.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.sectionQuestionPc)

        self.stackedWidget.addWidget(self.pagePC)
        self.pagePrint = QWidget()
        self.pagePrint.setObjectName(u"pagePrint")
        self.mainSectionPrint = QFrame(self.pagePrint)
        self.mainSectionPrint.setObjectName(u"mainSectionPrint")
        self.mainSectionPrint.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionPrint.setMinimumSize(QSize(0, 0))
        self.mainSectionPrint.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionPrint.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mainSectionPrint)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sectionTittlePrint = QFrame(self.mainSectionPrint)
        self.sectionTittlePrint.setObjectName(u"sectionTittlePrint")
        self.sectionTittlePrint.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittlePrint.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.sectionTittlePrint)

        self.sectionButtonPrint = QFrame(self.mainSectionPrint)
        self.sectionButtonPrint.setObjectName(u"sectionButtonPrint")
        self.sectionButtonPrint.setStyleSheet(u"#sectionButtonPrint > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionButtonPrint > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.sectionButtonPrint.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonPrint.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sectionButtonPrint)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.addPrinterPrintBtn = QPushButton(self.sectionButtonPrint)
        self.addPrinterPrintBtn.setObjectName(u"addPrinterPrintBtn")
        self.addPrinterPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.addPrinterPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/square-rounded-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addPrinterPrintBtn.setIcon(icon11)
        self.addPrinterPrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.addPrinterPrintBtn)

        self.myPrintersPrintBtn = QPushButton(self.sectionButtonPrint)
        self.myPrintersPrintBtn.setObjectName(u"myPrintersPrintBtn")
        self.myPrintersPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.myPrintersPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.myPrintersPrintBtn.setIcon(icon3)
        self.myPrintersPrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.myPrintersPrintBtn)

        self.cartridgePrintBtn = QPushButton(self.sectionButtonPrint)
        self.cartridgePrintBtn.setObjectName(u"cartridgePrintBtn")
        self.cartridgePrintBtn.setMaximumSize(QSize(16777215, 115))
        self.cartridgePrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cartridgePrintBtn.setIcon(icon10)
        self.cartridgePrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.cartridgePrintBtn)

        self.connectPrintBtn = QPushButton(self.sectionButtonPrint)
        self.connectPrintBtn.setObjectName(u"connectPrintBtn")
        self.connectPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.connectPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.connectPrintBtn.setIcon(icon10)
        self.connectPrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.connectPrintBtn)


        self.verticalLayout_7.addWidget(self.sectionButtonPrint)

        self.sectionQuestionPrint = QFrame(self.mainSectionPrint)
        self.sectionQuestionPrint.setObjectName(u"sectionQuestionPrint")
        self.sectionQuestionPrint.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionPrint.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.sectionQuestionPrint)

        self.stackedWidget.addWidget(self.pagePrint)
        self.pageDocument = QWidget()
        self.pageDocument.setObjectName(u"pageDocument")
        self.mainSectionDocument = QFrame(self.pageDocument)
        self.mainSectionDocument.setObjectName(u"mainSectionDocument")
        self.mainSectionDocument.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionDocument.setMinimumSize(QSize(0, 0))
        self.mainSectionDocument.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionDocument.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.mainSectionDocument)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.sectionTittleDocument = QFrame(self.mainSectionDocument)
        self.sectionTittleDocument.setObjectName(u"sectionTittleDocument")
        self.sectionTittleDocument.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittleDocument.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_10.addWidget(self.sectionTittleDocument)

        self.sectionButtonDocument = QFrame(self.mainSectionDocument)
        self.sectionButtonDocument.setObjectName(u"sectionButtonDocument")
        self.sectionButtonDocument.setStyleSheet(u"#sectionButtonDocument > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionButtonDocument > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.sectionButtonDocument.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonDocument.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.sectionButtonDocument)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.javaDocumentBtn = QPushButton(self.sectionButtonDocument)
        self.javaDocumentBtn.setObjectName(u"javaDocumentBtn")
        self.javaDocumentBtn.setMaximumSize(QSize(16777215, 115))
        self.javaDocumentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.javaDocumentBtn.setIcon(icon7)
        self.javaDocumentBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.javaDocumentBtn)

        self.citrixDocumentBtn = QPushButton(self.sectionButtonDocument)
        self.citrixDocumentBtn.setObjectName(u"citrixDocumentBtn")
        self.citrixDocumentBtn.setMaximumSize(QSize(16777215, 115))
        self.citrixDocumentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.citrixDocumentBtn.setIcon(icon8)
        self.citrixDocumentBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.citrixDocumentBtn)

        self.clearCitrixDocumentBtn = QPushButton(self.sectionButtonDocument)
        self.clearCitrixDocumentBtn.setObjectName(u"clearCitrixDocumentBtn")
        self.clearCitrixDocumentBtn.setMaximumSize(QSize(16777215, 115))
        self.clearCitrixDocumentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearCitrixDocumentBtn.setIcon(icon10)
        self.clearCitrixDocumentBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.clearCitrixDocumentBtn)


        self.verticalLayout_10.addWidget(self.sectionButtonDocument)

        self.sectionQuestionDocument = QFrame(self.mainSectionDocument)
        self.sectionQuestionDocument.setObjectName(u"sectionQuestionDocument")
        self.sectionQuestionDocument.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionDocument.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_10.addWidget(self.sectionQuestionDocument)

        self.stackedWidget.addWidget(self.pageDocument)
        self.pagePhishing = QWidget()
        self.pagePhishing.setObjectName(u"pagePhishing")
        self.mainSectionPhishing = QFrame(self.pagePhishing)
        self.mainSectionPhishing.setObjectName(u"mainSectionPhishing")
        self.mainSectionPhishing.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionPhishing.setMinimumSize(QSize(0, 0))
        self.mainSectionPhishing.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionPhishing.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.mainSectionPhishing)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sectionTittlePhishing = QFrame(self.mainSectionPhishing)
        self.sectionTittlePhishing.setObjectName(u"sectionTittlePhishing")
        self.sectionTittlePhishing.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittlePhishing.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_8.addWidget(self.sectionTittlePhishing)

        self.sectionButtonPhishing = QFrame(self.mainSectionPhishing)
        self.sectionButtonPhishing.setObjectName(u"sectionButtonPhishing")
        self.sectionButtonPhishing.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonPhishing.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.sectionButtonPhishing)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reportIbPhishingBtn = QPushButton(self.sectionButtonPhishing)
        self.reportIbPhishingBtn.setObjectName(u"reportIbPhishingBtn")
        self.reportIbPhishingBtn.setMaximumSize(QSize(16777215, 115))
        self.reportIbPhishingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reportIbPhishingBtn.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 2, 57, 1);\n"
"color: #fff;\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 55, 122);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/spy.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportIbPhishingBtn.setIcon(icon12)
        self.reportIbPhishingBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.reportIbPhishingBtn)

        self.teachIbCorsePhishingBtn = QPushButton(self.sectionButtonPhishing)
        self.teachIbCorsePhishingBtn.setObjectName(u"teachIbCorsePhishingBtn")
        self.teachIbCorsePhishingBtn.setMaximumSize(QSize(16777215, 115))
        self.teachIbCorsePhishingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teachIbCorsePhishingBtn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/school.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.teachIbCorsePhishingBtn.setIcon(icon13)
        self.teachIbCorsePhishingBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.teachIbCorsePhishingBtn)


        self.verticalLayout_8.addWidget(self.sectionButtonPhishing)

        self.sectionQuestionPhishing = QFrame(self.mainSectionPhishing)
        self.sectionQuestionPhishing.setObjectName(u"sectionQuestionPhishing")
        self.sectionQuestionPhishing.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionPhishing.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_8.addWidget(self.sectionQuestionPhishing)

        self.stackedWidget.addWidget(self.pagePhishing)
        self.pageVpn = QWidget()
        self.pageVpn.setObjectName(u"pageVpn")
        self.mainSectionVpn = QFrame(self.pageVpn)
        self.mainSectionVpn.setObjectName(u"mainSectionVpn")
        self.mainSectionVpn.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionVpn.setMinimumSize(QSize(0, 0))
        self.mainSectionVpn.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionVpn.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.mainSectionVpn)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sectionTittleVpn = QFrame(self.mainSectionVpn)
        self.sectionTittleVpn.setObjectName(u"sectionTittleVpn")
        self.sectionTittleVpn.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittleVpn.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.sectionTittleVpn)

        self.sectionButtonVpn = QFrame(self.mainSectionVpn)
        self.sectionButtonVpn.setObjectName(u"sectionButtonVpn")
        self.sectionButtonVpn.setStyleSheet(u"#sectionButtonVpn > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionButtonVpn > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.sectionButtonVpn.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonVpn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.sectionButtonVpn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bidRemoteVpnBtn = QPushButton(self.sectionButtonVpn)
        self.bidRemoteVpnBtn.setObjectName(u"bidRemoteVpnBtn")
        self.bidRemoteVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.bidRemoteVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bidRemoteVpnBtn.setIcon(icon10)
        self.bidRemoteVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.bidRemoteVpnBtn)

        self.problemVpnBtn = QPushButton(self.sectionButtonVpn)
        self.problemVpnBtn.setObjectName(u"problemVpnBtn")
        self.problemVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.problemVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.problemVpnBtn.setIcon(icon10)
        self.problemVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.problemVpnBtn)

        self.refreshVpnBtn = QPushButton(self.sectionButtonVpn)
        self.refreshVpnBtn.setObjectName(u"refreshVpnBtn")
        self.refreshVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.refreshVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/password.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshVpnBtn.setIcon(icon14)
        self.refreshVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.refreshVpnBtn)

        self.settingVpnBtn = QPushButton(self.sectionButtonVpn)
        self.settingVpnBtn.setObjectName(u"settingVpnBtn")
        self.settingVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.settingVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/device-desktop-share.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingVpnBtn.setIcon(icon15)
        self.settingVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.settingVpnBtn)


        self.verticalLayout_6.addWidget(self.sectionButtonVpn)

        self.sectionQuestionVpn = QFrame(self.mainSectionVpn)
        self.sectionQuestionVpn.setObjectName(u"sectionQuestionVpn")
        self.sectionQuestionVpn.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionVpn.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.sectionQuestionVpn)

        self.stackedWidget.addWidget(self.pageVpn)
        self.pageBrowser = QWidget()
        self.pageBrowser.setObjectName(u"pageBrowser")
        self.mainSectionBrowser = QFrame(self.pageBrowser)
        self.mainSectionBrowser.setObjectName(u"mainSectionBrowser")
        self.mainSectionBrowser.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionBrowser.setMinimumSize(QSize(0, 0))
        self.mainSectionBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionBrowser.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.mainSectionBrowser)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.sectionTittleBrowser = QFrame(self.mainSectionBrowser)
        self.sectionTittleBrowser.setObjectName(u"sectionTittleBrowser")
        self.sectionTittleBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittleBrowser.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.sectionTittleBrowser)

        self.sectionButtonBrowser = QFrame(self.mainSectionBrowser)
        self.sectionButtonBrowser.setObjectName(u"sectionButtonBrowser")
        self.sectionButtonBrowser.setStyleSheet(u"#sectionButtonBrowser > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionButtonBrowser > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.sectionButtonBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonBrowser.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.sectionButtonBrowser)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.edgeBrowserBtn = QPushButton(self.sectionButtonBrowser)
        self.edgeBrowserBtn.setObjectName(u"edgeBrowserBtn")
        self.edgeBrowserBtn.setMaximumSize(QSize(16777215, 115))
        self.edgeBrowserBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/brand-edge.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edgeBrowserBtn.setIcon(icon16)
        self.edgeBrowserBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.edgeBrowserBtn)

        self.firefoxBrowserBtn = QPushButton(self.sectionButtonBrowser)
        self.firefoxBrowserBtn.setObjectName(u"firefoxBrowserBtn")
        self.firefoxBrowserBtn.setMaximumSize(QSize(16777215, 115))
        self.firefoxBrowserBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/brand-firefox.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.firefoxBrowserBtn.setIcon(icon17)
        self.firefoxBrowserBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.firefoxBrowserBtn)

        self.yandexBrowserBtn = QPushButton(self.sectionButtonBrowser)
        self.yandexBrowserBtn.setObjectName(u"yandexBrowserBtn")
        self.yandexBrowserBtn.setMaximumSize(QSize(16777215, 115))
        self.yandexBrowserBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/xbox-y.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.yandexBrowserBtn.setIcon(icon18)
        self.yandexBrowserBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.yandexBrowserBtn)


        self.verticalLayout_11.addWidget(self.sectionButtonBrowser)

        self.sectionQuestionBrowser = QFrame(self.mainSectionBrowser)
        self.sectionQuestionBrowser.setObjectName(u"sectionQuestionBrowser")
        self.sectionQuestionBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionBrowser.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.sectionQuestionBrowser)

        self.stackedWidget.addWidget(self.pageBrowser)
        self.pageMail = QWidget()
        self.pageMail.setObjectName(u"pageMail")
        self.pageMail.setMinimumSize(QSize(0, 0))
        self.mainSectionMail = QFrame(self.pageMail)
        self.mainSectionMail.setObjectName(u"mainSectionMail")
        self.mainSectionMail.setGeometry(QRect(0, 0, 615, 380))
        self.mainSectionMail.setMinimumSize(QSize(0, 0))
        self.mainSectionMail.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSectionMail.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mainSectionMail)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.sectionTittleMail = QFrame(self.mainSectionMail)
        self.sectionTittleMail.setObjectName(u"sectionTittleMail")
        self.sectionTittleMail.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionTittleMail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.sectionTittleMail)

        self.sectionButtonMail = QFrame(self.mainSectionMail)
        self.sectionButtonMail.setObjectName(u"sectionButtonMail")
        self.sectionButtonMail.setStyleSheet(u"#sectionButtonMail > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionButtonMail > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.sectionButtonMail.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionButtonMail.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.sectionButtonMail)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.securityOutMailBtn = QPushButton(self.sectionButtonMail)
        self.securityOutMailBtn.setObjectName(u"securityOutMailBtn")
        self.securityOutMailBtn.setMaximumSize(QSize(16777215, 115))
        self.securityOutMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/mail-exclamation.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.securityOutMailBtn.setIcon(icon19)
        self.securityOutMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.securityOutMailBtn)

        self.runOutMailBtn = QPushButton(self.sectionButtonMail)
        self.runOutMailBtn.setObjectName(u"runOutMailBtn")
        self.runOutMailBtn.setMaximumSize(QSize(16777215, 115))
        self.runOutMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runOutMailBtn.setIcon(icon1)
        self.runOutMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.runOutMailBtn)

        self.fixOutMailBtn = QPushButton(self.sectionButtonMail)
        self.fixOutMailBtn.setObjectName(u"fixOutMailBtn")
        self.fixOutMailBtn.setMaximumSize(QSize(16777215, 115))
        self.fixOutMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/photo-x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fixOutMailBtn.setIcon(icon20)
        self.fixOutMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.fixOutMailBtn)

        self.signatureMailBtn = QPushButton(self.sectionButtonMail)
        self.signatureMailBtn.setObjectName(u"signatureMailBtn")
        self.signatureMailBtn.setMinimumSize(QSize(0, 0))
        self.signatureMailBtn.setMaximumSize(QSize(16777215, 115))
        self.signatureMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/signature.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.signatureMailBtn.setIcon(icon21)
        self.signatureMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.signatureMailBtn)


        self.verticalLayout_9.addWidget(self.sectionButtonMail)

        self.sectionQuestionMail = QFrame(self.mainSectionMail)
        self.sectionQuestionMail.setObjectName(u"sectionQuestionMail")
        self.sectionQuestionMail.setFrameShape(QFrame.Shape.StyledPanel)
        self.sectionQuestionMail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.sectionQuestionMail)

        self.stackedWidget.addWidget(self.pageMail)

        self.horizontalLayout.addWidget(self.mainBody)


        self.verticalLayout.addWidget(self.main)

        self.bottom = QWidget(self.centralwidget)
        self.bottom.setObjectName(u"bottom")

        self.verticalLayout.addWidget(self.bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"IT-\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a", None))
        self.failureBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0439 \u041f\u041a", None))
        self.mailBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.browserBtn.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u0430\u0443\u0437\u0435\u0440", None))
        self.printBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.documentBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443\u043c, 1C", None))
        self.phishingBtn.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0448\u0438\u043d\u0433", None))
        self.vpnBtn.setText(QCoreApplication.translate("MainWindow", u"VPN", None))
        self.clearCashePcBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u041a\u044d\u0448", None))
        self.openDownloadPcBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.openRecycleFolderPcBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u043e\u0440\u0437\u0438\u043d\u0443", None))
        self.problemSppPcBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f-\u043f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441 \u041f\u041a", None))
        self.addPrinterPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439\n"
"\u043f\u0440\u0438\u043d\u0442\u0435\u0440", None))
        self.myPrintersPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0438 \n"
"\u043f\u0440\u0438\u043d\u0442\u0435\u0440\u044b", None))
        self.cartridgePrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u0437\u0430\u043c\u0435\u043d\u0430\n"
"\u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0430", None))
        self.connectPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435\n"
"\u0441\u0435\u0442\u0435\u0432\u043e\u0433\u043e \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u0430", None))
        self.javaDocumentBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u044d\u0448 JAVA\n"
"\u0438 \u0411\u0440\u0430\u0443\u0437\u0435\u0440\u0430 EDGE", None))
        self.citrixDocumentBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u043a CITRIX\n"
"\u0434\u043b\u044f 1\u0421", None))
        self.clearCitrixDocumentBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f \u2014 \u0421\u0431\u0440\u043e\u0441 \u0441\u0435\u0441\u0441\u0438\u0438\n"
"1\u0421 CITRIX ", None))
        self.reportIbPhishingBtn.setText(QCoreApplication.translate("MainWindow", u"C\u043e\u043e\u0431\u0449\u0438\u0442\u044c\n"
"\u0432 \u0418\u0411", None))
        self.teachIbCorsePhishingBtn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441 \u043f\u043e\n"
"\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439\n"
"\u0431\u0437\u0435\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438", None))
        self.bidRemoteVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430\n"
" \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f", None))
        self.problemVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 \u043d\u0430\n"
"\u0443\u0434\u0430\u043b\u0451\u043d\u043a\u0435", None))
        self.refreshVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \n"
"\u0444\u0430\u043a\u0442\u043e\u0440\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438", None))
        self.settingVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u043e\u0433\u043e \n"
"\u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.edgeBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u2028\u043a\u044d\u0448 EDGE", None))
        self.firefoxBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u2028\u043a\u044d\u0448 FireFox", None))
        self.yandexBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u2028\u043a\u044d\u0448 Yandex Browser", None))
        self.securityOutMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a Outlook\n"
"\u0432 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435", None))
        self.runOutMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a Outlook\n"
"\u0432 \u043e\u0431\u044b\u0447\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435", None))
        self.fixOutMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0438\u043d\u0438\u0442\u044c \u0432\u043d\u0435\u0448\u043d\u0438\u0439\n"
"\u0432\u0438\u0434 Outlook", None))
        self.signatureMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435\n"
"\u043f\u043e\u0434\u043f\u0438\u0441\u0438", None))
    # retranslateUi

