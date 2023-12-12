"""Module is made to make an application with QTdesigner to plot a graph
"""
import csv
import sys

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from zonnecel.model import ExperimentZonnecel, list_devices
from zonnecel.ui_mainwindow import Ui_MainWindow

pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class UserInterface(QtWidgets.QMainWindow):
    """Class which is the model of the experiment"""

    def __init__(self):
        """Calls on the __init__() of the parent class"""
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # when these buttons are pressed, these functions are excecuted
        self.ui.comboBox.addItems(list_devices())
        self.ui.start_button.clicked.connect(self.plot_IU)

        self.ui.save_button.clicked.connect(self.save_data)

    @Slot()
    def plot_IU(self):
        """Makes a graph of voltages and currents with errorbars"""

        # current device is used in the graph
        self.experiment = ExperimentZonnecel(self.ui.comboBox.currentText())
        self.ui.PlotWidget.clear()

        # start, stop and amount of measurements can be manually altered in the graph
        (
            self.mean_voltages,
            self.mean_currents,
            self.error_voltages,
            self.error_currents,
        ) = self.experiment.IU(
            self.ui.start.value(),
            self.ui.stop.value(),
            self.ui.measurements.value(),
        )
        self.ui.PlotWidget.plot(
            self.mean_voltages, self.mean_currents, symbol="o", pen=None
        )
        self.ui.PlotWidget.setLabel("left", "Currents (A)")
        self.ui.PlotWidget.setLabel("bottom", "Voltages (V)")
        error_bars = pg.ErrorBarItem(
            x=np.array(self.mean_voltages),
            y=np.array(self.mean_currents),
            width=2 * np.array(self.error_voltages),
            height=2 * np.array(self.error_currents),
        )
        self.ui.PlotWidget.addItem(error_bars)
        # self.experiment.close_device()

    def plot_PR(self):
        """Makes a graph of voltages and currents with errorbars"""

        # current device is used in the graph
        self.experiment = ExperimentZonnecel(self.ui.comboBox.currentText())
        self.ui.PlotWidget.clear()

        # start, stop and amount of measurements can be manually altered in the graph
        (
            self.mean_powers,
            self.mean_resistances,
            self.error_powers,
            self.error_resistances,
        ) = self.experiment.PR(
            self.ui.start.value(),
            self.ui.stop.value(),
            self.ui.measurements.value(),
        )
        self.ui.PlotWidget.plot(
            self.mean_powers, self.mean_resistances, symbol="o", pen=None
        )
        self.ui.PlotWidget.setLabel("left", "Resistance (Ohm)")
        self.ui.PlotWidget.setLabel("bottom", "Power (W)")
        error_bars = pg.ErrorBarItem(
            x=np.array(self.mean_powers),
            y=np.array(self.mean_resistances),
            width=2 * np.array(self.error_powers),
            height=2 * np.array(self.error_resistances),
        )
        self.ui.PlotWidget.addItem(error_bars)
        # self.experiment.close_device()

    def save_data(self):
        """Opens a csv file under given name and saves data"""
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        with open(f"{filename}", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["mean voltages", "mean currents", "error voltages", "error currents"]
            )
            for a, b, c, d in zip(
                self.mean_powers,
                self.mean_resistances,
                self.error_powers,
                self.error_resistances,
            ):
                writer.writerow([a, b, c, d])


def main():
    """Make an application of QtWidget to execute and show the interface"""
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()