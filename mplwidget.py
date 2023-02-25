from PySide6 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt


class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        # self.ax.set_facecolor("#121e29")
        # self.fig.set_facecolor("#121e29")
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

        self.N_n_plot, = self.canvas.ax.plot([], [])
        self.N_k_plot, = self.canvas.ax.plot([], [])

        self.N_n_plot.set_label('N_n')
        self.N_k_plot.set_label('N_k')
        self.canvas.ax.legend()

    def update_plots(self, data, data_changed=True):
        if data_changed:
            self.N_n_plot.set_data(data.w, data.N_n)
            self.N_k_plot.set_data(data.w, data.N_k)
        self.canvas.ax.relim(visible_only=True)
        self.canvas.ax.autoscale_view()
        self.canvas.fig.canvas.draw()
        self.canvas.fig.canvas.flush_events()
