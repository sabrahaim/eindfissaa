# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PlotWidget = PlotWidget(self.centralwidget)
        self.PlotWidget.setObjectName(u"PlotWidget")

        self.verticalLayout_4.addWidget(self.PlotWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.start = QDoubleSpinBox(self.centralwidget)
        self.start.setObjectName(u"start")

        self.verticalLayout_2.addWidget(self.start)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.stop = QDoubleSpinBox(self.centralwidget)
        self.stop.setObjectName(u"stop")

        self.verticalLayout_3.addWidget(self.stop)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.measurements = QSpinBox(self.centralwidget)
        self.measurements.setObjectName(u"measurements")

        self.verticalLayout.addWidget(self.measurements)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.comboBox2 = QComboBox(self.centralwidget)
        self.comboBox2.setObjectName(u"comboBox2")

        self.verticalLayout_4.addWidget(self.comboBox2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_4.addWidget(self.comboBox)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout_4.addWidget(self.start_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout_4.addWidget(self.save_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Measurements", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start measurements", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

