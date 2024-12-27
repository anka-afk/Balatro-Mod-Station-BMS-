# 下载逻辑模块 从GitHub获取文件
# 1. 下载指定URL文件到本地 检查文件是否已经存在避免重复 多线程下载

import  requests
import os

def download_file(url,dest_path):
    if os.path.exists(dest_path):
        return "文件已存在"
    response = requests.get(url, stream=True)
    with open(dest_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    return "下载完成"