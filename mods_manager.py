# 模组管理模块 Mods文件夹的增删查
# 列出Mods下所有模组 添加模组 解压缩压缩包并安装到Mods

import  os
import  shutil

def list_mods(mods_folder):
    return  [f for f in os.listdir(mods_folder) if os.path.isdir(os.path.join(mods_folder, f))]

def add_mod(source_path, mods_folder):
    if source_path.endswith(".zip"):
        from utils import  unzip_file
        unzip_file(source_path, mods_folder)

    else:
        shutil.copytree(source_path, os.path.join(mods_folder, os.path.basename(source_path)))
    return  "模组添加完成"