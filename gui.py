# UI
# 1. 路径设置界面
# 2. Mods 文件夹管理界面
# 3. 联网模组下载界面
# 4. 状态栏显示

import  sys, os, json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog,
    QBoxLayout, QPushButton, QLabel,
    QVBoxLayout, QWidget, QMessageBox, QPlainTextEdit)
from config import Config
from logger import Logger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Balatro Mod Station BMS")
        self.setGeometry(300, 300, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 初始化界面
        layout = QVBoxLayout()

        # 是否存在配置
        if not(os.path.exists(Config.config_path)):

            self.auto_search_button = QPushButton("自动搜索游戏目录")
            self.auto_search_button.clicked.connect(self.auto_search_game_directory)
            layout.addWidget(self.auto_search_button)

            self.manual_select_button = QPushButton("手动选择游戏目录")
            self.manual_select_button.clicked.connect(self.manual_select_game_directory)
            layout.addWidget(self.manual_select_button)
        else:
            with open(Config.config_path, "r") as file:
                data = json.load(file)
                Config.game_directory = data["game_directory"]

        # 是否已安装lovely
        self.install_dll_button = QPushButton("安装 lovely")
        self.install_dll_button.clicked.connect(self.install_dll)
        layout.addWidget(self.install_dll_button)

        # 是否已安装Steammodded
        self.install_dll_button = QPushButton("安装 Steamodded")
        self.install_dll_button.clicked.connect(self.install_steamodded)
        layout.addWidget(self.install_dll_button)

        # 日志流
        self.log_widget = QPlainTextEdit(self)
        self.log_widget.setReadOnly(True)
        layout.addWidget(self.log_widget)

        # 应用样式
        central_widget.setLayout(layout)

    def install_dll(self):
        '''
        :return:调用installer安装lovely
        '''
        from installer import  install_version_dll
        result = install_version_dll(Config.game_directory)
        Logger.log(result)

    def install_steamodded(self):
        '''
        :return:调用installer安装steamodded
        '''
        from installer import install_loader_mods
        result = install_loader_mods(Config.mods_path)
        Logger.log(result)

    def auto_search_game_directory(self):
        '''
        :return: 自动搜索并设置游戏根目录
        '''
        # 常见的安装路径
        possible_paths = [
            r"C:\Program Files\steam\steamapps\common\Balatro",
            r"C:\steam\steamapps\common\Balatro",
            r"D:\steam\steamapps\common\Balatro",
            r"F:\steam\steamapps\common\Balatro"
        ]

        for path in possible_paths:
            if os.path.exists(os.path.join(path, "Balatro.exe")):
                Config.game_directory = path
                self.status_label.setText(f"找到游戏目录: {path}")
                QMessageBox.information(self, "成功", f"自动找到游戏目录：{path}")
                data = {"game_directory": Config.game_directory}
                with open("config.json", "w") as file:
                    json.dump(data, file, indent=4)
                return

        QMessageBox.warning(self, "未找到", "未能自动找到游戏目录，请手动选择。")

    def manual_select_game_directory(self):
        '''
        :return: 手动选择并设置游戏根目录
        '''
        selected_dir = QFileDialog.getExistingDirectory(self, "选择游戏目录", "")
        if selected_dir:
            if os.path.exists(os.path.join(selected_dir, "Balatro.exe")):
                Config.game_directory = selected_dir
                self.status_label.setText(f"手动选择游戏目录: {selected_dir}")
                QMessageBox.information(self, "成功", f"选择的游戏目录：{selected_dir}")
                data = {"game_directory": Config.game_directory}
                with open("config.json", "w") as file:
                    json.dump(data, file, indent=4)
            else:
                QMessageBox.warning(self, "错误", "所选目录中未找到 Balatro.exe，请重新选择。")

def start_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return  app, window

