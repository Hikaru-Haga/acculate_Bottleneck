# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:42:55 2024

@author: light
"""

import numpy as np
import homcloud.interface as hc
import homcloud.py3dmolhelper as py3dmolhelper
import matplotlib.pyplot as plt  #  可視化のため matplitlib の読み込み
import os
import cv2
import glob

judge_res = np.load('per_dataset/2afc/val/frameinterp/judge/judge_res.npy')
tra_cnn_res = np.load('result/result_val_frameinterp_d1.npy')


i = 0
for index in range(len(judge_res)):
    if judge_res[index] == tra_cnn_res[index]:
        i += 1
         

print("num = " + str(len(judge_res)) + " correct = " + str(i))
print("accuracy = " + str((i/len(judge_res)) * 100))
