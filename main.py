import sys
import time
import numpy as np
import qdarkstyle
from PySide6 import QtWidgets, QtGui

from Data import Data, ELECTRON_MASS_GRAMS, MAX_MODES, ATOMIC_MASS_UNITS, ELECTRON_CHARGE
from utils import get_charge_name_list
from ui_mainwindow import Ui_MainWindow


try:  # icon
    from ctypes import windll  # Only exists on Windows.
    myappid = 'Drude-Lorentz.model.model.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Drude-Lorentz")
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        self.data = Data()  # initialize all variables
        self.update_data()  # calculate and update graphs
        self.sync_defaults()  # set default values to ui

        # global params
        self.EpsilonLimitInput.valueChanged.connect(self.update_epsilon)
        self.W1_RangeInput.valueChanged.connect(self.update_w_range)
        self.W2_RangeInput.valueChanged.connect(self.update_w_range)
        self.ThicknessInput.valueChanged.connect(self.update_thickness)
        self.BoundCountInput.valueChanged.connect(self.update_bound_count)

        # charge params
        self.ChargeComboBox.currentIndexChanged.connect(self.charge_selection)
        self.NInput.valueChanged.connect(self.update_charge)
        self.NInputPow.valueChanged.connect(self.update_charge)
        self.ChargeMassInput.valueChanged.connect(self.update_charge)
        self.GammaInput.valueChanged.connect(self.update_charge)
        self.EffectiveChargeInput.valueChanged.connect(self.update_charge)
        self.FreqInput.valueChanged.connect(self.update_charge)
        self.FreqInput.setVisible(False)
        self.FreqLabel.setVisible(False)

        # graph show buttons
        self.NShowButton.stateChanged.connect(lambda state: self.graph.N_n_plot.set_visible(state))
        self.NShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.KShowButton.stateChanged.connect(lambda state: self.graph.N_k_plot.set_visible(state))
        self.KShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.AlphaShowButton.stateChanged.connect(lambda state: self.graph.alpha.set_visible(state))
        self.AlphaShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.DShowButton.stateChanged.connect(lambda state: self.graph.D.set_visible(state))
        self.DShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.RShowButton.stateChanged.connect(lambda state: self.graph.R_12.set_visible(state))
        self.RShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.TShowButton.stateChanged.connect(lambda state: self.graph.T.set_visible(state))
        self.TShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.PhiShowButton.stateChanged.connect(lambda state: self.graph.phase.set_visible(state))
        self.PhiShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.AShowButton.stateChanged.connect(lambda state: self.graph.A.set_visible(state))
        self.AShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.ERealShowButton.stateChanged.connect(lambda state: self.graph.eps_.set_visible(state))
        self.ERealShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))
        self.EImgShowButton.stateChanged.connect(lambda state: self.graph.eps__.set_visible(state))
        self.EImgShowButton.stateChanged.connect(lambda: self.graph.update_plots(self.data, data_changed=False))

        self.ExportButton.clicked.connect(self.export_data)

        self.ignore_input = False

    def export_data(self):
        pass
        # directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        # if self.NShowButton.isChecked():
        #     np.savetxt(f"{directory}/N_n.txt", np.c_[self.data.w, self.data.N_n])
        # if self.KShowButton.isChecked():
        #     np.savetxt(f"{directory}/N_k.txt", np.c_[self.data.w, self.data.N_k])
        # if self.AlphaShowButton.isChecked():
        #     np.savetxt(f"{directory}/alpha.txt", np.c_[self.data.w, self.data.alpha])
        # if self.DShowButton.isChecked():
        #     np.savetxt(f"{directory}/D.txt", np.c_[self.data.w, self.data.D])

    def charge_selection(self):
        i = self.ChargeComboBox.currentIndex()
        self.ignore_input = True
        if i == 0:  # free charge selected
            self.FreqInput.setVisible(False)
            self.FreqLabel.setVisible(False)
            self.sync_defaults()  # restore free charge values
        elif i > 0:  # bound charge selected
            i = i - 1
            self.FreqInput.setVisible(True)
            self.FreqLabel.setVisible(True)
            # restore bond charge values
            self.NInput.setValue(float(str(self.data.bound_N[i]).split("e")[0]))
            self.NInputPow.setValue(float(str(self.data.bound_N[i]).split("e")[1][1:]))
            self.ChargeMassInput.setValue(self.data.bound_masses[i] / ATOMIC_MASS_UNITS)
            self.GammaInput.setValue(self.data.bound_gamma[i])
            self.EffectiveChargeInput.setValue(self.data.bound_effective_charges[i] / ELECTRON_CHARGE)
            self.FreqInput.setValue(self.data.bound_freq_vibration[i])
            self.PlasmOmegaText.setText(str(round(self.data.w_i_plasm[i], 3)))
        self.ignore_input = False

    def update_bound_count(self):
        charge_list = get_charge_name_list()
        if self.BoundCountInput.value() > self.data.bound_number:
            self.data.init_new_charge()
        self.data.bound_number = self.BoundCountInput.value()
        self.ChargeComboBox.clear()
        self.ChargeComboBox.addItems(charge_list[0:self.data.bound_number + 1])
        self.ChargeComboBox.setCurrentIndex(self.data.bound_number)
        self.update_data()

    def update_charge(self):
        if self.ignore_input:
            return
        i = self.ChargeComboBox.currentIndex()
        if i == 0:  # free charge selected
            self.data.free_gamma = self.GammaInput.value()
            self.data.free_mass = self.ChargeMassInput.value() * ELECTRON_MASS_GRAMS
            self.data.free_N = self.NInput.value() * np.power(10, self.NInputPow.value())
            self.data.free_charge = self.EffectiveChargeInput.value() * ELECTRON_CHARGE
            self.update_data()
            self.PlasmOmegaText.setText(str(round(self.data.w_plasm_0, 3)))
        else:  # bound charge selected
            i = i - 1
            self.data.bound_masses[i] = self.ChargeMassInput.value() * ATOMIC_MASS_UNITS
            self.data.bound_effective_charges[i] = self.EffectiveChargeInput.value() * ELECTRON_CHARGE
            self.data.bound_gamma[i] = self.GammaInput.value()
            self.data.bound_freq_vibration[i] = self.FreqInput.value()
            self.data.bound_N[i] = self.NInput.value() * np.power(10, self.NInputPow.value())
            self.update_data()
            self.PlasmOmegaText.setText(str(round(self.data.w_i_plasm[i], 3)))

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

    def sync_defaults(self):
        # sync base values
        self.EpsilonLimitInput.setValue(self.data.membrane_epsilon_limit)
        self.W1_RangeInput.setValue(self.data.w_range[0])
        self.W2_RangeInput.setValue(self.data.w_range[1])
        self.ThicknessInput.setValue(self.data.thickness)
        self.BoundCountInput.setValue(self.data.bound_number)
        # sync free charge values
        self.NInput.setValue(float(str(self.data.free_N).split("e")[0]))
        self.NInputPow.setValue(float(str(self.data.free_N).split("e")[1][1:]))
        self.ChargeMassInput.setValue(self.data.free_mass / ELECTRON_MASS_GRAMS)
        self.GammaInput.setValue(self.data.free_gamma)
        self.EffectiveChargeInput.setValue(self.data.free_charge)
        self.PlasmOmegaText.setText(str(round(self.data.w_plasm_0, 3)))


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
with open("style.css", "r") as file:
    app.setStyleSheet(file.read())
window = MainWindow()
window.showMaximized()
app.exec()
