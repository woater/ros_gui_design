# -*- coding: utf-8 -*-
# !/usr/bin/env python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, QProcess, QMutex, pyqtSignal
import demo
import time
import signal

thread_1_run = True
thread_2_run = True


qmut_1 = QMutex()  # 创建线程锁
qmut_2 = QMutex()


class Thread_1(QThread):  # 线程1
    def __init__(self):
        super(Thread_1, self).__init__()

    def run(self):
        qmut_1.lock()  # 加锁
        values = [1, 2, 3, 4, 5]
        self.p1 = QProcess()
        self.p1.execute("rosrun", ["turtlesim", "turtlesim_node"])
        for i in values:
            print(i)
            time.sleep(0.5)  # 休眠
        qmut_1.unlock()  # 解锁


class Thread_2(QThread):  # 线程2
    _signal = pyqtSignal()

    def __init__(self):
        super(Thread_2, self).__init__()

    def run(self):
        # qmut_2.lock()  # 加锁
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(0.5)
        # qmut_2.unlock()  # 解锁
        self._signal.emit()


def click_success():  # push button function
    ui.pushButton.setEnabled(False)
    ui.pushButton_2.setEnabled(True)
    MainWindow.thread_1 = Thread_1()
    MainWindow.thread_1.start()


def click_success2():
    ui.pushButton_2.setEnabled(False)
    ui.pushButton.setEnabled(True)
    MainWindow.thread_1.p1.kill()


def click_success3():
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(True)
    MainWindow.thread_2 = Thread_2()
    MainWindow.thread_2.start()


def click_success4():
    ui.pushButton_4.setEnabled(False)
    ui.pushButton_3.setEnabled(True)
    Thread_2.p2.kill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = demo.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(click_success)
    ui.pushButton_2.clicked.connect(click_success2)
    ui.pushButton_3.clicked.connect(click_success3)
    ui.pushButton_4.clicked.connect(click_success4)
    sys.exit(app.exec_())
