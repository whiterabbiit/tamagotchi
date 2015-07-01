# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jul  1 18:38:56 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 626)
        self.frame_widget = QtWidgets.QWidget(MainWindow)
        self.frame_widget.setObjectName("frame_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttons_2 = QtWidgets.QFrame(self.frame_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_2.sizePolicy().hasHeightForWidth())
        self.buttons_2.setSizePolicy(sizePolicy)
        self.buttons_2.setMinimumSize(QtCore.QSize(80, 500))
        self.buttons_2.setObjectName("buttons_2")
        self.buttons = QtWidgets.QVBoxLayout(self.buttons_2)
        self.buttons.setSpacing(0)
        self.buttons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.buttons.setContentsMargins(1, 1, -1, -1)
        self.buttons.setObjectName("buttons")
        self.coin = QtWidgets.QLabel(self.buttons_2)
        self.coin.setMinimumSize(QtCore.QSize(100, 100))
        self.coin.setText("")
        self.coin.setObjectName("coin")
        self.buttons.addWidget(self.coin)
        self.number_of_coins = QtWidgets.QLabel(self.buttons_2)
        self.number_of_coins.setStyleSheet("font: 75 12pt \"Helvetica\";")
        self.number_of_coins.setFrameShadow(QtWidgets.QFrame.Raised)
        self.number_of_coins.setTextFormat(QtCore.Qt.AutoText)
        self.number_of_coins.setAlignment(QtCore.Qt.AlignCenter)
        self.number_of_coins.setWordWrap(False)
        self.number_of_coins.setObjectName("number_of_coins")
        self.buttons.addWidget(self.number_of_coins)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttons.addItem(spacerItem)
        self.store = QtWidgets.QPushButton(self.buttons_2)
        self.store.setObjectName("store")
        self.buttons.addWidget(self.store)
        self.save = QtWidgets.QPushButton(self.buttons_2)
        self.save.setObjectName("save")
        self.buttons.addWidget(self.save)
        self.cure = QtWidgets.QPushButton(self.buttons_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cure.sizePolicy().hasHeightForWidth())
        self.cure.setSizePolicy(sizePolicy)
        self.cure.setObjectName("cure")
        self.buttons.addWidget(self.cure)
        self.play = QtWidgets.QPushButton(self.buttons_2)
        self.play.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setObjectName("play")
        self.buttons.addWidget(self.play)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttons.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.buttons_2)
        self.canvas_frame = QtWidgets.QFrame(self.frame_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_frame.sizePolicy().hasHeightForWidth())
        self.canvas_frame.setSizePolicy(sizePolicy)
        self.canvas_frame.setMinimumSize(QtCore.QSize(500, 500))
        self.canvas_frame.setMaximumSize(QtCore.QSize(500, 500))
        self.canvas_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_frame.setObjectName("canvas_frame")
        self.canvases = QtWidgets.QHBoxLayout(self.canvas_frame)
        self.canvases.setSpacing(0)
        self.canvases.setContentsMargins(0, 0, 0, 0)
        self.canvases.setObjectName("canvases")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.store_frame = QtWidgets.QFrame(self.canvas_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_frame.sizePolicy().hasHeightForWidth())
        self.store_frame.setSizePolicy(sizePolicy)
        self.store_frame.setObjectName("store_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.store_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4.addWidget(self.store_frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.canvases.addLayout(self.verticalLayout_4)
        self.snake_widget = SnakeWidget(self.canvas_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snake_widget.sizePolicy().hasHeightForWidth())
        self.snake_widget.setSizePolicy(sizePolicy)
        self.snake_widget.setStyleSheet("border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;")
        self.snake_widget.setObjectName("snake_widget")
        self.canvases.addWidget(self.snake_widget)
        self.tamagotchi_widget = TamagotchiWidget(self.canvas_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tamagotchi_widget.sizePolicy().hasHeightForWidth())
        self.tamagotchi_widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Armenian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tamagotchi_widget.setFont(font)
        self.tamagotchi_widget.setStyleSheet("")
        self.tamagotchi_widget.setObjectName("tamagotchi_widget")
        self.canvases.addWidget(self.tamagotchi_widget)
        self.horizontalLayout.addWidget(self.canvas_frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.frame_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(595, 100))
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(595, 100))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.energy_bar = QtWidgets.QProgressBar(self.horizontalFrame_2)
        self.energy_bar.setProperty("value", 100)
        self.energy_bar.setObjectName("energy_bar")
        self.verticalLayout_3.addWidget(self.energy_bar)
        self.health_bar = QtWidgets.QProgressBar(self.horizontalFrame_2)
        self.health_bar.setProperty("value", 100)
        self.health_bar.setObjectName("health_bar")
        self.verticalLayout_3.addWidget(self.health_bar)
        self.hygiene_bar = QtWidgets.QProgressBar(self.horizontalFrame_2)
        self.hygiene_bar.setProperty("value", 100)
        self.hygiene_bar.setObjectName("hygiene_bar")
        self.verticalLayout_3.addWidget(self.hygiene_bar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.food_bar = QtWidgets.QProgressBar(self.horizontalFrame_2)
        self.food_bar.setProperty("value", 100)
        self.food_bar.setObjectName("food_bar")
        self.verticalLayout_2.addWidget(self.food_bar)
        self.happiness_bar = QtWidgets.QProgressBar(self.horizontalFrame_2)
        self.happiness_bar.setProperty("value", 100)
        self.happiness_bar.setObjectName("happiness_bar")
        self.verticalLayout_2.addWidget(self.happiness_bar)
        self.foo_bar = QtWidgets.QProgressBar(self.horizontalFrame_2)
        self.foo_bar.setProperty("value", 100)
        self.foo_bar.setObjectName("foo_bar")
        self.verticalLayout_2.addWidget(self.foo_bar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        MainWindow.setCentralWidget(self.frame_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.number_of_coins.setText(_translate("MainWindow", "0"))
        self.store.setText(_translate("MainWindow", "store"))
        self.save.setText(_translate("MainWindow", "save"))
        self.cure.setText(_translate("MainWindow", "cure"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.energy_bar.setFormat(_translate("MainWindow", "Energy: %p%"))
        self.health_bar.setFormat(_translate("MainWindow", "Health: %p%"))
        self.hygiene_bar.setFormat(_translate("MainWindow", "Hygiene: %p%"))
        self.food_bar.setFormat(_translate("MainWindow", "Food: %p%"))
        self.happiness_bar.setFormat(_translate("MainWindow", "Happiness: %p%"))

from tamagotchi_widget import TamagotchiWidget
from snake_widget import SnakeWidget
