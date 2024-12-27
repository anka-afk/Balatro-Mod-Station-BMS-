# 下载逻辑模块 从GitHub获取文件
# 1. 下载指定URL文件到本地 检查文件是否已经存在避免重复 多线程下载

import  requests
import os

def download_file(url, dest_path):
    print(f"开始下载: {url}")
    if os.path.exists(dest_path):
        return "文件已存在"
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查 HTTP 状态码

        print(f"响应头: {response.headers}")
        content_type = response.headers.get('Content-Type', '')

        if not any(allowed in content_type for allowed in ['application/zip', 'application/octet-stream']):
            raise Exception(f"下载的文件类型错误: {content_type}")

        with open(dest_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"下载完成: {dest_path}")
        return "下载完成"
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        return f"下载失败: {e}"
