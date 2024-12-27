# 安装逻辑模块 安装version.dll 加载器
# 下载version.dll到游戏根目录 下载加载器到%appdata%\Balatro\Mods

import os
import shutil
from downloader import download_file
from github_api import get_latest_release
from  utils import  ensure_folder_exists, unzip_file

def install_version_dll(game_root):
    repo_name = "ethangreen-dev/lovely-injector"

    # 获取最新下载URL
    try:
        url = get_latest_release(repo_name)
    except Exception as e:
        return f"获取lovely最新发行版失败: {e}"

    # 临时目录下载解压
    temp_dir = os.path.join(game_root, "temp")
    ensure_folder_exists(temp_dir)

    # 下载
    zip_path = os.path.join(temp_dir, "release.zip")
    result = download_file(url, zip_path)
    if "失败" in result:
        return  result

    # 解压缩到临时目录
    unzip_path = os.path.join(temp_dir, "unzip")
    ensure_folder_exists(unzip_path)
    unzip_file(zip_path, unzip_path)

    # 检查是否存在 version.dll 文件
    dll_path = None
    for root, dirs, files in os.walk(unzip_path):
        if "version.dll" in files:
            dll_path = os.path.join(root, "version.dll")
            break

    if not dll_path:
        # 清理临时目录
        shutil.rmtree(temp_dir)
        return "安装失败, 解压后的文件中未找到 version.dll"

    # 将 version.dll 移动到游戏根目录
    try:
        shutil.move(dll_path, os.path.join(game_root, "version.dll"))
    except Exception as e:
        return f"安装失败, 移动 version.dll 到游戏根目录失败: {e}"

    # 清理临时目录
    shutil.rmtree(temp_dir)
    return "lovely 安装成功！"

def install_loader_mods(mods_folder):
    loader_url = ""
    zip_path = os.path.join(mods_folder, "loader.zip")
    download_file(loader_url, zip_path)

    # 解压
    from utils import unzip_file
    unzip_file(zip_path, mods_folder)
    return "加载器安装完成"