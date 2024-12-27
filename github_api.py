# GitHub API交互模块 获取模组最新版本
# 调用API获取最新发行版信息 获取发行版的下载URL

from github import Github

def get_latest_release(repo_name, return_version=False):
    g = Github()
    try:
        repo = g.get_repo(repo_name)
        release = repo.get_latest_release()

        for asset in release.assets:
            if "windows" in asset.name.lower() or "msvc" in asset.name.lower():
                print(f"找到适合的发行版文件: {asset.name}")
                if return_version:
                    return asset.browser_download_url, release.tag_name
                return asset.browser_download_url

        raise Exception("没有找到适合的文件")
    except Exception as e:
        raise Exception(f"获取发行版信息失败: {e}")