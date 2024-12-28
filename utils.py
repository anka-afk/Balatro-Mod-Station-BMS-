# 通用工具
# 文件夹检查 创建 解压缩 下载状态进度条

import  os
import zipfile
import  json
from operator import truediv

from config import Config

def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def unzip_file(zip_path,dest_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)

def load_config():
    if os.path.exists(Config.config_path):
        with open(Config.config_path, "r") as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(Config.config_path, "w") as file:
        json.dump(config, file, indent=4)

def update_config(key, value):
    config = load_config()

    if key in config:
        config[key] = value
        save_config(config)
        return  True
    else:
        return False
