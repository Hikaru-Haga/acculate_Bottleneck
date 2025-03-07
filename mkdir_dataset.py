# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:00:58 2024

@author: light
"""

import os
import shutil

def duplicate_subdirectories(source_dir, destination_dir):
    """
    指定されたディレクトリ内の全てのサブディレクトリを複製します。

    Args:
        source_dir (str): 元のディレクトリパス。
        destination_dir (str): 複製先のディレクトリパス。
    """
    if not os.path.exists(source_dir):
        print(f"元ディレクトリ '{source_dir}' が存在しません。")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # サブディレクトリを巡回
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            # サブディレクトリのパスを生成
            source_path = os.path.join(root, dir_name)
            # 新しいディレクトリ構造を構築
            relative_path = os.path.relpath(source_path, source_dir)
            dest_path = os.path.join(destination_dir, relative_path)

            # ディレクトリを作成
            os.makedirs(dest_path, exist_ok=True)
            print(f"ディレクトリを複製しました: {dest_path}")

# 使用例
source_dir = "dataset"  # 元ディレクトリのパス
destination_dir = "per_dataset"  # 複製先のパス

duplicate_subdirectories(source_dir, destination_dir)