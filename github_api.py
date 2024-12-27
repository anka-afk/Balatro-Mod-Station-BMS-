# GitHub API交互模块 获取模组最新版本
# 调用API获取最新发行版信息 获取发行版的下载URL

from github import Github

def get_latest_release(repo_name):
    g = Github()
    repo = g.get_repo(repo_name)
    release = repo.get_latest_release()
    return release.assets[0].browser_download_url # 最新发行版