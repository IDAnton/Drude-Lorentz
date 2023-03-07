from PySide6 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt


class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor("#FDFDFDFF")
        self.fig.set_facecolor("#FDFDFDFF")
        self.fig.tight_layout(pad=0.1)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class mplwidget2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        self.toolbar = NavigationToolbar(self.canvas, self)  # add Toolbar
        self.vbl.addWidget(self.toolbar)

        self.RTE_wave, = self.canvas.ax.plot([], [], label="RTE")
        self.RTM_wave, = self.canvas.ax.plot([], [], label="RTM")
        self.TE_phase_12, = self.canvas.ax.plot([], [], label="TE_phase")
        self.TM_phase_12, = self.canvas.ax.plot([], [], label="TM_phase")
        self.RNP_wave, = self.canvas.ax.plot([], [], label="RNP")
        self.experimental, = self.canvas.ax.plot([], [], label="experiment")
        for line in self.canvas.ax.get_lines():
            line.set_linewidth(3)
        self.canvas.ax.legend(loc='upper right', ncols=2, fontsize=12)
        self.RTE_wave.set_visible(True)
        self.RTM_wave.set_visible(True)
        self.TE_phase_12.set_visible(False)
        self.TM_phase_12.set_visible(False)
        self.RNP_wave.set_visible(False)
        self.experimental.set_visible(False)
        self.redraw_legends()  # show only visible legends

    def update_plots(self, data, data_changed=True, redraw_legend=False):
        if data_changed:
            self.RTE_wave.set_data(data.w, data.RTE)
            self.RTM_wave.set_data(data.w, data.RTM)
            self.TE_phase_12.set_data(data.w, data.TE_phase)
            self.TM_phase_12.set_data(data.w, data.TM_phase)
            self.RNP_wave.set_data(data.w, data.RNP)
            if (data.experiment2_x is not None) and (data.experiment2_y is not None):
                self.experimental.set_data(data.experiment2_x, data.experiment2_y)
        if redraw_legend:
            self.redraw_legends()
        self.canvas.ax.relim(visible_only=True)
        self.canvas.ax.autoscale_view()
        self.canvas.fig.canvas.draw()
        self.canvas.fig.canvas.flush_events()

    def redraw_legends(self):
        labels = []
        for line in self.canvas.ax.get_lines():
            if line._visible:
                labels.append(line)
        self.canvas.ax.legend(handles=labels, loc='upper right', ncols=2, fontsize=12)
