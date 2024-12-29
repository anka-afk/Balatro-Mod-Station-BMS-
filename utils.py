# 通用工具
# 文件夹检查 创建 解压缩 下载状态进度条

import  os
import zipfile
import  json
from operator import truediv

from config import Config

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
