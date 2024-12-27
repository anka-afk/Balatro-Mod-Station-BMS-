# 安装逻辑模块 安装version.dll 加载器
# 下载version.dll到游戏根目录 下载加载器到%appdata%\Balatro\Mods

import os
from utils import download_file

def install_version_dll(game_root):
    url = ""
    dest_path = os.path.join(game_root, "version.dll")
    return download_file(url, dest_path)

def install_loader_mods(mods_folder):
    loader_url = ""
    zip_path = os.path.join(mods_folder, "loader.zip")
    download_file(loader_url, zip_path)

    # 解压
    from utils import unzip_file
    unzip_file(zip_path, mods_folder)
    return "加载器安装完成"