# 安装逻辑模块 安装version.dll 加载器
# 下载version.dll到游戏根目录 下载加载器到%appdata%\Balatro\Mods

import os
import shutil
from config import Config
from downloader import download_file
from github_api import get_latest_release
from utils import *
from mods_manager import ModManager
from logger import Logger

def install_version_dll(game_root):
    '''
    :param game_root: 游戏根目录
    :return: 安装lovely到游戏根目录
    '''
    repo_name = "ethangreen-dev/lovely-injector"

    # 获取最新下载URL
    try:
        url, lovely_version = get_latest_release(repo_name, return_version=True)
    except Exception as e:
        return f"获取lovely最新发行版失败: {e}"

    with temp_directory(prefix="lovely_") as temp_dir:
        unzip_path = download_and_unzip(url, temp_dir)

        dll_path = find_file(unzip_path, "version.dll")
        if not dll_path:
            return "安装失败, 解压后的文件中未找到 version.dll"
        shutil.move(dll_path, os.path.join(game_root, "version.dll"))

        ModManager.set_mod_info("lovely_injector", {
            "version": lovely_version
        })
        return "lovely 安装成功! "

def install_loader_mods(mods_folder):
    '''
    :param mods_folder: Mods文件夹
    :return: 安装steamodded到Mods文件夹
    '''
    from git import  Repo
    repo_url = Config.steamodded_repo_url
    target_path = os.path.join(mods_folder, "Steamodded")

    ensure_folder_exists(mods_folder)
    if os.path.exists(target_path):
        try:
            shutil.rmtree(target_path)
        except Exception as e:
            return f"清理旧加载器失败: {e}"

    try:
        Logger.info(f"正在克隆仓库到 {target_path}...")
        Repo.clone_from(repo_url, target_path)
    except Exception as e:
        return f"克隆加载器失败: {e}"

    return "Steamodded 加载器安装完成！"