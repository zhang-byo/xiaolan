# -*- coding: UTF-8 -*-
import sys
import os
sys.path.append('/home/pi/xiaolan/snowboy')
import snowboydecoder

def awaken():

    detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/snowboy/Alexa.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(a)

def a():
    try:
        sys.exit(-1)
    except SystemExit:
        os.system('python /home/pi/xiaolan/xldo.py unawaken')

awaken()
    
