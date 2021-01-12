# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:13:31 2021

@author: lanli
"""


import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import threading
import time
from PyQt5.QtWidgets import QMainWindow,QApplication
import my_video_player
from PyQt5.QtGui import *
from PyQt5 import QtGui
#from PyQt5.QtCore import QThread
import cv2

class MainCode(QMainWindow, my_video_player.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        my_video_player.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.video_play=False
        self.pushButton_fly.clicked.connect(self.on_video)    #按键控制无人机起飞
        self.pushButton_land.clicked.connect(self.off_video)  #按键控制无人机降落
        self.pushButton_fly.setEnabled(True)    #起飞前起飞按钮生效
        self.pushButton_land.setEnabled(False)  #起飞前降落按钮失效
        # self.video_stream=cv2.VideoCapture('/home/ubunutu/Documents/llui/video.mp4')
        self.video_stream=cv2.VideoCapture('http://192.168.1.103:8080/stream?topic=/camera/color/image_raw')
        self.frameRate = self.video_stream.get(cv2.CAP_PROP_FPS) # cv2.CV_CAP_PROP_FPS
        # self.totalFrameNumber=self.video_stream.get(cv2.CAP_PROP_FRAME_COUNT)
        # print(self.totalFrameNumber)

        
        self.horizontalScrollBar_pitch.setMinimum(-4)
        self.horizontalScrollBar_pitch.setMaximum(4)
        self.horizontalScrollBar_pitch.setSingleStep(1)
        self.horizontalScrollBar_pitch.setValue(0)
        self.horizontalScrollBar_pitch.valueChanged.connect(self.valuechange)
        
        
    def on_video(self):  # 起飞按钮的一些显示问题，可添加无人机起飞控制代码
        if self.video_play==False:
            self.pushButton_land.setEnabled(True)  #起飞后降落按钮生效 
            self.pushButton_fly.setEnabled(False)  #起飞后起飞按钮失效
            self.pushButton_fly.setText('已起飞')  #将按键改名
            self.video_play=True
            # 创建视频显示线程
            th = threading.Thread(target=self.Display)
            th.start()
        else:
            pass
        
    def off_video(self): # 降落按钮的一些显示问题，可添加无人机降落控制代码
        if self.video_play==True:
            self.pushButton_fly.setEnabled(False)   #起飞后起飞按钮依旧失效
            self.pushButton_land.setEnabled(False)  #起飞后降落按钮依旧失效
            self.pushButton_land.setText('已降落')  #将按键改名
            self.video_play=False
        else:
            pass

    def Display(self):
        if self.video_play:
            # frame_count=int(self.totalFrameNumber)
            while self.video_play:
                ret, frame = self.video_stream.read()
                #print(str(ret))
                if ret==True:
                    # print(str(ret))
                    frame=cv2.resize(frame,(1024, 431),interpolation=cv2.INTER_AREA)  #适应UI界面的窗口大小
                    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    self.Qframe=QImage(frame.data,frame.shape[1],frame.shape[0],
                               frame.shape[1]*3,QImage.Format_RGB888)           #Qimage读取图片
                    self.label_display_image.setPixmap(QPixmap.fromImage(self.Qframe))  #在Qlabel上画图
                    
                    cv2.waitKey(int(1000 / self.frameRate))
                else:
                    pass
                # frame_count=frame_count-1
                # print(frame_count)

    def valuechange(self):
        print('current slide_pitch value=%s' % self.horizontalScrollBar_pitch.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())
