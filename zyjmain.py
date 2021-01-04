# -*- coding: utf-8 -*-
# !/usr/bin/env python

import sys
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, QProcess
import demo
import os
import signal


pitch = 0.0
roll = 0.0
yaw = 0.0
thrust = 0.3
servicepid = 0


class Thread_launch(QThread):  # thread for launch controll node
    def __init__(self):
        super(Thread_launch, self).__init__()

    def run(self):
        global servicepid
        self.plaunch = QProcess()
        self.plaunch.execute("roscore&")
        self.plaunch.waitForFinished()


def click_launch():
    ui.pushButton_launch.setEnabled(False)
    ui.pushButton_stop.setEnabled(True)
    ui.thread_launch = Thread_launch()
    ui.thread_launch.start()


def click_stop():
    pstop = QProcess()
    pstop.execute("killall -9 roscore")
    pstop.waitForFinished()
    pstop.execute("killall -9 rosmaster")
    pstop.waitForFinished()
    ui.pushButton_launch.setEnabled(True)


def click_unlock():
    ui.pushButton_unlock.setEnabled(False)
    ui.pushButton_lock.setEnabled(True)
    punlock = QProcess()
    punlock.execute("rosservice", ["call", "/mavros/cmd/arming", "value: true"])
    punlock.waitForFinished()


def click_lock():
    ui.pushButton_lock.setEnabled(False)
    ui.pushButton_unlock.setEnabled(True)
    punlock = QProcess()
    punlock.execute("rosservice", ["call", "/mavros/cmd/arming", "value: false"])
    punlock.waitForFinished()


def click_set():
    global pitch, roll, yaw, thrust
    pset = QProcess()
    attributes_postfix = ", frame_id: 'body', auto_arm: true}"
    attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
    pset.execute("rosservice", ["call", "/set_attitude", attributes])
    print(attributes)


def edit_pitch(text):
    print("pitch changed: " + text)
    global pitch
    try:
        pitch = float(text)
    except ValueError:
        print("invalid value")


def edit_roll(text):
    print("roll changed: " + text)
    global roll
    try:
        roll = float(text)
    except ValueError:
        print("invalid value")


def edit_yaw(text):
    print("yaw changed: " + text)
    global yaw
    try:
        yaw = float(text)
    except ValueError:
        print("invalid value")


def edit_thrust(text):
    print("thrust changed: " + text)
    global thrust
    try:
        thrust = float(text)
    except ValueError:
        print("invalid value")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = demo.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #  set push buttons
    ui.pushButton_launch.clicked.connect(click_launch)
    ui.pushButton_launch.setEnabled(True)
    ui.pushButton_stop.clicked.connect(click_stop)
    ui.pushButton_stop.setEnabled(False)
    ui.pushButton_unlock.clicked.connect(click_unlock)
    ui.pushButton_lock.clicked.connect(click_lock)
    ui.pushButton_set.clicked.connect(click_set)
    #  set lineEdits
    ui.lineEdit_pitch.setPlaceholderText("0.0")
    ui.lineEdit_roll.setPlaceholderText("0.0")
    ui.lineEdit_yaw.setPlaceholderText("0.0")
    ui.lineEdit_thrust.setPlaceholderText("0.3")
    # set validators
    doubleValidator1 = QDoubleValidator()
    doubleValidator1.setRange(-0.4, 0.4)
    doubleValidator1.setNotation(QDoubleValidator.StandardNotation)
    doubleValidator1.setDecimals(2)
    doubleValidator2 = QDoubleValidator()
    doubleValidator2.setRange(-3.14, 3.14)
    doubleValidator2.setNotation(QDoubleValidator.StandardNotation)
    doubleValidator2.setDecimals(2)
    doubleValidator3 = QDoubleValidator()
    doubleValidator3.setRange(0.0, 1.0)
    doubleValidator3.setNotation(QDoubleValidator.StandardNotation)
    doubleValidator3.setDecimals(2)
    #  binding validator
    ui.lineEdit_pitch.setValidator(doubleValidator1)
    ui.lineEdit_roll.setValidator(doubleValidator1)
    ui.lineEdit_yaw.setValidator(doubleValidator2)
    ui.lineEdit_thrust.setValidator(doubleValidator3)
    # connect lineEdits
    ui.lineEdit_pitch.textChanged.connect(edit_pitch)
    ui.lineEdit_roll.textChanged.connect(edit_roll)
    ui.lineEdit_yaw.textChanged.connect(edit_yaw)
    ui.lineEdit_thrust.textChanged.connect(edit_thrust)
    sys.exit(app.exec_())
