# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:34:13 2024

@author: light
"""

import numpy as np
import homcloud.interface as hc
import homcloud.py3dmolhelper as py3dmolhelper
import matplotlib.pyplot as plt  #  可視化のため matplitlib の読み込み
import os
import cv2
import glob



judge_list = 'dataset/2afc/train/mix/judge/*.npy'
dis_list = 'per_dataset/2afc/train/mix/judge/judge_res'

def save_npy(judge_dir,dis_list):
    judge_list = glob.glob(judge_dir)
    x_list = []
    for item in judge_list:
        x = np.load(item)
        x_list.append(x.tolist())
        print(item)
        
    x_numpy = np.asarray(x_list)
    print(x_numpy)
    
    """
    np.save(dis_list , x_numpy)
    """
    
save_npy('dataset/2afc/val/cnn/judge/*.npy', 'per_dataset/2afc/val/cnn/judge/judge_res')


"""
save_npy('dataset/2afc/val/color/judge/*.npy', 'per_dataset/2afc/val/color/judge/judge_res')
save_npy('dataset/2afc/val/deblur/judge/*.npy', 'per_dataset/2afc/val/deblur/judge/judge_res')
save_npy('dataset/2afc/val/frameinterp/judge/*.npy', 'per_dataset/2afc/val/frameinterp/judge/judge_res')
save_npy('dataset/2afc/val/superres/judge/*.npy', 'per_dataset/2afc/val/superres/judge/judge_res')
save_npy('dataset/2afc/val/traditional/judge/*.npy', 'per_dataset/2afc/val/traditional/judge/judge_res')
"""
