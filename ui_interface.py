# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacetfEUhn.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 640)
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
"}\n"
"#sectionTittlePc {\n"
"    background-color: rgba(222, 118, 0, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#sectionTittleBrowser {\n"
"    background-color: rgba(222, 118, 0, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#sectionTittleMail {\n"
"    background-color: rgba(0, 122, 255, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#sectionTittlePrint {\n"
"    background-color: rgba(0, 122, 255, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#sectionTittleDocument {\n"
"    background-color: rgba(222, 1"
                        "18, 0, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#firtsTitleVpn {\n"
"    background-color: rgba(0, 122, 255, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#secondTitleVpn {\n"
"    background-color: rgba(222, 118, 0, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"#sectionTittlePhishing {\n"
"    background-color: rgba(255, 2, 57, 0.05);\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 80))
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
        self.informationField = QLabel(self.header)
        self.informationField.setObjectName(u"informationField")
        self.informationField.setGeometry(QRect(230, 40, 461, 22))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setWeight(QFont.DemiBold)
        self.informationField.setFont(font1)
        self.informationField.setStyleSheet(u"color: rgba(255, 2, 57, 1);\n"
"font-weight: 600;")
        self.informationField.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_30 = QLabel(self.header)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(750, 10, 81, 22))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setWeight(QFont.DemiBold)
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"color: rgba(24, 77, 229, 1);\n"
"font-weight: 600;")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_30.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_31 = QLabel(self.header)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(720, 10, 24, 24))
        self.label_31.setPixmap(QPixmap(u":/icons/icons/phone-call.svg"))
        self.label_31.setScaledContents(True)
        self.label_32 = QLabel(self.header)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(730, 40, 101, 22))
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"color: rgba(24, 77, 229, 1);\n"
"font-weight: 600;")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_32.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.header)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
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
        font3 = QFont()
        font3.setPointSize(10)
        self.failureBtn.setFont(font3)
        self.failureBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.failureBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/computer-err.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.failureBtn.setIcon(icon)
        self.failureBtn.setIconSize(QSize(24, 24))
        self.failureBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.failureBtn)

        self.mailBtn = QPushButton(self.frame)
        self.mailBtn.setObjectName(u"mailBtn")
        self.mailBtn.setFont(font3)
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
        self.browserBtn.setFont(font3)
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
        self.printBtn.setFont(font3)
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
        self.documentBtn.setFont(font3)
        self.documentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.documentBtn.setStyleSheet(u"QPushButton:hover {\n"
"font-size: 15px; \n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.documentBtn.setIcon(icon4)
        self.documentBtn.setIconSize(QSize(24, 24))
        self.documentBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.documentBtn)

        self.phishingBtn = QPushButton(self.frame)
        self.phishingBtn.setObjectName(u"phishingBtn")
        self.phishingBtn.setFont(font3)
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
        self.vpnBtn.setFont(font3)
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
        self.stackedWidget.setGeometry(QRect(9, 9, 664, 380))
        self.pagePC = QWidget()
        self.pagePC.setObjectName(u"pagePC")
        self.mainSectionPc = QWidget(self.pagePC)
        self.mainSectionPc.setObjectName(u"mainSectionPc")
        self.mainSectionPc.setGeometry(QRect(0, 0, 664, 380))
        self.mainSectionPc.setMinimumSize(QSize(664, 380))
        self.mainSectionPc.setMaximumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.mainSectionPc)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.sectionTittlePc = QWidget(self.mainSectionPc)
        self.sectionTittlePc.setObjectName(u"sectionTittlePc")
        self.sectionTittlePc.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.sectionTittlePc)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_2 = QWidget(self.sectionTittlePc)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 26))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 24, 24))
        self.label.setStyleSheet(u"text-align: center;")
        self.label.setPixmap(QPixmap(u":/icons/icons/alert-square-rounded.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setIndent(-1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 0, 141, 24))
        self.label_2.setFont(font1)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")

        self.verticalLayout_12.addWidget(self.widget_2)

        self.frame_3 = QFrame(self.sectionTittlePc)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-10, 0, 591, 51))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);\n"
"font-weight: 400;\n"
"padding-left: 35;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_12.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.sectionTittlePc)

        self.sectionButtonPc = QWidget(self.mainSectionPc)
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
        self.horizontalLayout_2 = QHBoxLayout(self.sectionButtonPc)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clearCashePcBtn = QPushButton(self.sectionButtonPc)
        self.clearCashePcBtn.setObjectName(u"clearCashePcBtn")
        self.clearCashePcBtn.setMaximumSize(QSize(16777215, 115))
        self.clearCashePcBtn.setFont(font3)
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
        self.openDownloadPcBtn.setFont(font3)
        self.openDownloadPcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openDownloadPcBtn.setToolTipDuration(-2)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openDownloadPcBtn.setIcon(icon8)
        self.openDownloadPcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.openDownloadPcBtn)

        self.openRecycleFolderPcBtn = QPushButton(self.sectionButtonPc)
        self.openRecycleFolderPcBtn.setObjectName(u"openRecycleFolderPcBtn")
        self.openRecycleFolderPcBtn.setMaximumSize(QSize(16777215, 115))
        self.openRecycleFolderPcBtn.setFont(font3)
        self.openRecycleFolderPcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openRecycleFolderPcBtn.setToolTipDuration(-3)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/trash-x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openRecycleFolderPcBtn.setIcon(icon9)
        self.openRecycleFolderPcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.openRecycleFolderPcBtn)

        self.problemSppPcBtn = QPushButton(self.sectionButtonPc)
        self.problemSppPcBtn.setObjectName(u"problemSppPcBtn")
        self.problemSppPcBtn.setMaximumSize(QSize(16777215, 115))
        self.problemSppPcBtn.setFont(font3)
        self.problemSppPcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/headset.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.problemSppPcBtn.setIcon(icon10)
        self.problemSppPcBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.problemSppPcBtn)


        self.verticalLayout_5.addWidget(self.sectionButtonPc)

        self.sectionQuestionPc = QWidget(self.mainSectionPc)
        self.sectionQuestionPc.setObjectName(u"sectionQuestionPc")
        self.sectionQuestionPc.setMaximumSize(QSize(16777215, 115))
        self.sectionQuestionPc.setToolTipDuration(-3)
        self.sectionQuestionPc.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.sectionQuestionPc)

        self.stackedWidget.addWidget(self.pagePC)
        self.pagePrint = QWidget()
        self.pagePrint.setObjectName(u"pagePrint")
        self.mainSectionPrint = QWidget(self.pagePrint)
        self.mainSectionPrint.setObjectName(u"mainSectionPrint")
        self.mainSectionPrint.setGeometry(QRect(0, 0, 664, 380))
        self.mainSectionPrint.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.mainSectionPrint)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.sectionTittlePrint = QWidget(self.mainSectionPrint)
        self.sectionTittlePrint.setObjectName(u"sectionTittlePrint")
        self.widget_7 = QWidget(self.sectionTittlePrint)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 40, 634, 72))
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 621, 61))
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setPointSize(12)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);\n"
"padding-left: 35;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.widget_8 = QWidget(self.sectionTittlePrint)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 10, 634, 26))
        self.widget_8.setMaximumSize(QSize(16777215, 26))
        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 24, 24))
        self.label_11.setStyleSheet(u"text-align: center;")
        self.label_11.setPixmap(QPixmap(u":/icons/icons/info-square-rounded.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setIndent(-1)
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 0, 281, 24))
        self.label_12.setFont(font1)
        self.label_12.setToolTipDuration(-1)
        self.label_12.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")

        self.verticalLayout_7.addWidget(self.sectionTittlePrint)

        self.sectionButtonPrint = QWidget(self.mainSectionPrint)
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
        self.horizontalLayout_4 = QHBoxLayout(self.sectionButtonPrint)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.addPrinterPrintBtn = QPushButton(self.sectionButtonPrint)
        self.addPrinterPrintBtn.setObjectName(u"addPrinterPrintBtn")
        self.addPrinterPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.addPrinterPrintBtn.setFont(font3)
        self.addPrinterPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/square-rounded-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addPrinterPrintBtn.setIcon(icon11)
        self.addPrinterPrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.addPrinterPrintBtn)

        self.myPrintersPrintBtn = QPushButton(self.sectionButtonPrint)
        self.myPrintersPrintBtn.setObjectName(u"myPrintersPrintBtn")
        self.myPrintersPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.myPrintersPrintBtn.setFont(font3)
        self.myPrintersPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.myPrintersPrintBtn.setIcon(icon3)
        self.myPrintersPrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.myPrintersPrintBtn)

        self.cartridgePrintBtn = QPushButton(self.sectionButtonPrint)
        self.cartridgePrintBtn.setObjectName(u"cartridgePrintBtn")
        self.cartridgePrintBtn.setMaximumSize(QSize(16777215, 115))
        self.cartridgePrintBtn.setFont(font3)
        self.cartridgePrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cartridgePrintBtn.setIcon(icon10)
        self.cartridgePrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.cartridgePrintBtn)

        self.connectPrintBtn = QPushButton(self.sectionButtonPrint)
        self.connectPrintBtn.setObjectName(u"connectPrintBtn")
        self.connectPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.connectPrintBtn.setFont(font3)
        self.connectPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.connectPrintBtn.setIcon(icon10)
        self.connectPrintBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.connectPrintBtn)


        self.verticalLayout_7.addWidget(self.sectionButtonPrint)

        self.sectionQuestionPrint = QWidget(self.mainSectionPrint)
        self.sectionQuestionPrint.setObjectName(u"sectionQuestionPrint")
        self.sectionQuestionPrint.setMaximumSize(QSize(16777215, 115))
        self.sectionQuestionPrint.setStyleSheet(u"#sectionQuestionPrint > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionQuestionPrint > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.problemScanPrintBtn = QPushButton(self.sectionQuestionPrint)
        self.problemScanPrintBtn.setObjectName(u"problemScanPrintBtn")
        self.problemScanPrintBtn.setGeometry(QRect(0, 0, 159, 115))
        self.problemScanPrintBtn.setMaximumSize(QSize(16777215, 115))
        self.problemScanPrintBtn.setFont(font3)
        self.problemScanPrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.problemScanPrintBtn.setIcon(icon10)
        self.problemScanPrintBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.sectionQuestionPrint)

        self.stackedWidget.addWidget(self.pagePrint)
        self.pageDocument = QWidget()
        self.pageDocument.setObjectName(u"pageDocument")
        self.mainSectionDocument = QWidget(self.pageDocument)
        self.mainSectionDocument.setObjectName(u"mainSectionDocument")
        self.mainSectionDocument.setGeometry(QRect(0, -11, 664, 380))
        self.mainSectionDocument.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.mainSectionDocument)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.sectionTittleDocument = QWidget(self.mainSectionDocument)
        self.sectionTittleDocument.setObjectName(u"sectionTittleDocument")
        sizePolicy.setHeightForWidth(self.sectionTittleDocument.sizePolicy().hasHeightForWidth())
        self.sectionTittleDocument.setSizePolicy(sizePolicy)
        self.sectionTittleDocument.setMinimumSize(QSize(0, 0))
        self.sectionTittleDocument.setMaximumSize(QSize(16777215, 16777215))
        self.widget_9 = QWidget(self.sectionTittleDocument)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(10, 20, 632, 26))
        self.widget_9.setMaximumSize(QSize(16777215, 26))
        self.widget_9.setStyleSheet(u"")
        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 24, 24))
        self.label_13.setStyleSheet(u"text-align: center;")
        self.label_13.setPixmap(QPixmap(u":/icons/icons/alert-square-rounded.svg"))
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13.setIndent(-1)
        self.label_14 = QLabel(self.widget_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 0, 591, 24))
        self.label_14.setFont(font4)
        self.label_14.setToolTipDuration(-1)
        self.label_14.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);\n"
"")
        self.widget_10 = QWidget(self.sectionTittleDocument)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(10, 60, 632, 51))
        self.widget_10.setMinimumSize(QSize(0, 51))
        self.widget_10.setMaximumSize(QSize(16777215, 26))
        self.widget_10.setStyleSheet(u"")
        self.label_15 = QLabel(self.widget_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 10, 24, 24))
        self.label_15.setStyleSheet(u"text-align: center;")
        self.label_15.setPixmap(QPixmap(u":/icons/icons/alert-square-rounded.svg"))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15.setIndent(-1)
        self.label_16 = QLabel(self.widget_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 0, 581, 51))
        self.label_16.setFont(font4)
        self.label_16.setToolTipDuration(-1)
        self.label_16.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);")

        self.verticalLayout_10.addWidget(self.sectionTittleDocument)

        self.sectionButtonDocument = QWidget(self.mainSectionDocument)
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

        self.sectionQuestionDocument = QWidget(self.mainSectionDocument)
        self.sectionQuestionDocument.setObjectName(u"sectionQuestionDocument")

        self.verticalLayout_10.addWidget(self.sectionQuestionDocument)

        self.stackedWidget.addWidget(self.pageDocument)
        self.pagePhishing = QWidget()
        self.pagePhishing.setObjectName(u"pagePhishing")
        self.mainSectionPhishing = QWidget(self.pagePhishing)
        self.mainSectionPhishing.setObjectName(u"mainSectionPhishing")
        self.mainSectionPhishing.setGeometry(QRect(0, 0, 664, 380))
        self.mainSectionPhishing.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.mainSectionPhishing)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 10, 0)
        self.sectionTittlePhishing = QWidget(self.mainSectionPhishing)
        self.sectionTittlePhishing.setObjectName(u"sectionTittlePhishing")
        self.widget_11 = QWidget(self.sectionTittlePhishing)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 10, 634, 26))
        self.widget_11.setMaximumSize(QSize(16777215, 26))
        self.label_17 = QLabel(self.widget_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 0, 24, 24))
        self.label_17.setStyleSheet(u"text-align: center;")
        self.label_17.setPixmap(QPixmap(u":/icons/icons/square-rounded-x.svg"))
        self.label_17.setScaledContents(True)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17.setIndent(-1)
        self.label_18 = QLabel(self.widget_11)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 0, 491, 24))
        self.label_18.setFont(font1)
        self.label_18.setToolTipDuration(-1)
        self.label_18.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.frame_12 = QFrame(self.sectionTittlePhishing)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 40, 631, 74))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_19 = QLabel(self.frame_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 0, 311, 44))
        self.label_19.setFont(font5)
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 40, 266, 24))
        self.label_20.setFont(font5)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(280, 40, 99, 24))
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: rgba(24, 77, 229, 1);")
        self.label_21.setFrameShape(QFrame.Shape.NoFrame)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21.setOpenExternalLinks(False)
        self.label_21.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_8.addWidget(self.sectionTittlePhishing)

        self.sectionButtonPhishing = QWidget(self.mainSectionPhishing)
        self.sectionButtonPhishing.setObjectName(u"sectionButtonPhishing")
        self.horizontalLayout_5 = QHBoxLayout(self.sectionButtonPhishing)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
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

        self.sectionQuestionPhishing = QWidget(self.mainSectionPhishing)
        self.sectionQuestionPhishing.setObjectName(u"sectionQuestionPhishing")

        self.verticalLayout_8.addWidget(self.sectionQuestionPhishing)

        self.stackedWidget.addWidget(self.pagePhishing)
        self.pageVpn = QWidget()
        self.pageVpn.setObjectName(u"pageVpn")
        self.mainSectionVpn = QWidget(self.pageVpn)
        self.mainSectionVpn.setObjectName(u"mainSectionVpn")
        self.mainSectionVpn.setGeometry(QRect(0, 0, 664, 387))
        self.mainSectionVpn.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.mainSectionVpn)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.sectionTittleVpn = QWidget(self.mainSectionVpn)
        self.sectionTittleVpn.setObjectName(u"sectionTittleVpn")
        self.firtsTitleVpn = QWidget(self.sectionTittleVpn)
        self.firtsTitleVpn.setObjectName(u"firtsTitleVpn")
        self.firtsTitleVpn.setGeometry(QRect(0, 0, 650, 91))
        self.widget_12 = QWidget(self.firtsTitleVpn)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(0, 0, 621, 39))
        self.widget_12.setMinimumSize(QSize(0, 39))
        self.widget_12.setMaximumSize(QSize(16777215, 0))
        self.label_22 = QLabel(self.widget_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 24, 24))
        self.label_22.setStyleSheet(u"text-align: center;")
        self.label_22.setPixmap(QPixmap(u":/icons/icons/info-square-rounded.svg"))
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22.setIndent(-1)
        self.label_23 = QLabel(self.widget_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 10, 281, 24))
        self.label_23.setFont(font1)
        self.label_23.setToolTipDuration(-1)
        self.label_23.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.label_24 = QLabel(self.firtsTitleVpn)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(40, 40, 581, 43))
        self.label_24.setFont(font5)
        self.secondTitleVpn = QWidget(self.sectionTittleVpn)
        self.secondTitleVpn.setObjectName(u"secondTitleVpn")
        self.secondTitleVpn.setGeometry(QRect(0, 100, 650, 113))
        self.widget_13 = QWidget(self.secondTitleVpn)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(0, 0, 621, 35))
        self.widget_13.setMinimumSize(QSize(0, 35))
        self.widget_13.setMaximumSize(QSize(16777215, 0))
        self.label_25 = QLabel(self.widget_13)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 24, 24))
        self.label_25.setStyleSheet(u"text-align: center;")
        self.label_25.setPixmap(QPixmap(u":/icons/icons/alert-square-rounded.svg"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25.setIndent(-1)
        self.label_26 = QLabel(self.widget_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(40, 10, 281, 24))
        self.label_26.setFont(font1)
        self.label_26.setToolTipDuration(-1)
        self.label_26.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.label_27 = QLabel(self.secondTitleVpn)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 40, 611, 65))
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.sectionTittleVpn)

        self.sectionButtonVpn = QWidget(self.mainSectionVpn)
        self.sectionButtonVpn.setObjectName(u"sectionButtonVpn")
        self.sectionButtonVpn.setMaximumSize(QSize(16777215, 90))
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
        self.horizontalLayout_3 = QHBoxLayout(self.sectionButtonVpn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bidRemoteVpnBtn = QPushButton(self.sectionButtonVpn)
        self.bidRemoteVpnBtn.setObjectName(u"bidRemoteVpnBtn")
        self.bidRemoteVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.bidRemoteVpnBtn.setFont(font3)
        self.bidRemoteVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bidRemoteVpnBtn.setIcon(icon10)
        self.bidRemoteVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.bidRemoteVpnBtn)

        self.problemVpnBtn = QPushButton(self.sectionButtonVpn)
        self.problemVpnBtn.setObjectName(u"problemVpnBtn")
        self.problemVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.problemVpnBtn.setFont(font3)
        self.problemVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.problemVpnBtn.setIcon(icon10)
        self.problemVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.problemVpnBtn)

        self.refreshVpnBtn = QPushButton(self.sectionButtonVpn)
        self.refreshVpnBtn.setObjectName(u"refreshVpnBtn")
        self.refreshVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.refreshVpnBtn.setFont(font3)
        self.refreshVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/password.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshVpnBtn.setIcon(icon14)
        self.refreshVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.refreshVpnBtn)

        self.settingVpnBtn = QPushButton(self.sectionButtonVpn)
        self.settingVpnBtn.setObjectName(u"settingVpnBtn")
        self.settingVpnBtn.setMaximumSize(QSize(16777215, 115))
        self.settingVpnBtn.setFont(font3)
        self.settingVpnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/device-desktop-share.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingVpnBtn.setIcon(icon15)
        self.settingVpnBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.settingVpnBtn)


        self.verticalLayout_6.addWidget(self.sectionButtonVpn)

        self.sectionQuestionVpn = QWidget(self.mainSectionVpn)
        self.sectionQuestionVpn.setObjectName(u"sectionQuestionVpn")
        self.sectionQuestionVpn.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_6.addWidget(self.sectionQuestionVpn)

        self.stackedWidget.addWidget(self.pageVpn)
        self.pageBrowser = QWidget()
        self.pageBrowser.setObjectName(u"pageBrowser")
        self.mainSectionBrowser = QWidget(self.pageBrowser)
        self.mainSectionBrowser.setObjectName(u"mainSectionBrowser")
        self.mainSectionBrowser.setGeometry(QRect(0, 0, 664, 380))
        self.mainSectionBrowser.setMinimumSize(QSize(0, 0))
        self.verticalLayout_11 = QVBoxLayout(self.mainSectionBrowser)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 10, 0)
        self.sectionTittleBrowser = QWidget(self.mainSectionBrowser)
        self.sectionTittleBrowser.setObjectName(u"sectionTittleBrowser")
        self.sectionTittleBrowser.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.sectionTittleBrowser)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_5 = QWidget(self.sectionTittleBrowser)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 26))
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 24, 24))
        self.label_7.setStyleSheet(u"text-align: center;")
        self.label_7.setPixmap(QPixmap(u":/icons/icons/alert-square-rounded.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setIndent(-1)
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 0, 141, 20))
        self.label_8.setFont(font1)
        self.label_8.setToolTipDuration(-1)
        self.label_8.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")

        self.verticalLayout_14.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.sectionTittleBrowser)
        self.widget_6.setObjectName(u"widget_6")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(-10, 0, 591, 24))
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);\n"
"padding-left: 35;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_14.addWidget(self.widget_6)


        self.verticalLayout_11.addWidget(self.sectionTittleBrowser)

        self.sectionButtonBrowser = QWidget(self.mainSectionBrowser)
        self.sectionButtonBrowser.setObjectName(u"sectionButtonBrowser")
        self.sectionButtonBrowser.setMaximumSize(QSize(16777215, 16777215))
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

        self.sectionQuestionBrowser = QWidget(self.mainSectionBrowser)
        self.sectionQuestionBrowser.setObjectName(u"sectionQuestionBrowser")

        self.verticalLayout_11.addWidget(self.sectionQuestionBrowser)

        self.stackedWidget.addWidget(self.pageBrowser)
        self.pageMail = QWidget()
        self.pageMail.setObjectName(u"pageMail")
        self.pageMail.setMinimumSize(QSize(0, 0))
        self.mainSectionMail = QWidget(self.pageMail)
        self.mainSectionMail.setObjectName(u"mainSectionMail")
        self.mainSectionMail.setGeometry(QRect(0, 0, 664, 380))
        self.mainSectionMail.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.mainSectionMail)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 10, 0)
        self.sectionTittleMail = QWidget(self.mainSectionMail)
        self.sectionTittleMail.setObjectName(u"sectionTittleMail")
        self.sectionTittleMail.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.sectionTittleMail)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_4 = QWidget(self.sectionTittleMail)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 26))
        self.widget_4.setStyleSheet(u"")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 24, 24))
        self.label_5.setStyleSheet(u"text-align: center;")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/info-square-rounded.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setIndent(-1)
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 0, 491, 24))
        self.label_6.setFont(font4)
        self.label_6.setToolTipDuration(-1)
        self.label_6.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);\n"
"font-weight: 400;")
        self.label_6.setLineWidth(1)

        self.verticalLayout_13.addWidget(self.widget_4)


        self.verticalLayout_9.addWidget(self.sectionTittleMail)

        self.sectionButtonMail = QWidget(self.mainSectionMail)
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
        self.horizontalLayout_6 = QHBoxLayout(self.sectionButtonMail)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.securityOutMailBtn = QPushButton(self.sectionButtonMail)
        self.securityOutMailBtn.setObjectName(u"securityOutMailBtn")
        self.securityOutMailBtn.setMaximumSize(QSize(16777215, 115))
        self.securityOutMailBtn.setFont(font3)
        self.securityOutMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/mail-exclamation.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.securityOutMailBtn.setIcon(icon19)
        self.securityOutMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.securityOutMailBtn)

        self.runOutMailBtn = QPushButton(self.sectionButtonMail)
        self.runOutMailBtn.setObjectName(u"runOutMailBtn")
        self.runOutMailBtn.setMaximumSize(QSize(16777215, 115))
        self.runOutMailBtn.setFont(font3)
        self.runOutMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runOutMailBtn.setStyleSheet(u"")
        self.runOutMailBtn.setIcon(icon1)
        self.runOutMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.runOutMailBtn)

        self.fixOutMailBtn = QPushButton(self.sectionButtonMail)
        self.fixOutMailBtn.setObjectName(u"fixOutMailBtn")
        self.fixOutMailBtn.setMaximumSize(QSize(16777215, 115))
        self.fixOutMailBtn.setFont(font3)
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
        self.signatureMailBtn.setFont(font3)
        self.signatureMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/signature.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.signatureMailBtn.setIcon(icon21)
        self.signatureMailBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.signatureMailBtn)


        self.verticalLayout_9.addWidget(self.sectionButtonMail)

        self.sectionQuestionMail = QWidget(self.mainSectionMail)
        self.sectionQuestionMail.setObjectName(u"sectionQuestionMail")
        self.sectionQuestionMail.setMaximumSize(QSize(16777215, 115))
        self.sectionQuestionMail.setStyleSheet(u"#sectionQuestionMail > QPushButton {\n"
"border: 1px solid rgba(21, 33, 73, 0.1);\n"
"text-align: center;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"#sectionQuestionMail > QPushButton:hover {\n"
"background-color: rgba(26, 51, 115, 0.05);\n"
"color: rgba(21, 33, 73, 1);\n"
"}")
        self.archiveMailBtn = QPushButton(self.sectionQuestionMail)
        self.archiveMailBtn.setObjectName(u"archiveMailBtn")
        self.archiveMailBtn.setGeometry(QRect(0, 0, 159, 115))
        self.archiveMailBtn.setMaximumSize(QSize(16777215, 115))
        self.archiveMailBtn.setFont(font3)
        self.archiveMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.archiveMailBtn.setStyleSheet(u"")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/mail-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.archiveMailBtn.setIcon(icon22)
        self.archiveMailBtn.setIconSize(QSize(20, 20))
        self.autoReplayMailBtn = QPushButton(self.sectionQuestionMail)
        self.autoReplayMailBtn.setObjectName(u"autoReplayMailBtn")
        self.autoReplayMailBtn.setGeometry(QRect(166, 0, 159, 115))
        self.autoReplayMailBtn.setMaximumSize(QSize(16777215, 115))
        self.autoReplayMailBtn.setFont(font3)
        self.autoReplayMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.autoReplayMailBtn.setStyleSheet(u"")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/answer.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.autoReplayMailBtn.setIcon(icon23)
        self.autoReplayMailBtn.setIconSize(QSize(20, 20))
        self.offlineModeMailBtn = QPushButton(self.sectionQuestionMail)
        self.offlineModeMailBtn.setObjectName(u"offlineModeMailBtn")
        self.offlineModeMailBtn.setGeometry(QRect(330, 0, 159, 115))
        self.offlineModeMailBtn.setMaximumSize(QSize(16777215, 115))
        self.offlineModeMailBtn.setFont(font3)
        self.offlineModeMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.offlineModeMailBtn.setStyleSheet(u"")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/worldwide.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.offlineModeMailBtn.setIcon(icon24)
        self.offlineModeMailBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.sectionQuestionMail)

        self.stackedWidget.addWidget(self.pageMail)

        self.horizontalLayout.addWidget(self.mainBody)


        self.verticalLayout.addWidget(self.main)

        self.bottom = QWidget(self.centralwidget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMaximumSize(QSize(16777215, 112))
        self.horizontalLayout_9 = QHBoxLayout(self.bottom)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.bottom)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMaximumSize(QSize(150, 16777215))
        self.label_4 = QLabel(self.widget_41)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 0, 96, 106))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/logo_main.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setMargin(0)

        self.horizontalLayout_9.addWidget(self.widget_41)

        self.systemInfoBottom = QWidget(self.bottom)
        self.systemInfoBottom.setObjectName(u"systemInfoBottom")
        self.horizontalLayout_10 = QHBoxLayout(self.systemInfoBottom)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.blockInfoBottom = QWidget(self.systemInfoBottom)
        self.blockInfoBottom.setObjectName(u"blockInfoBottom")
        self.blockInfoBottom.setMaximumSize(QSize(16777215, 16777215))
        self.blockInformation = QWidget(self.blockInfoBottom)
        self.blockInformation.setObjectName(u"blockInformation")
        self.blockInformation.setGeometry(QRect(9, 10, 541, 91))
        self.blockInformation.setStyleSheet(u"#blockInformation {\n"
"    background-color: rgba(0, 122, 255, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.logoBottom = QLabel(self.blockInformation)
        self.logoBottom.setObjectName(u"logoBottom")
        self.logoBottom.setGeometry(QRect(10, 20, 24, 24))
        self.logoBottom.setMaximumSize(QSize(16777215, 16777215))
        self.logoBottom.setPixmap(QPixmap(u":/icons/icons/info-square-rounded.svg"))
        self.logoBottom.setScaledContents(True)
        self.logoBottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.userLabelBottom = QLabel(self.blockInformation)
        self.userLabelBottom.setObjectName(u"userLabelBottom")
        self.userLabelBottom.setGeometry(QRect(40, 20, 21, 21))
        self.userLabelBottom.setMinimumSize(QSize(0, 0))
        self.userLabelBottom.setMaximumSize(QSize(16777215, 16777215))
        self.userLabelBottom.setFont(font3)
        self.userLabelBottom.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);")
        self.userLabelBottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.userBottom = QLabel(self.blockInformation)
        self.userBottom.setObjectName(u"userBottom")
        self.userBottom.setGeometry(QRect(59, 20, 167, 22))
        self.userBottom.setMaximumSize(QSize(16777215, 16777215))
        self.userBottom.setFont(font2)
        self.userBottom.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.userBottom.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.userBottom.setMargin(0)
        self.userBottom.setIndent(7)
        self.userBottom.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.pcLabelBottom = QLabel(self.blockInformation)
        self.pcLabelBottom.setObjectName(u"pcLabelBottom")
        self.pcLabelBottom.setGeometry(QRect(230, 20, 24, 20))
        self.pcLabelBottom.setMaximumSize(QSize(16777215, 16777215))
        self.pcLabelBottom.setFont(font3)
        self.pcLabelBottom.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);")
        self.pcLabelBottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pcLabelBottom.setMargin(0)
        self.pcNameBottom = QLabel(self.blockInformation)
        self.pcNameBottom.setObjectName(u"pcNameBottom")
        self.pcNameBottom.setGeometry(QRect(250, 20, 121, 22))
        self.pcNameBottom.setMaximumSize(QSize(16777215, 16777215))
        self.pcNameBottom.setFont(font2)
        self.pcNameBottom.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.pcNameBottom.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pcNameBottom.setIndent(7)
        self.pcNameBottom.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.ipLabelBottom = QLabel(self.blockInformation)
        self.ipLabelBottom.setObjectName(u"ipLabelBottom")
        self.ipLabelBottom.setGeometry(QRect(370, 20, 61, 20))
        self.ipLabelBottom.setMaximumSize(QSize(16777215, 16777215))
        self.ipLabelBottom.setFont(font3)
        self.ipLabelBottom.setStyleSheet(u"color: rgba(21, 33, 73, 0.66);")
        self.ipLabelBottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ipBottom = QLabel(self.blockInformation)
        self.ipBottom.setObjectName(u"ipBottom")
        self.ipBottom.setGeometry(QRect(430, 20, 111, 22))
        self.ipBottom.setMaximumSize(QSize(16777215, 16777215))
        self.ipBottom.setFont(font2)
        self.ipBottom.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.ipBottom.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ipBottom.setIndent(7)
        self.ipBottom.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_28 = QLabel(self.blockInformation)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 50, 24, 24))
        self.label_28.setPixmap(QPixmap(u":/icons/icons/alert-square-rounded.svg"))
        self.label_28.setScaledContents(True)
        self.label_29 = QLabel(self.blockInformation)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(40, 50, 241, 22))
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")
        self.reloadInformation = QLabel(self.blockInformation)
        self.reloadInformation.setObjectName(u"reloadInformation")
        self.reloadInformation.setGeometry(QRect(290, 50, 121, 22))
        self.reloadInformation.setFont(font2)
        self.reloadInformation.setStyleSheet(u"color: rgba(21, 33, 73, 1);\n"
"font-weight: 600;")

        self.horizontalLayout_10.addWidget(self.blockInfoBottom)

        self.widget_21 = QWidget(self.systemInfoBottom)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(130, 16777215))
        self.portalSppBtn = QPushButton(self.widget_21)
        self.portalSppBtn.setObjectName(u"portalSppBtn")
        self.portalSppBtn.setGeometry(QRect(0, 40, 65, 28))
        self.portalSppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.portalSppBtn.setStyleSheet(u"color: rgba(24, 77, 229, 1);\n"
"font-weight: 600;")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/external-link.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.portalSppBtn.setIcon(icon25)
        self.portalSppBtn.setIconSize(QSize(24, 24))
        self.feedbackBtn = QPushButton(self.widget_21)
        self.feedbackBtn.setObjectName(u"feedbackBtn")
        self.feedbackBtn.setGeometry(QRect(80, 40, 35, 24))
        self.feedbackBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.feedbackBtn.setStyleSheet(u"color: rgba(24, 77, 229, 1);\n"
"font-weight: 600;")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/circle-heart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.feedbackBtn.setIcon(icon26)
        self.feedbackBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.widget_21)


        self.horizontalLayout_9.addWidget(self.systemInfoBottom)


        self.verticalLayout.addWidget(self.bottom)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"IT-\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a", None))
        self.informationField.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"700002-911", None))
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"8(495)739-21-41", None))
        self.failureBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0439 \u041f\u041a", None))
        self.mailBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.browserBtn.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u0430\u0443\u0437\u0435\u0440", None))
        self.printBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.documentBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443\u043c, 1C", None))
        self.phishingBtn.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0448\u0438\u043d\u0433", None))
        self.vpnBtn.setText(QCoreApplication.translate("MainWindow", u"VPN", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0437\u0430\u0431\u044b\u0432\u0430\u0439\u0442\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0436\u0430\u0442\u044c \u041f\u041a \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u0438\u00a0\u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f\n"
"\u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
#if QT_CONFIG(tooltip)
        self.clearCashePcBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432 \u041f\u041a, \u043d\u0435 \u043e\u0447\u0438\u0441\u0442\u043a\u0430 \u041a\u042d\u0428\u0430 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clearCashePcBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u041a\u044d\u0448", None))
#if QT_CONFIG(tooltip)
        self.openDownloadPcBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0434\u0430\u043b\u0438\u0442\u0435 \u0438\u0437 \u043d\u0435\u0435 \u0432\u0441\u0435 \u0442\u043e \u0447\u0442\u043e \u0432\u0430\u043c \u043d\u0435 \u043d\u0430\u0434\u043e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.openDownloadPcBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.openRecycleFolderPcBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u043e\u0440\u0437\u0438\u043d\u0443, n\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.openRecycleFolderPcBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u043e\u0440\u0437\u0438\u043d\u0443", None))
#if QT_CONFIG(tooltip)
        self.problemSppPcBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435 \u0421\u041f\u041f - \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0432 \u0440\u0430\u0431\u043e\u0442\u0435 \u041f\u041a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.problemSppPcBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f-\u043f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441 \u041f\u041a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0438 \u0437\u0430\u044f\u0432\u043a\u0438 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 P00-XXXX-YYYY, \n"
"\u0433\u0434\u0435 XXXX- \u043a\u043e\u0434 \u0444\u0438\u043b\u0438\u0430\u043b\u0430 \u0421\u041e\u0413\u0410\u0417, YYYY- \u043a\u043e\u0434 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430.\n"
"\u0415\u0441\u043b\u0438 \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u043e\u0432 \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u043b\u0441\u044f, \u043e\u0444\u043e\u0440\u043c\u0438\u0442\u0435 \u0437\u0430\u044f\u0432\u043a\u0443 \u0432 \u0421\u041f\u041f", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438 \u0432 \u0421\u041f\u041f", None))
#if QT_CONFIG(tooltip)
        self.addPrinterPrintBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u0438\u0437 \u043e\u0442\u043a\u0440\u044b\u0432\u0448\u0435\u0433\u043e\u0441\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u043d\u0443\u0436\u043d\u044b\u0439, \u0434\u0432\u043e\u0439\u043d\u044b\u043c \u043a\u043b\u0438\u043a\u043e\u043c \u043c\u044b\u0448\u043a\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addPrinterPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439\n"
"\u043f\u0440\u0438\u043d\u0442\u0435\u0440", None))
#if QT_CONFIG(tooltip)
        self.myPrintersPrintBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0441\u043f\u0438\u0441\u043e\u043a \u0432\u0430\u0448\u0438\u0445 \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u043e\u0432. \u0415\u0441\u043b\u0438 \u043d\u0430\u0434\u043e \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u043d\u0435\u043d\u0443\u0436\u043d\u044b\u0439, \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043f\u0440\u0430\u0432\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u043e\u0439 \u043c\u044b\u0448\u043a\u0438 \u0438 \u0432\u044b\u0431\u0438\u0440\u0438\u0442\u0435 '\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e'</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.myPrintersPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0438 \n"
"\u043f\u0440\u0438\u043d\u0442\u0435\u0440\u044b", None))
#if QT_CONFIG(tooltip)
        self.cartridgePrintBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435 \u0421\u041f\u041f - \u0417\u0430\u043c\u0435\u043d\u0430 \u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cartridgePrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u0437\u0430\u043c\u0435\u043d\u0430\n"
"\u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0430", None))
#if QT_CONFIG(tooltip)
        self.connectPrintBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435 \u0421\u041f\u041f - \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0441\u0435\u0442\u0435\u0432\u043e\u0433\u043e \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.connectPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435\n"
"\u0441\u0435\u0442\u0435\u0432\u043e\u0433\u043e \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u0430", None))
#if QT_CONFIG(tooltip)
        self.problemScanPrintBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435 \u0421\u041f\u041f - \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 \u0441 \u043f\u0435\u0447\u0430\u0442\u044c\u044e \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435\u043c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.problemScanPrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0430\n"
"\u0441 \u043f\u0435\u0447\u0430\u0442\u044c\u044e\n"
"\u0438 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435\u043c", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u043d\u0435 \u0432\u044b\u0433\u0440\u0443\u0436\u0430\u044e\u0442\u0441\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b, \u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u043c\u043e\u0447\u044c \u043e\u0447\u0438\u0441\u0442\u043a\u0430 \u043a\u044d\u0448\u0430 JAVA", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0437\u0430\u0431\u044b\u0432\u0430\u0439\u0442\u0435, \u0415\u0441\u043b\u0438 1\u0421 \u0441\u0442\u0430\u043b \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c, \u0432 \u0442.\u0447. \u0437\u0430\u0432\u0438\u0441\u0430\u0442\u044c, \n"
"\u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0435 CITRIX ", None))
#if QT_CONFIG(tooltip)
        self.javaDocumentBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043d\u043e\u043f\u043a\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442 \u041e\u0447\u0438\u0441\u0442\u043a\u0443 \u041a\u042d\u0428\u0430 JAVA \u0438 \u041a\u042d\u0428 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430 EDGE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.javaDocumentBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u044d\u0448 JAVA\n"
"\u0438 \u0411\u0440\u0430\u0443\u0437\u0435\u0440\u0430 EDGE", None))
#if QT_CONFIG(tooltip)
        self.citrixDocumentBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442 CITRIX</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.citrixDocumentBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u043a CITRIX\n"
"\u0434\u043b\u044f 1\u0421", None))
#if QT_CONFIG(tooltip)
        self.clearCitrixDocumentBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0421\u041f\u041f \u043f\u043e \u0441\u0431\u0440\u043e\u0441\u0443 \u0441\u0435\u0441\u0441\u0438\u0438 CITRIX \u0432\u0440\u0443\u0447\u043d\u0443\u044e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clearCitrixDocumentBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f \u2014 \u0421\u0431\u0440\u043e\u0441 \u0441\u0435\u0441\u0441\u0438\u0438\n"
"1\u0421 CITRIX ", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u043d\u043e! \u041f\u0440\u0438 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0438 \u043f\u043e\u0434\u043e\u0437\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043f\u0438\u0441\u0435\u043c:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u2014 \u041d\u0435 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0430\u043c!\n"
"\u2014 \u041d\u0435 \u043f\u0435\u0440\u0435\u0441\u044b\u043b\u0430\u0442\u044c \u043a\u043e\u043b\u043b\u0435\u0433\u0430\u043c!", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u2014 \u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043e\u043e\u0431\u0449\u0438\u0442\u044c \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443", None))
#if QT_CONFIG(accessibility)
        self.label_21.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"<a>inc@sogaz.ru</a>", None))
#endif // QT_CONFIG(accessibility)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"inc@sogaz.ru", None))
#if QT_CONFIG(tooltip)
        self.reportIbPhishingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043f\u0438\u0441\u044c\u043c\u0430 \u043d\u0430 \u0430\u0434\u0440\u0435\u0441 \u0418\u0411</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.reportIbPhishingBtn.setText(QCoreApplication.translate("MainWindow", u"C\u043e\u043e\u0431\u0449\u0438\u0442\u044c\n"
"\u0432 \u0418\u0411", None))
#if QT_CONFIG(tooltip)
        self.teachIbCorsePhishingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b \u0418\u0411</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.teachIbCorsePhishingBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c\n"
" \u0410\u041e \"\u0421\u041e\u0413\u0410\u0417\"", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"AnyConnect", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u043f\u0440\u043e\u0434\u0430\u0436 \u2014 RS3.SOGAZ.RU\u2028\u041b\u0438\u0447\u043d\u043e\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e \u2014 RS9.SOGAZ.RU", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f \u043a VPN", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u0438\u044f \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f.\n"
"\u0414\u0432\u0443\u0445\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u0443\u044e \u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044e (\u0432\u0442\u043e\u0440\u043e\u0439 \u0444\u0430\u043a\u0442\u043e\u0440) \u043d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0432 \u043e\u0444\u0438\u0441\u0435!\n"
"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 \u0432 \u0440\u0435\u0448\u0435\u043d\u0438\u0438 \u043f\u043e \u0437\u0430\u044f\u0432\u043a\u0435 \u0438 \u043d\u0438\u0436\u0435 \u043f\u043e \u043a\u043d\u043e\u043f\u043a\u0435", None))
#if QT_CONFIG(tooltip)
        self.bidRemoteVpnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435 \u0421\u041f\u041f - \u0443\u0434\u0430\u043b\u0435\u043d\u043a\u0430 \u0438 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bidRemoteVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430\n"
" \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f", None))
#if QT_CONFIG(tooltip)
        self.problemVpnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435 \u0421\u041f\u041f - \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 \u0441 \u0443\u0434\u0430\u043b\u0435\u043d\u043a\u043e\u0439</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.problemVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f - \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 \u043d\u0430\n"
"\u0443\u0434\u0430\u043b\u0451\u043d\u043a\u0435", None))
#if QT_CONFIG(tooltip)
        self.refreshVpnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u043f\u0438\u0441\u044c\u043c\u043e \u043d\u0430 \u0430\u0434\u0440\u0435\u0441 \u0421\u041f\u041f \u0434\u043b\u044f \u0441\u0431\u0440\u043e\u0441\u0430 2 \u0444\u0430\u043a\u0442\u043e\u0440\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.refreshVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \n"
"\u0444\u0430\u043a\u0442\u043e\u0440\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.settingVpnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f\u043c\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u043d\u0433\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingVpnBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u043e\u0433\u043e \n"
"\u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u0442\u0438\u0442\u0435 \u043a\u044d\u0448", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0441\u0442\u0430\u0431\u0438\u043b\u044c\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430", None))
#if QT_CONFIG(tooltip)
        self.edgeBrowserBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043a\u044d\u0448\u0430 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430 EDGE, \u0435\u0441\u043b\u0438 \u043d\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e \u0432\u044b\u0433\u0440\u0443\u0436\u0430\u044e\u0442\u0441\u044f \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b. \u0411\u0440\u0430\u0443\u0437\u0435\u0440 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0441\u044f \u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0442 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.edgeBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u2028\u043a\u044d\u0448 EDGE", None))
#if QT_CONFIG(tooltip)
        self.firefoxBrowserBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043a\u044d\u0448\u0430 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430 FireFox, \u0435\u0441\u043b\u0438 \u043d\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e \u0432\u044b\u0433\u0440\u0443\u0436\u0430\u044e\u0442\u0441\u044f \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b. \u0411\u0440\u0430\u0443\u0437\u0435\u0440 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0441\u044f \u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0442 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.firefoxBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u2028\u043a\u044d\u0448 FireFox", None))
#if QT_CONFIG(tooltip)
        self.yandexBrowserBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043a\u044d\u0448\u0430 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430 Yandex, \u0435\u0441\u043b\u0438 \u043d\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e \u0432\u044b\u0433\u0440\u0443\u0436\u0430\u044e\u0442\u0441\u044f \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b. \u0411\u0440\u0430\u0443\u0437\u0435\u0440 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0441\u044f \u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0442 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u043a\u043b\u0430\u0434\u043a\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.yandexBrowserBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u2028\u043a\u044d\u0448 Yandex Browser", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443, \u0447\u0442\u043e\u0431\u044b \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
#if QT_CONFIG(tooltip)
        self.securityOutMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043f\u043e\u0447\u0442\u0430 \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043b\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c\u0441\u044f \u0438\u043b\u0438 \u0437\u0430\u043f\u0443\u0441\u0442\u0438\u043b\u0430\u0441\u044c \u0441 \u043e\u0448\u0438\u0431\u043a\u0430\u043c\u0438. \u041f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u043d\u0430\u0436\u0430\u0442\u044c \u041e\u041a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.securityOutMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a Outlook\n"
"\u0432 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u043c\n"
"\u0440\u0435\u0436\u0438\u043c\u0435", None))
#if QT_CONFIG(tooltip)
        self.runOutMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u0432 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435, \u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442 Outlook \u0432 \u043e\u0431\u044b\u0447\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.runOutMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a Outlook\n"
"\u0432 \u043e\u0431\u044b\u0447\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435", None))
#if QT_CONFIG(tooltip)
        self.fixOutMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u042d\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0430 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442 \u0432\u0438\u0434 \u043f\u043e\u0447\u0442\u044b \u043d\u0430 \u043f\u0435\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439, \u043d\u043e \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u0437\u0430\u043a\u0440\u043e\u0439\u0442\u0435 Outlook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fixOutMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0438\u043d\u0438\u0442\u044c \u0432\u043d\u0435\u0448\u043d\u0438\u0439\n"
"\u0432\u0438\u0434 Outlook", None))
#if QT_CONFIG(tooltip)
        self.signatureMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0435\u0439 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0432 Outlook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.signatureMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435\n"
"\u043f\u043e\u0434\u043f\u0438\u0441\u0438", None))
#if QT_CONFIG(tooltip)
        self.sectionQuestionMail.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.archiveMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0435\u0439 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0430\u0440\u0445\u0438\u0432\u0430\u0446\u0438\u0438 \u0432 Outlook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.archiveMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f\n"
"\u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435\n"
"\u0430\u0440\u0445\u0438\u0432\u0430\u0446\u0438\u0438 \u0432\n"
"Outlook", None))
#if QT_CONFIG(tooltip)
        self.autoReplayMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0435\u0439 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 \u0430\u0432\u0442\u043e\u043e\u0442\u0432\u0435\u0442\u0430 \u0432 Outlook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autoReplayMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f\n"
"\u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435\n"
"\u0430\u0432\u0442\u043e\u043e\u0442\u0432\u0435\u0442\u0430 \u0432\n"
"Outlook", None))
#if QT_CONFIG(tooltip)
        self.offlineModeMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0435\u0439 \u043f\u043e \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044e \u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430 \u0432 Outlook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.offlineModeMailBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f\n"
"\u043f\u043e \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044e\n"
"\u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u043e\u0433\u043e\n"
"\u0440\u0435\u0436\u0438\u043c\u0430 \u0432 Outlook", None))
        self.label_4.setText("")
        self.logoBottom.setText("")
        self.userLabelBottom.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0417:", None))
        self.userBottom.setText(QCoreApplication.translate("MainWindow", u"Nalenkov.dmitry.K", None))
        self.pcLabelBottom.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041a:", None))
        self.pcNameBottom.setText(QCoreApplication.translate("MainWindow", u"W00-0000-0333", None))
        self.ipLabelBottom.setText(QCoreApplication.translate("MainWindow", u"IP-adress:", None))
        self.ipBottom.setText(QCoreApplication.translate("MainWindow", u"100.100.135.146", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u043d\u0435 \u043f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0436\u0430\u043b\u0441\u044f c :", None))
        self.reloadInformation.setText("")
#if QT_CONFIG(tooltip)
        self.portalSppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b \u0421\u041f\u041f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.portalSppBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u041f", None))
#if QT_CONFIG(tooltip)
        self.feedbackBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.feedbackBtn.setText("")
    # retranslateUi

