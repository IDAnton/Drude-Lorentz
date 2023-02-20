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
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

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
        font = QFont()
        font.setPointSize(12)
        self.EpsilonLimitInput.setFont(font)
        self.EpsilonLimitInput.setLayoutDirection(Qt.LeftToRight)
        self.EpsilonLimitInput.setAutoFillBackground(False)
        self.EpsilonLimitInput.setWrapping(False)
        self.EpsilonLimitInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.EpsilonLimitInput.setDecimals(1)
        self.EpsilonLimitInput.setMaximum(100.000000000000000)
        self.EpsilonLimitInput.setValue(50.000000000000000)

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
        self.W2_RangeInput.setFont(font)
        self.W2_RangeInput.setLayoutDirection(Qt.LeftToRight)
        self.W2_RangeInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.W2_RangeInput.setDecimals(0)
        self.W2_RangeInput.setMaximum(9999.000000000000000)
        self.W2_RangeInput.setValue(4500.000000000000000)

        self.W_RangeLayout.addWidget(self.W2_RangeInput)

        self.RangeSpliterText = QLabel(self.centralwidget)
        self.RangeSpliterText.setObjectName(u"RangeSpliterText")
        self.RangeSpliterText.setFont(font)

        self.W_RangeLayout.addWidget(self.RangeSpliterText)

        self.W1_RangeInput = QDoubleSpinBox(self.centralwidget)
        self.W1_RangeInput.setObjectName(u"W1_RangeInput")
        self.W1_RangeInput.setFont(font)
        self.W1_RangeInput.setLayoutDirection(Qt.LeftToRight)
        self.W1_RangeInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.W1_RangeInput.setDecimals(0)
        self.W1_RangeInput.setMaximum(9999.000000000000000)
        self.W1_RangeInput.setValue(10.000000000000000)

        self.W_RangeLayout.addWidget(self.W1_RangeInput)


        self.MainParamsLayout.setLayout(1, QFormLayout.LabelRole, self.W_RangeLayout)

        self.W_RangeText = QLabel(self.centralwidget)
        self.W_RangeText.setObjectName(u"W_RangeText")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.W_RangeText.setFont(font2)
        self.W_RangeText.setTextFormat(Qt.AutoText)

        self.MainParamsLayout.setWidget(1, QFormLayout.FieldRole, self.W_RangeText)

        self.MembraneThicknessText = QLabel(self.centralwidget)
        self.MembraneThicknessText.setObjectName(u"MembraneThicknessText")
        self.MembraneThicknessText.setFont(font2)

        self.MainParamsLayout.setWidget(2, QFormLayout.FieldRole, self.MembraneThicknessText)

        self.ThicknessInput = QDoubleSpinBox(self.centralwidget)
        self.ThicknessInput.setObjectName(u"ThicknessInput")
        self.ThicknessInput.setFont(font)
        self.ThicknessInput.setLayoutDirection(Qt.LeftToRight)
        self.ThicknessInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ThicknessInput.setDecimals(0)
        self.ThicknessInput.setMaximum(99999.000000000000000)

        self.MainParamsLayout.setWidget(2, QFormLayout.LabelRole, self.ThicknessInput)


        self.ParamsVerticalLayout.addLayout(self.MainParamsLayout)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.ParamsVerticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.ParamsVerticalLayout.addWidget(self.pushButton_2)


        self.GraphHorizontalLayout.addLayout(self.ParamsVerticalLayout)

        self.graph = MplWidget(self.centralwidget)
        self.graph.setObjectName(u"graph")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setMinimumSize(QSize(200, 250))
        self.graph.setMaximumSize(QSize(16777215, 16777215))
        self.graph.setAcceptDrops(False)
        self.graph.setLayoutDirection(Qt.RightToLeft)
        self.graph.setAutoFillBackground(True)

        self.GraphHorizontalLayout.addWidget(self.graph)


        self.MainVerticalLayout.addLayout(self.GraphHorizontalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
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
        self.EpsilonLimitText.setText(QCoreApplication.translate("MainWindow", u"\u03b5 \u221e", None))
        self.RangeSpliterText.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.W_RangeText.setText(QCoreApplication.translate("MainWindow", u"\u03c9 range", None))
        self.MembraneThicknessText.setText(QCoreApplication.translate("MainWindow", u"Membrane thickness (nm)", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

