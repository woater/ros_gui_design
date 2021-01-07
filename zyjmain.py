# -*- coding: utf-8 -*-
# !/usr/bin/env python

import sys
import os
#  from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, QProcess
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
import demo
import cv2

pitch = 0.0
roll = 0.0
yaw = 0.0
thrust = 0.3
servicepid = 0
attributes_postfix = ", frame_id: 'body', auto_arm: true}"


class Thread_controll(QThread):  # thread for controll node
    def __init__(self):
        super(Thread_controll, self).__init__()

    def run(self):
        self.pcontroll = QProcess()
        self.plaunch.execute("roslaunch", ["clever", "clever.launch"])
        # self.pid = self.pcontroll.execute("roscore")
        print(self.pid)
        self.pcontroll.waitForFinished()


class Thread_camera(QThread):  # thread for camera node
    def __init__(self):
        super(Thread_camera, self).__init__()

    def run(self):
        self.plaunch = QProcess()
        self.plaunch.execute("roslaunch", ["ros_vision_demo", "rs_camera.launch"])
        self.plaunch.waitForFinished()


class Thread_face(QThread):  # thread for face detection
    def __init__(self):
        super(Thread_face, self).__init__()

    def run(self):
        self.plaunch = QProcess()
        self.plaunch.execute("rosrun", ["ros_vision_demo", "control_test4.py"])
        self.plaunch.waitForFinished()


# class Thread_set(QThread):
#     def __init__(self):
#         super(Thread_set, self).__init__()

#     def run(self):
#         self.pcontroll = QProcess()
#         global attributes_postfix
#         attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
#         self.pcontroll.execute("rosservice", ["call", "/set_attitude", attributes])


def click_controll():
    ui.pushButton_controll.setEnabled(False)
    ui.pushButton_stopcontroll.setEnabled(True)
    ui.thread_launch = Thread_controll()
    ui.thread_launch.start()


def click_stopcontroll():
    pstop = QProcess()
    pstop.execute("rosnode", ["kill", "clever"])
    pstop.waitForFinished()
    ui.pushButton_controll.setEnabled(True)


def click_camera():
    ui.pushButton_camera.setEnabled(False)
    ui.pushButton_stopcamera.setEnabled(True)
    ui.thread_camera = Thread_camera()
    ui.thread_camera.start()


def click_stopcamera():
    ui.pushButton_camera.setEnabled(True)
    pstopcamera = QProcess()
    pstopcamera.execute("rosnode", ["kill", "ros_vision_demo"])
    pstopcamera.waitForFinished()


def click_unlock():
    # ui.video_play = True
    # print("video_play: " + repr(ui.video_play))
    ui.pushButton_unlock.setEnabled(False)
    ui.pushButton_lock.setEnabled(True)
    punlock = QProcess()
    punlock.execute("rosservice", ["call", "/mavros/cmd/arming", "value: true"])
    punlock.waitForFinished()


def click_lock():
    # ui.video_play = False
    # print("video_play: " + repr(ui.video_play))
    ui.pushButton_lock.setEnabled(False)
    ui.pushButton_unlock.setEnabled(True)
    punlock = QProcess()
    punlock.execute("rosservice", ["call", "/mavros/cmd/arming", "value: false"])
    punlock.waitForFinished()


def click_set():
    global pitch, roll, yaw, thrust
    pset = QProcess()
    global attributes_postfix
    attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
    pset.execute("rosservice", ["call", "/set_attitude", attributes])
    print(attributes)


def click_face():
    ui.pushButton_face.setEnabled(True)
    ui.thread_face = Thread_face()
    ui.thread_face.start()


def click_stopface():
    # pstopcamera = QProcess()
    # pstopcamera.execute("rosnode", ["kill", "ros_vision_demo"])
    # pstopcamera.execute("rosnode", ["kill", "$(rosnode list)", "|", "grep", "face"])
    # pstopcamera.waitForFinished()
    os.system("rosnode kill $(rosnode list) | grep face")
    ui.pushButton_camera.setEnabled(True)



# def edit_pitch(text):
#     print("pitch changed: " + text)
#     global pitch
#     try:
#         pitch = float(text)
#     except ValueError:
#         print("invalid value")


# def edit_roll(text):
#     print("roll changed: " + text)
#     global roll
#     try:
#         roll = float(text)
#     except ValueError:
#         print("invalid value")


# def edit_yaw(text):
#     print("yaw changed: " + text)
#     global yaw
#     try:
#         yaw = float(text)
#     except ValueError:
#         print("invalid value")


# def edit_thrust(text):
#     print("thrust changed: " + text)
#     global thrust
#     try:
#         thrust = float(text)
#     except ValueError:
#         print("invalid value")


def scroll_pitch():
    global pitch
    pitch = float(ui.Scrollbar_pitch.value()) / 100
    print(pitch)
    pset = QProcess()
    attributes_postfix = ", frame_id: 'body', auto_arm: true}"
    attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
    pset.execute("rosservice", ["call", "/set_attitude", attributes])


def scroll_roll():
    global roll
    roll = float(ui.Scrollbar_roll.value()) / 100
    pset = QProcess()
    attributes_postfix = ", frame_id: 'body', auto_arm: true}"
    attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
    pset.execute("rosservice", ["call", "/set_attitude", attributes])


def scroll_thrust():
    global thrust
    thrust = float(ui.Scrollbar_thrust.value()) / 100
    pset = QProcess()
    attributes_postfix = ", frame_id: 'body', auto_arm: true}"
    attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
    pset.execute("rosservice", ["call", "/set_attitude", attributes])


def scroll_yaw():
    global yaw
    yaw = float(ui.Scrollbar_yaw.value()) / 100
    pset = QProcess()
    attributes_postfix = ", frame_id: 'body', auto_arm: true}"
    attributes = "{pitch: " + repr(pitch) + ", roll: " + repr(roll) + ", yaw: " + repr(yaw) + ", thrust: " + repr(thrust) + attributes_postfix
    pset.execute("rosservice", ["call", "/set_attitude", attributes])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = demo.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # set video player
    ui.video_stream = cv2.VideoCapture('/home/ubunutu/Documents/tree.avi')
    ui.painter = QtGui.QPainter(MainWindow)
    ui.video_play = False
    print("ui.video_play" + repr(ui.video_play))
    #  set push buttons
    ui.pushButton_controll.clicked.connect(click_controll)
    ui.pushButton_controll.setEnabled(True)
    ui.pushButton_stopcontroll.clicked.connect(click_stopcontroll)
    ui.pushButton_stopcontroll.setEnabled(False)
    ui.pushButton_unlock.clicked.connect(click_unlock)
    ui.pushButton_lock.clicked.connect(click_lock)
    ui.pushButton_set.clicked.connect(click_set)
    ui.pushButton_face.clicked.connect(click_face)
    ui.pushButton_camera.clicked.connect(click_camera)
    ui.pushButton_stopcamera.setEnabled(True)
    ui.pushButton_stopcamera.clicked.connect(click_stopcamera)
    ui.pushButton_stopface.clicked.connect(click_stopface)
    # #  set lineEdits
    # ui.lineEdit_pitch.setPlaceholderText("0.0")
    # ui.lineEdit_roll.setPlaceholderText("0.0")
    # ui.lineEdit_yaw.setPlaceholderText("0.0")
    # ui.lineEdit_thrust.setPlaceholderText("0.3")
    # set validators
    # doubleValidator1 = QDoubleValidator()
    # doubleValidator1.setRange(-0.4, 0.4)
    # doubleValidator1.setNotation(QDoubleValidator.StandardNotation)
    # doubleValidator1.setDecimals(2)
    # doubleValidator2 = QDoubleValidator()
    # doubleValidator2.setRange(-3.14, 3.14)
    # doubleValidator2.setNotation(QDoubleValidator.StandardNotation)
    # doubleValidator2.setDecimals(2)
    # doubleValidator3 = QDoubleValidator()
    # doubleValidator3.setRange(0.0, 1.0)
    # doubleValidator3.setNotation(QDoubleValidator.StandardNotation)
    # doubleValidator3.setDecimals(2)
    # #  binding validator
    # ui.lineEdit_pitch.setValidator(doubleValidator1)
    # ui.lineEdit_roll.setValidator(doubleValidator1)
    # ui.lineEdit_yaw.setValidator(doubleValidator2)
    # ui.lineEdit_thrust.setValidator(doubleValidator3)
    # # connect lineEdits
    # ui.lineEdit_pitch.textChanged.connect(edit_pitch)
    # ui.lineEdit_roll.textChanged.connect(edit_roll)
    # ui.lineEdit_yaw.textChanged.connect(edit_yaw)
    # ui.lineEdit_thrust.textChanged.connect(edit_thrust)
    # set Scrollbars
    ui.Scrollbar_pitch.setMaximum(40)
    ui.Scrollbar_pitch.setMinimum(-40)
    ui.Scrollbar_pitch.setSingleStep(1)
    ui.Scrollbar_pitch.setValue(0)

    ui.Scrollbar_roll.setMaximum(40)
    ui.Scrollbar_roll.setMinimum(-40)
    ui.Scrollbar_roll.setSingleStep(1)
    ui.Scrollbar_roll.setValue(0)

    ui.Scrollbar_thrust.setMaximum(100)
    ui.Scrollbar_thrust.setMinimum(0)
    ui.Scrollbar_thrust.setSingleStep(1)
    ui.Scrollbar_thrust.setValue(30)

    ui.Scrollbar_yaw.setMaximum(314)
    ui.Scrollbar_yaw.setMinimum(-314)
    ui.Scrollbar_yaw.setSingleStep(1)
    ui.Scrollbar_yaw.setValue(0)
    # connect Scrollbar
    # ui.Scrollbar_pitch.valueChanged.connect(scroll_pitch)
    ui.Scrollbar_roll.sliderReleased.connect(scroll_roll)
    ui.Scrollbar_thrust.sliderReleased.connect(scroll_thrust)
    ui.Scrollbar_yaw.sliderReleased.connect(scroll_yaw)
    ui.Scrollbar_pitch.sliderReleased.connect(scroll_pitch)
    sys.exit(app.exec_())
