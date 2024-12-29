# 启动GUI 入口
import sys, os
from gui import start_gui
from logger import Logger
from mods_manager import ModManager
from config import Config

if __name__ == '__main__':
    Config.mods_path = os.path.join(os.getenv("APPDATA"),"Balatro","Mods")
    app, window = start_gui()
    Logger.set_log_widget(window.log_widget)
    Logger.info(message="=-=-=-=-==-=-=-=-=Balatro Mod Station=-=-=-=-==-=-=-=-=")
    Logger.info(message="=-=-=-=-==-=-=-=-=Loading mods=-=-=-=-==-=-=-=-=")
    ModManager.load_mods()
    sys.exit(app.exec())