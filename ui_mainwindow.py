# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1106, 755)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.MainVerticalLayout = QVBoxLayout()
        self.MainVerticalLayout.setObjectName(u"MainVerticalLayout")
        self.MainVerticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.GraphHorizontalLayout = QHBoxLayout()
        self.GraphHorizontalLayout.setObjectName(u"GraphHorizontalLayout")
        self.ParamsVerticalLayout = QVBoxLayout()
        self.ParamsVerticalLayout.setObjectName(u"ParamsVerticalLayout")
        self.MainParamsLayout = QFormLayout()
        self.MainParamsLayout.setObjectName(u"MainParamsLayout")
        self.EpsilonLimitInput = QDoubleSpinBox(self.centralwidget)
        self.EpsilonLimitInput.setObjectName(u"EpsilonLimitInput")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EpsilonLimitInput.sizePolicy().hasHeightForWidth())
        self.EpsilonLimitInput.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.EpsilonLimitInput.setFont(font)
        self.EpsilonLimitInput.setLayoutDirection(Qt.LeftToRight)
        self.EpsilonLimitInput.setAutoFillBackground(False)
        self.EpsilonLimitInput.setWrapping(False)
        self.EpsilonLimitInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.EpsilonLimitInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.EpsilonLimitInput.setDecimals(1)
        self.EpsilonLimitInput.setMaximum(100.000000000000000)
        self.EpsilonLimitInput.setValue(2.000000000000000)

        self.MainParamsLayout.setWidget(0, QFormLayout.LabelRole, self.EpsilonLimitInput)

        self.EpsilonLimitText = QLabel(self.centralwidget)
        self.EpsilonLimitText.setObjectName(u"EpsilonLimitText")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.EpsilonLimitText.setFont(font1)

        self.MainParamsLayout.setWidget(0, QFormLayout.FieldRole, self.EpsilonLimitText)

        self.W_RangeLayout = QHBoxLayout()
        self.W_RangeLayout.setObjectName(u"W_RangeLayout")
        self.W2_RangeInput = QDoubleSpinBox(self.centralwidget)
        self.W2_RangeInput.setObjectName(u"W2_RangeInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.W2_RangeInput.sizePolicy().hasHeightForWidth())
        self.W2_RangeInput.setSizePolicy(sizePolicy1)
        self.W2_RangeInput.setFont(font)
        self.W2_RangeInput.setLayoutDirection(Qt.LeftToRight)
        self.W2_RangeInput.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.W2_RangeInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.W2_RangeInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.W2_RangeInput.setDecimals(0)
        self.W2_RangeInput.setMaximum(9999.000000000000000)
        self.W2_RangeInput.setValue(4500.000000000000000)

        self.W_RangeLayout.addWidget(self.W2_RangeInput)

        self.RangeSpliterText = QLabel(self.centralwidget)
        self.RangeSpliterText.setObjectName(u"RangeSpliterText")
        font2 = QFont()
        font2.setPointSize(12)
        self.RangeSpliterText.setFont(font2)

        self.W_RangeLayout.addWidget(self.RangeSpliterText)

        self.W1_RangeInput = QDoubleSpinBox(self.centralwidget)
        self.W1_RangeInput.setObjectName(u"W1_RangeInput")
        self.W1_RangeInput.setFont(font)
        self.W1_RangeInput.setLayoutDirection(Qt.LeftToRight)
        self.W1_RangeInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.W1_RangeInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.W1_RangeInput.setDecimals(0)
        self.W1_RangeInput.setMaximum(9999.000000000000000)
        self.W1_RangeInput.setValue(10.000000000000000)

        self.W_RangeLayout.addWidget(self.W1_RangeInput)


        self.MainParamsLayout.setLayout(1, QFormLayout.LabelRole, self.W_RangeLayout)

        self.W_RangeText = QLabel(self.centralwidget)
        self.W_RangeText.setObjectName(u"W_RangeText")
        self.W_RangeText.setFont(font)
        self.W_RangeText.setTextFormat(Qt.AutoText)

        self.MainParamsLayout.setWidget(1, QFormLayout.FieldRole, self.W_RangeText)

        self.ThicknessInput = QDoubleSpinBox(self.centralwidget)
        self.ThicknessInput.setObjectName(u"ThicknessInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ThicknessInput.sizePolicy().hasHeightForWidth())
        self.ThicknessInput.setSizePolicy(sizePolicy2)
        self.ThicknessInput.setFont(font)
        self.ThicknessInput.setLayoutDirection(Qt.LeftToRight)
        self.ThicknessInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ThicknessInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ThicknessInput.setDecimals(0)
        self.ThicknessInput.setMaximum(9999.000000000000000)
        self.ThicknessInput.setValue(1.000000000000000)

        self.MainParamsLayout.setWidget(2, QFormLayout.LabelRole, self.ThicknessInput)

        self.MembraneThicknessText = QLabel(self.centralwidget)
        self.MembraneThicknessText.setObjectName(u"MembraneThicknessText")
        self.MembraneThicknessText.setFont(font)

        self.MainParamsLayout.setWidget(2, QFormLayout.FieldRole, self.MembraneThicknessText)


        self.ParamsVerticalLayout.addLayout(self.MainParamsLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.ParamsVerticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.NInputPow = QDoubleSpinBox(self.centralwidget)
        self.NInputPow.setObjectName(u"NInputPow")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.NInputPow.sizePolicy().hasHeightForWidth())
        self.NInputPow.setSizePolicy(sizePolicy3)
        self.NInputPow.setFont(font)
        self.NInputPow.setLayoutDirection(Qt.LeftToRight)
        self.NInputPow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NInputPow.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.NInputPow.setDecimals(0)
        self.NInputPow.setMinimum(1.000000000000000)
        self.NInputPow.setMaximum(23.000000000000000)
        self.NInputPow.setValue(11.000000000000000)

        self.horizontalLayout.addWidget(self.NInputPow)

        self.Npow = QLabel(self.centralwidget)
        self.Npow.setObjectName(u"Npow")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Npow.sizePolicy().hasHeightForWidth())
        self.Npow.setSizePolicy(sizePolicy4)
        self.Npow.setFont(font)
        self.Npow.setTextFormat(Qt.AutoText)
        self.Npow.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Npow)

        self.NInput = QDoubleSpinBox(self.centralwidget)
        self.NInput.setObjectName(u"NInput")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.NInput.sizePolicy().hasHeightForWidth())
        self.NInput.setSizePolicy(sizePolicy5)
        self.NInput.setFont(font)
        self.NInput.setLayoutDirection(Qt.LeftToRight)
        self.NInput.setWrapping(False)
        self.NInput.setFrame(True)
        self.NInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.NInput.setProperty("showGroupSeparator", False)
        self.NInput.setDecimals(2)
        self.NInput.setMaximum(9.000000000000000)
        self.NInput.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.NInput)

        self.NLabel = QLabel(self.centralwidget)
        self.NLabel.setObjectName(u"NLabel")
        self.NLabel.setFont(font)
        self.NLabel.setStyleSheet(u"label->setText(\"<html><head/><body><p>U<span style=\"\" vertical-align:sub;\"\">ABC</span></p></body></html>\");\n"
"")

        self.horizontalLayout.addWidget(self.NLabel)


        self.ParamsVerticalLayout.addLayout(self.horizontalLayout)

        self.FreeChargeLayout = QFormLayout()
        self.FreeChargeLayout.setObjectName(u"FreeChargeLayout")
        self.ChargeMassInput = QDoubleSpinBox(self.centralwidget)
        self.ChargeMassInput.setObjectName(u"ChargeMassInput")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ChargeMassInput.sizePolicy().hasHeightForWidth())
        self.ChargeMassInput.setSizePolicy(sizePolicy6)
        self.ChargeMassInput.setFont(font)
        self.ChargeMassInput.setLayoutDirection(Qt.LeftToRight)
        self.ChargeMassInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ChargeMassInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ChargeMassInput.setDecimals(3)
        self.ChargeMassInput.setMaximum(10000.000000000000000)
        self.ChargeMassInput.setValue(1.000000000000000)

        self.FreeChargeLayout.setWidget(1, QFormLayout.LabelRole, self.ChargeMassInput)

        self.ChargeMassLabel = QLabel(self.centralwidget)
        self.ChargeMassLabel.setObjectName(u"ChargeMassLabel")
        self.ChargeMassLabel.setFont(font)

        self.FreeChargeLayout.setWidget(1, QFormLayout.FieldRole, self.ChargeMassLabel)

        self.GammaLabel = QLabel(self.centralwidget)
        self.GammaLabel.setObjectName(u"GammaLabel")
        self.GammaLabel.setFont(font)

        self.FreeChargeLayout.setWidget(2, QFormLayout.FieldRole, self.GammaLabel)

        self.GammaInput = QDoubleSpinBox(self.centralwidget)
        self.GammaInput.setObjectName(u"GammaInput")
        self.GammaInput.setFont(font)
        self.GammaInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.GammaInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.GammaInput.setMinimum(-99999.990000000005239)
        self.GammaInput.setMaximum(99999.990000000005239)
        self.GammaInput.setValue(30.000000000000000)

        self.FreeChargeLayout.setWidget(2, QFormLayout.LabelRole, self.GammaInput)


        self.ParamsVerticalLayout.addLayout(self.FreeChargeLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ParamsVerticalLayout.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.ParamsVerticalLayout.addWidget(self.pushButton_2)


        self.GraphHorizontalLayout.addLayout(self.ParamsVerticalLayout)

        self.graph = MplWidget(self.centralwidget)
        self.graph.setObjectName(u"graph")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy7)
        self.graph.setMinimumSize(QSize(200, 250))
        self.graph.setMaximumSize(QSize(16777215, 16777215))
        self.graph.setAcceptDrops(False)
        self.graph.setLayoutDirection(Qt.RightToLeft)
        self.graph.setAutoFillBackground(True)

        self.GraphHorizontalLayout.addWidget(self.graph)


        self.MainVerticalLayout.addLayout(self.GraphHorizontalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.MainVerticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.MainVerticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.EpsilonLimitText.setText(QCoreApplication.translate("MainWindow", u"\u03b5 \u043f\u043b\u0435\u043d\u043a\u0438", None))
        self.RangeSpliterText.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.W_RangeText.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0447\u0430\u0441\u0442\u043e\u0442", None))
        self.MembraneThicknessText.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u043c\u0435\u043c\u0431\u0440\u0430\u043d\u044b", None))
        self.NInputPow.setSuffix("")
        self.Npow.setText(QCoreApplication.translate("MainWindow", u"\u2022 10 ^", None))
        self.NLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.ChargeMassLabel.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0441\u0430 \u0437\u0430\u0440\u044f\u0434\u0430", None))
        self.GammaLabel.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0442\u0443\u0445\u0430\u043d\u0438\u0435 \u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u0439", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

