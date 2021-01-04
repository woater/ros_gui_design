# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(600, 10, 160, 128))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_launch = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_launch.setObjectName("pushButton_launch")
        self.verticalLayout.addWidget(self.pushButton_launch)
        self.pushButton_unlock = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_unlock.setObjectName("pushButton_unlock")
        self.verticalLayout.addWidget(self.pushButton_unlock)
        self.pushButton_lock = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_lock.setObjectName("pushButton_lock")
        self.verticalLayout.addWidget(self.pushButton_lock)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(600, 180, 161, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_pitch = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_pitch.setObjectName("lineEdit_pitch")
        self.horizontalLayout.addWidget(self.lineEdit_pitch)
        self.pushButton_set = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_set.setGeometry(QtCore.QRect(640, 430, 99, 27))
        self.pushButton_set.setObjectName("pushButton_set")
        self.pushButton_face = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_face.setGeometry(QtCore.QRect(590, 460, 181, 31))
        self.pushButton_face.setObjectName("pushButton_face")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(600, 240, 161, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_roll = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_roll.setObjectName("lineEdit_roll")
        self.horizontalLayout_2.addWidget(self.lineEdit_roll)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(600, 300, 161, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_yaw = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_yaw.setObjectName("lineEdit_yaw")
        self.horizontalLayout_3.addWidget(self.lineEdit_yaw)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(600, 360, 161, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_thrust = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_thrust.setObjectName("lineEdit_thrust")
        self.horizontalLayout_4.addWidget(self.lineEdit_thrust)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 150, 121, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UAV controller"))
        self.pushButton_launch.setText(_translate("MainWindow", "launch controll node"))
        self.pushButton_unlock.setText(_translate("MainWindow", "unlock UAV"))
        self.pushButton_lock.setText(_translate("MainWindow", "lock UAV"))
        self.label.setText(_translate("MainWindow", "pitch"))
        self.pushButton_set.setText(_translate("MainWindow", "set"))
        self.pushButton_face.setText(_translate("MainWindow", "face detect and trace"))
        self.label_2.setText(_translate("MainWindow", "roll   "))
        self.label_3.setText(_translate("MainWindow", "yaw  "))
        self.label_4.setText(_translate("MainWindow", "thrust"))
        self.label_5.setText(_translate("MainWindow", "manual controll"))
        self.menuMore.setTitle(_translate("MainWindow", "more"))
