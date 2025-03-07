# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:14:08 2024

@author: light

事前準備 
このファイルの置き場所　C:/perceptualSimilarity/
正解ラベルの置かれたファイル(0 or 1 or 0.5)　dataset/2afc/train/cnn/judge
画像0 dataset/2afc/train/cnn/p0
画像1 dataset/2afc/train/cnn/p1
参考画像 dataset/2afc/train/cnn/ref

正解ラベルのファイルの命名規則　<6桁>.npy
画像ファイル名の命名規則 <6桁>.png

"""
import homcloud.interface as hc
import numpy as np  # NumPy (数値配列)
import cv2
from sklearn.utils.extmath import cartesian
import os
import glob
            
def make_png2txt(source_dir,dis_dir):
    for subdir in os.listdir(source_dir):
        f = os.path.join(source_dir, subdir)
        if os.path.isfile(f):
            basename = os.path.splitext(os.path.basename(f))[0]
            bgr_array = cv2.imread(f)
            rgb_array = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2RGB)
            GRAY = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2GRAY)
            
            print(basename)
            dis_path = os.path.join(dis_dir, basename + "_GRAYxy.csv")
            np.savetxt(dis_path,GRAY,fmt='%d')

make_png2txt("dataset/2afc/val/cnn/p0", "xy_dataset/2afc/val/cnn/p0")
make_png2txt("dataset/2afc/val/cnn/p1", "xy_dataset/2afc/val/cnn/p1")
make_png2txt("dataset/2afc/val/cnn/ref", "xy_dataset/2afc/val/cnn/ref")

make_png2txt("dataset/2afc/val/color/p0", "xy_dataset/2afc/val/color/p0")
make_png2txt("dataset/2afc/val/color/p1", "xy_dataset/2afc/val/color/p1")
make_png2txt("dataset/2afc/val/color/ref", "xy_dataset/2afc/val/color/ref")

make_png2txt("dataset/2afc/val/deblur/p0", "xy_dataset/2afc/val/deblur/p0")
make_png2txt("dataset/2afc/val/deblur/p1", "xy_dataset/2afc/val/deblur/p1")
make_png2txt("dataset/2afc/val/deblur/ref", "xy_dataset/2afc/val/deblur/ref")

make_png2txt("dataset/2afc/val/frameinterp/p0", "xy_dataset/2afc/val/frameinterp/p0")
make_png2txt("dataset/2afc/val/frameinterp/p1", "xy_dataset/2afc/val/frameinterp/p1")
make_png2txt("dataset/2afc/val/frameinterp/ref", "xy_dataset/2afc/val/frameinterp/ref")

make_png2txt("dataset/2afc/val/superres/p0", "xy_dataset/2afc/val/superres/p0")
make_png2txt("dataset/2afc/val/superres/p1", "xy_dataset/2afc/val/superres/p1")
make_png2txt("dataset/2afc/val/superres/ref", "xy_dataset/2afc/val/superres/ref")

make_png2txt("dataset/2afc/val/traditional/p0", "xy_dataset/2afc/val/traditional/p0")
make_png2txt("dataset/2afc/val/traditional/p1", "xy_dataset/2afc/val/traditional/p1")
make_png2txt("dataset/2afc/val/traditional/ref", "xy_dataset/2afc/val/traditional/ref")