# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:01:30 2024

@author: light
"""

import numpy as np
import homcloud.interface as hc
import homcloud.py3dmolhelper as py3dmolhelper
import matplotlib.pyplot as plt  #  可視化のため matplitlib の読み込み
import os
import cv2
import glob


def make_BD(source_dir):
    source_split = str(source_dir).split('/')
    ref_list = glob.glob(os.path.join(source_dir,'ref','*.pdgm'))
    p0_list = glob.glob(os.path.join(source_dir,'p0','*.pdgm'))
    p1_list = glob.glob(os.path.join(source_dir,'p1','*.pdgm'))
    
    res_list = []
    for index in range(len(ref_list)):
        print(index)
        pd_ref = hc.PDList(ref_list[index]).dth_diagram(1)
        pd_p0 = hc.PDList(p0_list[index]).dth_diagram(1)
        pd_p1 = hc.PDList(p1_list[index]).dth_diagram(1)

        bottle_dis_p0 = hc.distance.bottleneck(pd_ref, pd_p0)
        bottle_dis_p1 = hc.distance.bottleneck(pd_ref, pd_p1)
        if bottle_dis_p0 > bottle_dis_p1:
            res_list.append([1.0])
        elif bottle_dis_p0 < bottle_dis_p1:
            res_list.append([0.0])
        else:
            res_list.append([0.5])

    res_numpy = np.asarray(res_list)
    np.save(os.path.join('result','result_' + source_split[2] + '_' + source_split[3] + '_d1'), res_numpy)
    

make_BD('per_dataset/2afc/val/cnn')
make_BD('per_dataset/2afc/val/color')
make_BD('per_dataset/2afc/val/deblur')
make_BD('per_dataset/2afc/val/frameinterp')
make_BD('per_dataset/2afc/val/superres')
make_BD('per_dataset/2afc/val/traditional')

    
