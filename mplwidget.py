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
        self.fig.tight_layout(pad=0.25, h_pad=0.25, w_pad=0.25)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        self.toolbar = NavigationToolbar(self.canvas, self)  # add Toolbar
        self.vbl.addWidget(self.toolbar)

        self.N_n_plot, = self.canvas.ax.plot([], [], label="N_n")
        self.N_k_plot, = self.canvas.ax.plot([], [], label="N_k")
        self.alpha, = self.canvas.ax.plot([], [], label="alpha")
        self.D, = self.canvas.ax.plot([], [], label="D")
        self.R_12, = self.canvas.ax.plot([], [], label="R")
        self.T, = self.canvas.ax.plot([], [], label="T")
        self.phase, = self.canvas.ax.plot([], [], label="phi")
        self.A, = self.canvas.ax.plot([], [], label="A")
        self.eps_, = self.canvas.ax.plot([], [],  label="eps''")
        self.eps__, = self.canvas.ax.plot([], [], label="eps''")
        for line in self.canvas.ax.get_lines():
            line.set_linewidth(3)
        self.canvas.ax.legend(loc='upper right', ncols=5, fontsize=11)
        self.alpha.set_visible(False)
        self.D.set_visible(False)
        self.R_12.set_visible(False)
        self.T.set_visible(False)
        self.phase.set_visible(False)
        self.A.set_visible(False)
        self.eps_.set_visible(False)
        self.eps__.set_visible(False)

    def update_plots(self, data, data_changed=True):
        if data_changed:
            self.N_n_plot.set_data(data.w, data.N_n)
            self.N_k_plot.set_data(data.w, data.N_k)
            self.alpha.set_data(data.w, data.alpha)
            self.D.set_data(data.w, data.D)
            self.R_12.set_data(data.w, data.R_12)
            self.T.set_data(data.w, data.T)
            self.phase.set_data(data.w, data.phi)
            self.A.set_data(data.w, data.A)
            self.eps_.set_data(data.w, data.epsilon_real)
            self.eps__.set_data(data.w, data.epsilon_im)
        self.canvas.ax.relim(visible_only=True)
        self.canvas.ax.autoscale_view()
        self.canvas.fig.canvas.draw()
        self.canvas.fig.canvas.flush_events()
