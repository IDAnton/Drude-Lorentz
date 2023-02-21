import sys
import time
import numpy as np
import qdarkstyle
from PySide6 import QtWidgets


from Data import Data, ELECTRON_MASS_GRAMS, MAX_MODES, ATOMIC_MASS_UNITS, ELECTRON_CHARGE
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

        self.BoundCountInput.valueChanged.connect(self.update_bound_count)

        self.NInput.valueChanged.connect(self.update_charge)
        self.NInputPow.valueChanged.connect(self.update_charge)

        self.ChargeMassInput.valueChanged.connect(self.update_charge)
        self.GammaInput.valueChanged.connect(self.update_charge)

    def update_bound_count(self):
        charge_list = ["Свободный заряд"]
        for i in range(0, MAX_MODES):
            charge_list.append(f"Связанный заряд №{i+1}")
        self.data.bound_number = self.BoundCountInput.value()
        self.ChargeComboBox.clear()
        self.ChargeComboBox.addItems(charge_list[0:self.data.bound_number+1])
        self.ChargeComboBox.setCurrentIndex(self.data.bound_number)

    def update_charge(self):
        i = self.ChargeComboBox.currentIndex()
        if i == 0:
            self.data.free_gamma = self.GammaInput.value()
            self.data.free_mass = self.ChargeMassInput.value() * ELECTRON_MASS_GRAMS
            self.data.free_N = self.NInput.value() * np.power(10, self.NInputPow.value())
        else:
            i = i - 1
            self.data.bound_masses[i] = self.ChargeMassInput.value() * ATOMIC_MASS_UNITS
            self.data.bound_effective_charges[i] = self.EffectiveChargeInput.value() * ELECTRON_CHARGE
            self.data.bound_gamma[i] = self.GammaInput.value()
            self.data.bound_freq_vibration[i] = self.FreqInput.value()
            self.data.bound_N = self.NInput.value() * np.power(10, self.NInputPow.value())
        self.update_data()


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
        #print("--- %s seconds ---" % (time.time() - start_time))


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
window = MainWindow()
window.showMaximized()
app.exec()
