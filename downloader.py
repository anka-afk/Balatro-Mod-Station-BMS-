import requests
import os
import threading
from logger import Logger

def download_file(url, dest_folder):
    '''
    下载指定 URL 文件到本地（非阻塞，默认创建新线程）
    :param url: 下载链接
    :param dest_folder: 目标文件夹路径
    :return: 下载结果信息
    '''
    def _download():
        try:
            # 获取文件名
            filename = os.path.basename(url)
            dest_path = os.path.join(dest_folder, filename)

            # 发起请求
            response = requests.get(url, stream=True)
            response.raise_for_status()  # 检查 HTTP 状态码

            Logger.info(f"响应头: {response.headers}")
            content_type = response.headers.get('Content-Type', '')

            # 检查文件类型
            if not any(allowed in content_type for allowed in ['application/zip', 'application/octet-stream']):
                raise Exception(f"下载的文件类型错误: {content_type}")

            # 写入文件
            with open(dest_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            Logger.info(f"下载完成: {dest_path}")
            return dest_path
        except requests.exceptions.RequestException as e:
            Logger.error(f"下载失败: {e}")
            raise Exception(f"下载失败: {e}")
        finally:
            # 线程执行完毕后自动回收
            Logger.info(f"线程已回收: {threading.current_thread().name}")

    # 创建并启动线程
    thread = threading.Thread(target=_download, name=f"DownloadThread-{os.path.basename(url)}")
    thread.start()
    thread.join()  # 等待线程执行完成

    # 返回下载结果
    return _download()