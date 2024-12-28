# 启动GUI 入口

from gui import start_gui
from mods_manager import ModManager

if __name__ == '__main__':
    print("=-=-=-=-==-=-=-=-=Balatro Mod Station=-=-=-=-==-=-=-=-=")
    start_gui()
    print("=-=-=-=-==-=-=-=-=Loading mods=-=-=-=-==-=-=-=-=")
    ModManager.load_mods()