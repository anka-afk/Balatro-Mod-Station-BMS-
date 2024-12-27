# 通用工具
# 文件夹检查 创建 解压缩 下载状态进度条

import  os
import zipfile

def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def unzip_file(zip_path,dest_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)