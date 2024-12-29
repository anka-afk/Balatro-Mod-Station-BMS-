# GitHub API交互模块 获取模组最新版本
# 调用API获取最新发行版信息 获取发行版的下载URL

from github import Github
from  logger import Logger

def get_latest_release(repo_name, return_version=False):
    '''
    :param repo_name: 仓库名字
    :param return_version: 是否需要返回最新的发行版版本号
    :return: 最新合适的发行版的下载链接 版本号(可选)
    '''
    g = Github()
    try:
        repo = g.get_repo(repo_name)
        release = repo.get_latest_release()

        for asset in release.assets:
            if "windows" in asset.name.lower() or "msvc" in asset.name.lower():
                Logger.info(f"找到适合的发行版文件: {asset.name}")
                if return_version:
                    return asset.browser_download_url, release.tag_name
                return asset.browser_download_url

        raise Exception("没有找到适合的文件")
    except Exception as e:
        raise Exception(f"获取发行版信息失败: {e}")