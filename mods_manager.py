# 模组管理模块 Mods文件夹的增删查
# 列出Mods下所有模组 添加模组 解压缩压缩包并安装到Mods

import  os
import  shutil
from  utils import *
from config import Config
from github_api import get_latest_release

def list_mods(mods_folder):
    return  [f for f in os.listdir(mods_folder) if os.path.isdir(os.path.join(mods_folder, f))]

def add_mod(source_path, mods_folder):
    if source_path.endswith(".zip"):
        from utils import  unzip_file
        unzip_file(source_path, mods_folder)

    else:
        shutil.copytree(source_path, os.path.join(mods_folder, os.path.basename(source_path)))
    return  "模组添加完成"

class ModManager:
    '''
    :mods:一个字典, 键为mod名称(非repo名称), 值为一个字典mods_info, 维护mod的各种信息(版本, repo名等)
    '''
    _mods = {}

    @property
    def mods(self):
        return self._mods

    @mods.setter
    def mods(self, mods):
        self._mods = mods
        self.save_mods()

    @classmethod
    def load_mods(cls):
        '''
        :return:从config.json读取mods字典
        '''
        try:
            if os.path.exists(Config.config_path):
                config = load_config()
                cls.mods = config.get('mods', {})
            else:
                cls.mods = {}
        except Exception as e:
            print(f"加载mod信息失败: {e}")
            cls.mods = {}

    @classmethod
    def save_mods(cls):
        '''
        :return:保存变量信息到config.json
        '''
        try:
            config = load_config()
            config['mods'] = cls.mods
            save_config(config)
        except Exception as e:
            print(f"保存版本信息失败: {e}")

    @classmethod
    def get_mod_info(cls, mod_name):
        '''
        :param mod_name: 模组名称
        :return: 模组信息
        '''
        return cls.mods.get(mod_name)

    @classmethod
    def set_mod_info(cls, mod_name, mod_info):
        '''

        :param mod_name: 模组名称
        :param mod_info: 模组信息(版本, repo名等)
        :return: 保存信息到文件和变量
        '''
        cls.mods[mod_name] = mod_info
        cls.save_mods()

    @classmethod
    def get_mods_to_update(cls):
        '''
        :return: 一个列表，包含需要更新的模组及其版本信息。
                 每个元素是一个字典 {mod_name, current_version, latest_version}
        '''
        mods_to_update = []
        mods = cls.mods

        for mod_name, mod_info in mods.items():
            try:
                _, latest_version = get_latest_release(mod_info["repo_name"], return_version=True)
                current_version = mod_info.get("version")
                if current_version != latest_version:
                    mods_to_update.append({
                        "mod_name":mod_name,
                        "current_version":current_version,
                        "latest_version":latest_version,
                    })
            except Exception as e:
                print(f"检查模组 {mod_name} 更新失败: {e}")

        return mods_to_update



