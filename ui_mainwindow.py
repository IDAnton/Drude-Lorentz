# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_test.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

from mplwidget import MplWidget
from mplwidget2 import mplwidget2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1143, 799)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.MainVerticalLayout = QVBoxLayout()
        self.MainVerticalLayout.setObjectName(u"MainVerticalLayout")
        self.MainVerticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.MainVerticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ParametrsPages = QStackedWidget(self.centralwidget)
        self.ParametrsPages.setObjectName(u"ParametrsPages")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParametrsPages.sizePolicy().hasHeightForWidth())
        self.ParametrsPages.setSizePolicy(sizePolicy)
        self.ParametrsPages.setMaximumSize(QSize(350, 16777215))
        self.ParametrsPages.setCursor(QCursor(Qt.ArrowCursor))
        self.ParametrsPages.setFocusPolicy(Qt.WheelFocus)
        self.ParametrsPages.setAutoFillBackground(False)
        self.ParametrsPages.setFrameShape(QFrame.NoFrame)
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.ParamsVerticalLayout = QVBoxLayout(self.Page1)
        self.ParamsVerticalLayout.setObjectName(u"ParamsVerticalLayout")
        self.ParamsVerticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ParamsVerticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.MainParamsLayout = QFormLayout()
        self.MainParamsLayout.setObjectName(u"MainParamsLayout")
        self.MainParamsLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MainParamsLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.MainParamsLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.EpsilonLimitInput = QDoubleSpinBox(self.Page1)
        self.EpsilonLimitInput.setObjectName(u"EpsilonLimitInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EpsilonLimitInput.sizePolicy().hasHeightForWidth())
        self.EpsilonLimitInput.setSizePolicy(sizePolicy1)
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

        self.EpsilonLimitText = QLabel(self.Page1)
        self.EpsilonLimitText.setObjectName(u"EpsilonLimitText")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.EpsilonLimitText.setFont(font1)

        self.MainParamsLayout.setWidget(0, QFormLayout.FieldRole, self.EpsilonLimitText)

        self.W_RangeLayout = QHBoxLayout()
        self.W_RangeLayout.setObjectName(u"W_RangeLayout")
        self.W2_RangeInput = QDoubleSpinBox(self.Page1)
        self.W2_RangeInput.setObjectName(u"W2_RangeInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.W2_RangeInput.sizePolicy().hasHeightForWidth())
        self.W2_RangeInput.setSizePolicy(sizePolicy2)
        self.W2_RangeInput.setFont(font)
        self.W2_RangeInput.setLayoutDirection(Qt.LeftToRight)
        self.W2_RangeInput.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.W2_RangeInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.W2_RangeInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.W2_RangeInput.setDecimals(0)
        self.W2_RangeInput.setMaximum(9999.000000000000000)
        self.W2_RangeInput.setValue(4500.000000000000000)

        self.W_RangeLayout.addWidget(self.W2_RangeInput)

        self.RangeSpliterText = QLabel(self.Page1)
        self.RangeSpliterText.setObjectName(u"RangeSpliterText")
        font2 = QFont()
        font2.setPointSize(12)
        self.RangeSpliterText.setFont(font2)

        self.W_RangeLayout.addWidget(self.RangeSpliterText)

        self.W1_RangeInput = QDoubleSpinBox(self.Page1)
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

        self.W_RangeText = QLabel(self.Page1)
        self.W_RangeText.setObjectName(u"W_RangeText")
        self.W_RangeText.setFont(font)
        self.W_RangeText.setTextFormat(Qt.AutoText)

        self.MainParamsLayout.setWidget(1, QFormLayout.FieldRole, self.W_RangeText)

        self.ThicknessInput = QDoubleSpinBox(self.Page1)
        self.ThicknessInput.setObjectName(u"ThicknessInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ThicknessInput.sizePolicy().hasHeightForWidth())
        self.ThicknessInput.setSizePolicy(sizePolicy3)
        self.ThicknessInput.setFont(font)
        self.ThicknessInput.setLayoutDirection(Qt.LeftToRight)
        self.ThicknessInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ThicknessInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ThicknessInput.setDecimals(0)
        self.ThicknessInput.setMaximum(9999.000000000000000)
        self.ThicknessInput.setValue(1.000000000000000)

        self.MainParamsLayout.setWidget(2, QFormLayout.LabelRole, self.ThicknessInput)

        self.MembraneThicknessText = QLabel(self.Page1)
        self.MembraneThicknessText.setObjectName(u"MembraneThicknessText")
        self.MembraneThicknessText.setFont(font)

        self.MainParamsLayout.setWidget(2, QFormLayout.FieldRole, self.MembraneThicknessText)

        self.BoundCountInput = QSpinBox(self.Page1)
        self.BoundCountInput.setObjectName(u"BoundCountInput")
        self.BoundCountInput.setFont(font)
        self.BoundCountInput.setLayoutDirection(Qt.LeftToRight)
        self.BoundCountInput.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.BoundCountInput.setMinimum(0)
        self.BoundCountInput.setMaximum(10)
        self.BoundCountInput.setValue(0)

        self.MainParamsLayout.setWidget(3, QFormLayout.LabelRole, self.BoundCountInput)

        self.ChargeCountLabel = QLabel(self.Page1)
        self.ChargeCountLabel.setObjectName(u"ChargeCountLabel")
        self.ChargeCountLabel.setFont(font)

        self.MainParamsLayout.setWidget(3, QFormLayout.FieldRole, self.ChargeCountLabel)


        self.ParamsVerticalLayout.addLayout(self.MainParamsLayout)

        self.line = QFrame(self.Page1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.ParamsVerticalLayout.addWidget(self.line)

        self.ChargeComboBox = QComboBox(self.Page1)
        self.ChargeComboBox.addItem("")
        self.ChargeComboBox.setObjectName(u"ChargeComboBox")
        self.ChargeComboBox.setFont(font)
        self.ChargeComboBox.setLayoutDirection(Qt.LeftToRight)
        self.ChargeComboBox.setEditable(False)
        self.ChargeComboBox.setMaxVisibleItems(10)
        self.ChargeComboBox.setMaxCount(200)
        self.ChargeComboBox.setDuplicatesEnabled(False)

        self.ParamsVerticalLayout.addWidget(self.ChargeComboBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.NInputPow = QDoubleSpinBox(self.Page1)
        self.NInputPow.setObjectName(u"NInputPow")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.NInputPow.sizePolicy().hasHeightForWidth())
        self.NInputPow.setSizePolicy(sizePolicy4)
        self.NInputPow.setFont(font)
        self.NInputPow.setLayoutDirection(Qt.LeftToRight)
        self.NInputPow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NInputPow.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.NInputPow.setDecimals(0)
        self.NInputPow.setMinimum(1.000000000000000)
        self.NInputPow.setMaximum(23.000000000000000)
        self.NInputPow.setValue(11.000000000000000)

        self.horizontalLayout.addWidget(self.NInputPow)

        self.Npow = QLabel(self.Page1)
        self.Npow.setObjectName(u"Npow")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Npow.sizePolicy().hasHeightForWidth())
        self.Npow.setSizePolicy(sizePolicy5)
        self.Npow.setFont(font)
        self.Npow.setTextFormat(Qt.AutoText)
        self.Npow.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Npow)

        self.NInput = QDoubleSpinBox(self.Page1)
        self.NInput.setObjectName(u"NInput")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.NInput.sizePolicy().hasHeightForWidth())
        self.NInput.setSizePolicy(sizePolicy6)
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

        self.NLabel = QLabel(self.Page1)
        self.NLabel.setObjectName(u"NLabel")
        self.NLabel.setFont(font)
        self.NLabel.setStyleSheet(u"label->setText(\"<html><head/><body><p>U<span style=\"\" vertical-align:sub;\"\">ABC</span></p></body></html>\");\n"
"")

        self.horizontalLayout.addWidget(self.NLabel)


        self.ParamsVerticalLayout.addLayout(self.horizontalLayout)

        self.ChargeLayout = QFormLayout()
        self.ChargeLayout.setObjectName(u"ChargeLayout")
        self.ChargeLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.ChargeLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.ChargeLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.ChargeMassInput = QDoubleSpinBox(self.Page1)
        self.ChargeMassInput.setObjectName(u"ChargeMassInput")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.ChargeMassInput.sizePolicy().hasHeightForWidth())
        self.ChargeMassInput.setSizePolicy(sizePolicy7)
        self.ChargeMassInput.setFont(font)
        self.ChargeMassInput.setLayoutDirection(Qt.LeftToRight)
        self.ChargeMassInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ChargeMassInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ChargeMassInput.setDecimals(3)
        self.ChargeMassInput.setMaximum(10000.000000000000000)
        self.ChargeMassInput.setValue(1.000000000000000)

        self.ChargeLayout.setWidget(1, QFormLayout.LabelRole, self.ChargeMassInput)

        self.ChargeMassLabel = QLabel(self.Page1)
        self.ChargeMassLabel.setObjectName(u"ChargeMassLabel")
        self.ChargeMassLabel.setFont(font)

        self.ChargeLayout.setWidget(1, QFormLayout.FieldRole, self.ChargeMassLabel)

        self.GammaInput = QDoubleSpinBox(self.Page1)
        self.GammaInput.setObjectName(u"GammaInput")
        self.GammaInput.setFont(font)
        self.GammaInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.GammaInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.GammaInput.setMinimum(-99999.990000000005239)
        self.GammaInput.setMaximum(99999.990000000005239)
        self.GammaInput.setValue(30.000000000000000)

        self.ChargeLayout.setWidget(2, QFormLayout.LabelRole, self.GammaInput)

        self.GammaLabel = QLabel(self.Page1)
        self.GammaLabel.setObjectName(u"GammaLabel")
        self.GammaLabel.setFont(font)

        self.ChargeLayout.setWidget(2, QFormLayout.FieldRole, self.GammaLabel)

        self.EffectiveChargeLabel = QLabel(self.Page1)
        self.EffectiveChargeLabel.setObjectName(u"EffectiveChargeLabel")
        self.EffectiveChargeLabel.setFont(font)

        self.ChargeLayout.setWidget(3, QFormLayout.FieldRole, self.EffectiveChargeLabel)

        self.EffectiveChargeInput = QDoubleSpinBox(self.Page1)
        self.EffectiveChargeInput.setObjectName(u"EffectiveChargeInput")
        sizePolicy6.setHeightForWidth(self.EffectiveChargeInput.sizePolicy().hasHeightForWidth())
        self.EffectiveChargeInput.setSizePolicy(sizePolicy6)
        self.EffectiveChargeInput.setFont(font)
        self.EffectiveChargeInput.setLayoutDirection(Qt.LeftToRight)
        self.EffectiveChargeInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.EffectiveChargeInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.EffectiveChargeInput.setDecimals(3)
        self.EffectiveChargeInput.setMinimum(1.000000000000000)
        self.EffectiveChargeInput.setMaximum(4.000000000000000)

        self.ChargeLayout.setWidget(3, QFormLayout.LabelRole, self.EffectiveChargeInput)

        self.FreqLabel = QLabel(self.Page1)
        self.FreqLabel.setObjectName(u"FreqLabel")
        self.FreqLabel.setEnabled(True)
        self.FreqLabel.setFont(font)

        self.ChargeLayout.setWidget(4, QFormLayout.FieldRole, self.FreqLabel)

        self.FreqInput = QDoubleSpinBox(self.Page1)
        self.FreqInput.setObjectName(u"FreqInput")
        self.FreqInput.setFont(font)
        self.FreqInput.setLayoutDirection(Qt.LeftToRight)
        self.FreqInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.FreqInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.FreqInput.setDecimals(0)
        self.FreqInput.setMaximum(999999.000000000000000)
        self.FreqInput.setValue(1100.000000000000000)

        self.ChargeLayout.setWidget(4, QFormLayout.LabelRole, self.FreqInput)

        self.PlasmOmegaHintLabel = QLabel(self.Page1)
        self.PlasmOmegaHintLabel.setObjectName(u"PlasmOmegaHintLabel")
        self.PlasmOmegaHintLabel.setFont(font)

        self.ChargeLayout.setWidget(5, QFormLayout.FieldRole, self.PlasmOmegaHintLabel)

        self.PlasmOmegaText = QLabel(self.Page1)
        self.PlasmOmegaText.setObjectName(u"PlasmOmegaText")
        self.PlasmOmegaText.setFont(font)

        self.ChargeLayout.setWidget(5, QFormLayout.LabelRole, self.PlasmOmegaText)


        self.ParamsVerticalLayout.addLayout(self.ChargeLayout)

        self.line_2 = QFrame(self.Page1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.ParamsVerticalLayout.addWidget(self.line_2)

        self.GraphShowLayout = QVBoxLayout()
        self.GraphShowLayout.setObjectName(u"GraphShowLayout")
        self.ShowLabel = QLabel(self.Page1)
        self.ShowLabel.setObjectName(u"ShowLabel")
        self.ShowLabel.setFont(font)
        self.ShowLabel.setAlignment(Qt.AlignCenter)

        self.GraphShowLayout.addWidget(self.ShowLabel)

        self.GraphShowGridLayout = QGridLayout()
        self.GraphShowGridLayout.setObjectName(u"GraphShowGridLayout")
        self.ERealShowButton = QCheckBox(self.Page1)
        self.ERealShowButton.setObjectName(u"ERealShowButton")
        self.ERealShowButton.setFont(font)
        self.ERealShowButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ERealShowButton.setLayoutDirection(Qt.RightToLeft)
        self.ERealShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.ERealShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.ERealShowButton, 0, 3, 1, 1)

        self.EImgShowButton = QCheckBox(self.Page1)
        self.EImgShowButton.setObjectName(u"EImgShowButton")
        self.EImgShowButton.setFont(font)
        self.EImgShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.EImgShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.EImgShowButton, 0, 2, 1, 1)

        self.NShowButton = QCheckBox(self.Page1)
        self.NShowButton.setObjectName(u"NShowButton")
        self.NShowButton.setFont(font)
        self.NShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.NShowButton.setChecked(True)

        self.GraphShowGridLayout.addWidget(self.NShowButton, 0, 1, 1, 1)

        self.KShowButton = QCheckBox(self.Page1)
        self.KShowButton.setObjectName(u"KShowButton")
        self.KShowButton.setFont(font)
        self.KShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.KShowButton.setChecked(True)

        self.GraphShowGridLayout.addWidget(self.KShowButton, 0, 0, 1, 1)

        self.RShowButton = QCheckBox(self.Page1)
        self.RShowButton.setObjectName(u"RShowButton")
        self.RShowButton.setFont(font)
        self.RShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.RShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.RShowButton, 1, 3, 1, 1)

        self.PhiShowButton = QCheckBox(self.Page1)
        self.PhiShowButton.setObjectName(u"PhiShowButton")
        self.PhiShowButton.setFont(font)
        self.PhiShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.PhiShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.PhiShowButton, 1, 2, 1, 1)

        self.AlphaShowButton = QCheckBox(self.Page1)
        self.AlphaShowButton.setObjectName(u"AlphaShowButton")
        self.AlphaShowButton.setFont(font)
        self.AlphaShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.AlphaShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.AlphaShowButton, 1, 1, 1, 1)

        self.DShowButton = QCheckBox(self.Page1)
        self.DShowButton.setObjectName(u"DShowButton")
        self.DShowButton.setFont(font)
        self.DShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.DShowButton.setChecked(False)
        self.DShowButton.setAutoRepeat(False)

        self.GraphShowGridLayout.addWidget(self.DShowButton, 1, 0, 1, 1)

        self.TShowButton = QCheckBox(self.Page1)
        self.TShowButton.setObjectName(u"TShowButton")
        self.TShowButton.setFont(font)
        self.TShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.TShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.TShowButton, 2, 3, 1, 1)

        self.AShowButton = QCheckBox(self.Page1)
        self.AShowButton.setObjectName(u"AShowButton")
        self.AShowButton.setFont(font)
        self.AShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.AShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.AShowButton, 2, 2, 1, 1)

        self.ExpShowButton = QCheckBox(self.Page1)
        self.ExpShowButton.setObjectName(u"ExpShowButton")
        self.ExpShowButton.setFont(font)
        self.ExpShowButton.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.ExpShowButton.setChecked(False)

        self.GraphShowGridLayout.addWidget(self.ExpShowButton, 2, 1, 1, 1)


        self.GraphShowLayout.addLayout(self.GraphShowGridLayout)


        self.ParamsVerticalLayout.addLayout(self.GraphShowLayout)

        self.line_3 = QFrame(self.Page1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.ParamsVerticalLayout.addWidget(self.line_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ImportButton = QPushButton(self.Page1)
        self.ImportButton.setObjectName(u"ImportButton")

        self.horizontalLayout_2.addWidget(self.ImportButton)

        self.ExportButton = QPushButton(self.Page1)
        self.ExportButton.setObjectName(u"ExportButton")

        self.horizontalLayout_2.addWidget(self.ExportButton)


        self.ParamsVerticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ParamsVerticalLayout.addItem(self.verticalSpacer)

        self.ParametrsPages.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.ParametrsPages.addWidget(self.Page2)

        self.gridLayout.addWidget(self.ParametrsPages, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(-1, 17, -1, -1)
        self.Page2Button = QPushButton(self.centralwidget)
        self.Page2Button.setObjectName(u"Page2Button")

        self.horizontalLayout_5.addWidget(self.Page2Button)

        self.Page1Button = QPushButton(self.centralwidget)
        self.Page1Button.setObjectName(u"Page1Button")

        self.horizontalLayout_5.addWidget(self.Page1Button)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.GraphsPages = QStackedWidget(self.centralwidget)
        self.GraphsPages.setObjectName(u"GraphsPages")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.GraphsPages.sizePolicy().hasHeightForWidth())
        self.GraphsPages.setSizePolicy(sizePolicy8)
        self.GraphsPages.setSizeIncrement(QSize(1, 1))
        self.graph = MplWidget()
        self.graph.setObjectName(u"graph")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy9)
        self.graph.setMinimumSize(QSize(550, 550))
        self.GraphsPages.addWidget(self.graph)
        self.graph2 = mplwidget2()
        self.graph2.setObjectName(u"graph2")
        self.graph2.setMinimumSize(QSize(550, 550))
        self.GraphsPages.addWidget(self.graph2)

        self.gridLayout.addWidget(self.GraphsPages, 0, 2, 2, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.MainVerticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.MainVerticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ChargeComboBox.setCurrentIndex(0)
        self.GraphsPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.EpsilonLimitText.setText(QCoreApplication.translate("MainWindow", u"\u03b5 \u043f\u043b\u0435\u043d\u043a\u0438", None))
        self.RangeSpliterText.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.W_RangeText.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0447\u0430\u0441\u0442\u043e\u0442", None))
        self.MembraneThicknessText.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u043c\u0435\u043c\u0431\u0440\u0430\u043d\u044b", None))
        self.ChargeCountLabel.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u0437\u0430\u0440\u044f\u0434\u043e\u0432 ", None))
        self.ChargeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0439 \u0437\u0430\u0440\u044f\u0434", None))

        self.ChargeComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0439 \u0437\u0430\u0440\u044f\u0434", None))
        self.NInputPow.setSuffix("")
        self.Npow.setText(QCoreApplication.translate("MainWindow", u"\u2022 10 ^", None))
        self.NLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.ChargeMassLabel.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0441\u0430 \u0437\u0430\u0440\u044f\u0434\u0430", None))
        self.GammaLabel.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0442\u0443\u0445\u0430\u043d\u0438\u0435 \u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u0439", None))
        self.EffectiveChargeLabel.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0437\u0430\u0440\u044f\u0434 ", None))
        self.FreqLabel.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u0439", None))
        self.PlasmOmegaHintLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0437\u043c\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.PlasmOmegaText.setText("")
        self.ShowLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u043c\u044b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.ERealShowButton.setText(QCoreApplication.translate("MainWindow", u"\u03b5\u2019(\u03bd)", None))
        self.EImgShowButton.setText(QCoreApplication.translate("MainWindow", u"\u03b5\u2019\u2019(\u03bd)", None))
        self.NShowButton.setText(QCoreApplication.translate("MainWindow", u"n(\u03bd)", None))
        self.KShowButton.setText(QCoreApplication.translate("MainWindow", u"k(\u03bd)", None))
        self.RShowButton.setText(QCoreApplication.translate("MainWindow", u"R(\u03bd) ", None))
        self.PhiShowButton.setText(QCoreApplication.translate("MainWindow", u"\u03c6(\u03bd)", None))
        self.AlphaShowButton.setText(QCoreApplication.translate("MainWindow", u"\u03b1(v)", None))
        self.DShowButton.setText(QCoreApplication.translate("MainWindow", u"D(\u03bd)", None))
        self.TShowButton.setText(QCoreApplication.translate("MainWindow", u"T(\u03bd)", None))
        self.AShowButton.setText(QCoreApplication.translate("MainWindow", u"A(\u03bd)", None))
        self.ExpShowButton.setText(QCoreApplication.translate("MainWindow", u"exp(v)", None))
        self.ImportButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.ExportButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.Page2Button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435", None))
        self.Page1Button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

