import sys, os, time
import numpy as np
from PySide6 import QtWidgets, QtGui

from Data import Data, ELECTRON_MASS_GRAMS, MAX_MODES, ATOMIC_MASS_UNITS, ELECTRON_CHARGE
from utils import get_charge_name_list
from ui_mainwindow import Ui_MainWindow

basedir = os.path.dirname(__file__)

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
        self.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "static", "icon.ico")))

        self.data = Data()  # initialize all variables
        self.update_data()  # calculate and update graphs
        self.sync_defaults()  # set default values to ui

        # Pages
        self.Page1Button.clicked.connect(self.page1pushed)
        self.Page2Button.clicked.connect(self.page2pushed)
        #self.Page2Button.clicked.connect(self.page2pushed)

        # global params
        self.EpsilonLimitInput.valueChanged.connect(self.update_epsilon)
        self.W1_RangeInput.valueChanged.connect(self.update_w_range)
        self.W2_RangeInput.valueChanged.connect(self.update_w_range)
        self.ThicknessInput.valueChanged.connect(self.update_thickness)
        self.BoundCountInput.valueChanged.connect(self.update_bound_count)
        self.N_media_n_input.valueChanged.connect(self.update_N_media)
        self.N_media_k_input.valueChanged.connect(self.update_N_media)

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
        self.NShowButton.stateChanged.connect(lambda state: self.graph.N_n_plot.set_visible(state))  # first page
        self.KShowButton.stateChanged.connect(lambda state: self.graph.N_k_plot.set_visible(state))
        self.AlphaShowButton.stateChanged.connect(lambda state: self.graph.alpha.set_visible(state))
        self.DShowButton.stateChanged.connect(lambda state: self.graph.D.set_visible(state))
        self.RShowButton.stateChanged.connect(lambda state: self.graph.R_12.set_visible(state))
        self.TShowButton.stateChanged.connect(lambda state: self.graph.T.set_visible(state))
        self.PhiShowButton.stateChanged.connect(lambda state: self.graph.phase.set_visible(state))
        self.AShowButton.stateChanged.connect(lambda state: self.graph.A.set_visible(state))
        self.ERealShowButton.stateChanged.connect(lambda state: self.graph.eps_.set_visible(state))
        self.EImgShowButton.stateChanged.connect(lambda state: self.graph.eps__.set_visible(state))
        self.ExpShowButton.stateChanged.connect(lambda state: self.graph.experimental.set_visible(state))
        self.RTE_waveShowButton.stateChanged.connect(lambda state: self.graph2.RTE_wave.set_visible(state))  # second page
        self.RTM_waveButton.stateChanged.connect(lambda state: self.graph2.RTM_wave.set_visible(state))
        self.TE_phaseShowButton.stateChanged.connect(lambda state: self.graph2.TE_phase_12.set_visible(state))
        self.TM_phaseShowButton.stateChanged.connect(lambda state: self.graph2.TM_phase_12.set_visible(state))
        self.RNP_waveShowButton.stateChanged.connect(lambda state: self.graph2.RNP_wave.set_visible(state))
        self.Exp2ShowButton.stateChanged.connect(lambda state: self.graph2.experimental.set_visible(state))
        for i in range(self.GraphShowGridLayout.count()):
            self.GraphShowGridLayout.itemAt(i).widget().stateChanged.connect(
                lambda: self.graph.update_plots(self.data, data_changed=False, redraw_legend=True))
        for i in range(self.GraphShowGridLayout_2.count()):
            self.GraphShowGridLayout_2.itemAt(i).widget().stateChanged.connect(
                lambda: self.graph2.update_plots(self.data, data_changed=False, redraw_legend=True))

        # import / export
        self.ExportButton.clicked.connect(lambda: self.export_data(self.graph))
        self.ImportButton.clicked.connect(lambda: self.import_data(self.ExpShowButton, self.graph))
        self.ExportButton2.clicked.connect(lambda: self.export_data(self.graph2))
        self.ImportButton2.clicked.connect(lambda: self.import_data(self.Exp2ShowButton, self.graph2))

        # angel
        self.AngelSlider.valueChanged.connect(lambda value: self.AngelSpinBox.setValue(value))
        self.AngelSpinBox.valueChanged.connect(lambda value: self.AngelSlider.setValue(value))
        self.AngelSpinBox.valueChanged.connect(self.update_angel)

        self.ignore_input = False

    def update_angel(self, value):
        self.data.angle = value * np.pi / 180
        self.update_data()

    def page1pushed(self):
        self.ParametrsPages.setCurrentWidget(self.Page1)
        self.GraphsPages.setCurrentWidget(self.graph)
        self.Page1Button.setStyleSheet("QPushButton#Page1Button {background-color: rgb(170, 170, 255)}")
        self.Page2Button.setStyleSheet("QPushButton#Page2Button {background-color: rgb('FBFBFBFF')}")

    def page2pushed(self):
        self.ParametrsPages.setCurrentWidget(self.Page2)
        self.GraphsPages.setCurrentWidget(self.graph2)
        self.Page2Button.setStyleSheet("QPushButton#Page2Button {background-color: rgb(170, 170, 255)}")
        self.Page1Button.setStyleSheet("QPushButton#Page1Button {background-color: rgb('FBFBFBFF')}")

    def import_data(self, ExpShowButton, graph):
        data_file = QtWidgets.QFileDialog.getOpenFileName()
        try:
            data = np.loadtxt(data_file[0])
            if ExpShowButton == self.ExpShowButton:
                self.data.experiment_x, self.data.experiment_y = np.hsplit(data, 2)
            if ExpShowButton == self.Exp2ShowButton:
                self.data.experiment2_x, self.data.experiment2_y = np.hsplit(data, 2)
        except ValueError as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка импорта", f"Файл содержит некорректные данные")
            return
        ExpShowButton.setEnabled(True)
        ExpShowButton.setChecked(True)
        graph.update_plots(self.data)

    def export_data(self, graph):
        showed_graphs = [line for line in graph.canvas.ax.get_lines() if line._visible]
        if len(showed_graphs) > 1:
            QtWidgets.QMessageBox.warning(None, "Ошибка экспорта", f"Необходимо выбрать только один график")
            return
        if len(showed_graphs) == 0:
            QtWidgets.QMessageBox.warning(None, "Ошибка экспорта", f"Выберите один график для экспорта")
            return
        x = showed_graphs[0].get_xdata()
        y = showed_graphs[0].get_ydata()
        lable = showed_graphs[0].get_label()
        file = QtWidgets.QFileDialog.getSaveFileName()[0]
        np.savetxt(fname=file, X=np.column_stack((x, y)))
        QtWidgets.QMessageBox.information(None, "Файл сохранен", f"{lable} сохранен")

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

    def update_N_media(self):
        self.data.N_media = self.N_media_n_input.value() + 1j * self.N_media_k_input.value()
        self.update_data()

    def update_w_range(self):
        self.data.w_range = self.W1_RangeInput.value(), self.W2_RangeInput.value()
        self.data.update_w_range()
        self.update_data()

    def update_thickness(self):
        self.data.thickness = self.ThicknessInput.value() * 1e-7
        self.update_data()

    def update_data(self):
        start_time = time.time()
        self.data.calculate()
        self.graph.update_plots(self.data)
        self.graph2.update_plots(self.data)
        #print("--- %s seconds ---" % (time.time() - start_time))

    def sync_defaults(self):
        # sync base values
        self.EpsilonLimitInput.setValue(self.data.membrane_epsilon_limit)
        self.N_media_n_input.setValue(np.real(self.data.N_media))
        self.N_media_k_input.setValue(np.imag(self.data.N_media))
        self.W1_RangeInput.setValue(self.data.w_range[0])
        self.W2_RangeInput.setValue(self.data.w_range[1])
        self.ThicknessInput.setValue(self.data.thickness / 1e-7)
        self.BoundCountInput.setValue(self.data.bound_number)
        # sync free charge values
        self.NInput.setValue(float(str(self.data.free_N).split("e")[0]))
        self.NInputPow.setValue(float(str(self.data.free_N).split("e")[1][1:]))
        self.ChargeMassInput.setValue(self.data.free_mass / ELECTRON_MASS_GRAMS)
        self.GammaInput.setValue(self.data.free_gamma)
        self.EffectiveChargeInput.setValue(self.data.free_charge)
        self.PlasmOmegaText.setText(str(round(self.data.w_plasm_0, 3)))
        self.AngelSpinBox.setValue(float(self.data.angle) /np.pi * 180)
        self.AngelSlider.setValue(float(self.data.angle) / np.pi * 180)


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
with open(os.path.join(basedir, "static", "style.css"), "r") as file:
    app.setStyleSheet(file.read())
window = MainWindow()
window.showMaximized()
app.exec()
