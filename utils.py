# 通用工具
# 文件夹检查 创建 解压缩 下载状态进度条

import  os
import shutil
import zipfile
import  json
import  tempfile
from downloader import download_file
from config import Config
from contextlib import contextmanager
from logger import Logger

def ensure_folder_exists(folder):
    '''
    :param folder: 文件夹路径
    :return: 如果不存在目标文件夹, 创建该文件夹
    '''
    if not os.path.exists(folder):
        os.makedirs(folder)

def unzip_file(zip_path,dest_path):
    '''
    :param zip_path: zip文件路径
    :param dest_path: 解压目标文件夹路径
    :return: 解压zip文件到目标文件夹
    '''
    ensure_folder_exists(dest_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)

def load_config():
    '''
    :return:加载config.json, 返回整个config字典
    '''
    if os.path.exists(Config.config_path):
        with open(Config.config_path, "r") as file:
            return json.load(file)
    return {}

def save_config(config):
    '''
    :param config: 需要保存的config字典
    :return: 直接替换保存进入config.json
    '''
    with open(Config.config_path, "w") as file:
        json.dump(config, file, indent=4)

def update_config(key, value):
    '''
    :param key: config.json字典中的键
    :param value: config.json中对应键需要更新的值
    :return: 直接写入文件
    '''
    config = load_config()

    if key in config:
        config[key] = value
        save_config(config)
        return  True
    else:
        return False

@contextmanager
def temp_directory(prefix="temp_"):
    '''
    创建一个临时目录, 并在使用完毕后自动清理.
    :param prefix: 临时目录的前缀
    :return: 临时目录路径
    '''
    temp_dir = tempfile.mkdtemp(prefix=prefix)
    try:
        Logger.info(f"临时目录已创建: {temp_dir}")
        yield temp_dir
    except Exception as e:
        Logger.error(f"创建临时目录失败: {e}")
        raise
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
            Logger.info(f"临时目录已清理: {temp_dir}")

def download_and_unzip(url, dest_folder, unzip_folder_name=None):
    '''
    下载文件并解压到目标文件夹
    :param url: 下载链接
    :param dest_folder:目标文件夹路径
    :return: 解压后的文件夹路径
    '''
    zip_path = download_file(url, dest_folder)
    if unzip_folder_name is None:
        zip_filename = os.path.basename(zip_path)
        unzip_folder_name  = os.path.splitext(zip_filename)[0]

    unzip_path = os.path.join(dest_folder, unzip_folder_name)
    unzip_file(zip_path, unzip_path)

    return unzip_path

def find_file(directory, filename):
    '''
    在目录中查找指定文件
    :param directory: 要查找的目录
    :param filename: 要查找的文件名
    :return: 文件的完整路径, 如果未找到则返回None
    '''
    for root, dirs, files in os.walk(directory):
        for filename in files:
            return os.path.join(root, filename)
    return None
