import sys
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

        data = Data()

        self.x = np.linspace(0, 6 * np.pi, 100)
        self.y = np.sin(self.x)

        self.l1 , = self.graph.canvas.ax.plot(self.x, self.y)
        l2 = self.graph.canvas.ax.plot(self.x, self.y)
        # self.graph.canvas.draw()
        self.pushButton.clicked.connect(self.update1)

    def update1(self):
        self.l1.set_ydata(np.random.random(100))
        self.graph.canvas.fig.canvas.draw()
        self.graph.canvas.fig.canvas.flush_events()



app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
#app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
window = MainWindow()
window.showMaximized()
app.exec()
