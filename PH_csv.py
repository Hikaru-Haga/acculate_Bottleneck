# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:50:37 2024

@author: light
"""

import numpy as np
import homcloud.interface as hc
import homcloud.py3dmolhelper as py3dmolhelper
import matplotlib.pyplot as plt  #  可視化のため matplitlib の読み込み
import os
import cv2

def main():
    make_PD("xy_dataset/2afc/val/color/p0", "per_dataset/2afc/val/color/p0")
    make_PD("xy_dataset/2afc/val/color/p1", "per_dataset/2afc/val/color/p1")
    make_PD("xy_dataset/2afc/val/color/ref", "per_dataset/2afc/val/color/ref")

    make_PD("xy_dataset/2afc/val/deblur/p0", "per_dataset/2afc/val/deblur/p0")
    make_PD("xy_dataset/2afc/val/deblur/p1", "per_dataset/2afc/val/deblur/p1")
    make_PD("xy_dataset/2afc/val/deblur/ref", "per_dataset/2afc/val/deblur/ref")

    make_PD("xy_dataset/2afc/val/frameinterp/p0", "per_dataset/2afc/val/frameinterp/p0")
    make_PD("xy_dataset/2afc/val/frameinterp/p1", "per_dataset/2afc/val/frameinterp/p1")
    make_PD("xy_dataset/2afc/val/frameinterp/ref", "per_dataset/2afc/val/frameinterp/ref")

    make_PD("xy_dataset/2afc/val/superres/p0", "per_dataset/2afc/val/superres/p0")
    make_PD("xy_dataset/2afc/val/superres/p1", "per_dataset/2afc/val/superres/p1")
    make_PD("xy_dataset/2afc/val/superres/ref", "per_dataset/2afc/val/superres/ref")

    make_PD("xy_dataset/2afc/val/traditional/p0", "per_dataset/2afc/val/traditional/p0")
    make_PD("xy_dataset/2afc/val/traditional/p1", "per_dataset/2afc/val/traditional/p1")
    make_PD("xy_dataset/2afc/val/traditional/ref", "per_dataset/2afc/val/traditional/ref")


def make_PD(source_dir,dis_dir):
    for filename in os.listdir(source_dir):
        f = os.path.join(source_dir, filename)
        if os.path.isfile(f):
            basename = os.path.splitext(os.path.basename(f))[0]
            print(f)
            a_load = np.loadtxt(f)
            dis_path = os.path.join(dis_dir, basename + ".pdgm")
            
            hc.PDList.from_bitmap_levelset(a_load, "sublevel", save_to=dis_path)


if __name__ == "__main__":
    main()