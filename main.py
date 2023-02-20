import sys
import time
import numpy as np
import qdarkstyle
from PySide6 import QtWidgets
from Data import Data
from ui_mainwindow import Ui_MainWindow

from mplwidget import Canvas


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.data = Data()  # initialize all variables
        self.graph.update_plots(self.data)  # plot default graphs

        self.EpsilonLimitInput.valueChanged.connect(self.update_epsilon)
        self.W1_RangeInput.valueChanged.connect(self.update_w_range)
        self.W2_RangeInput.valueChanged.connect(self.update_w_range)
        self.ThicknessInput.valueChanged.connect(self.update_thickness)

    def update_epsilon(self):
        self.data.membrane_epsilon_limit = self.EpsilonLimitInput.value()
        self.update_data()

    def update_w_range(self):
        self.data.w_range = self.W1_RangeInput.value(), self.W2_RangeInput.value()
        self.data.update_w_range()
        self.update_data()

    def update_thickness(self):
        self.data.thickness = self.ThicknessInput.value()
        self.update_data()

    def update_data(self):
        start_time = time.time()
        self.data.calculate()
        self.graph.update_plots(self.data)
        print("--- %s seconds ---" % (time.time() - start_time))


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
window = MainWindow()
window.showMaximized()
app.exec()
