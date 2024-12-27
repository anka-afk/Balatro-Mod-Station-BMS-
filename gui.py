# UI
# 1. 路径设置界面
# 2. Mods 文件夹管理界面
# 3. 联网模组下载界面
# 4. 状态栏显示

import  sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QBoxLayout, QPushButton, QLabel, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Balatro Mod Station BMS")
        self.setGeometry(300, 300, 800, 600)

        # 初始化界面
        layout = QVBoxLayout()
        self.status_label = QLabel("请选择游戏目录")
        layout.addWidget(self.status_label)

        self.install_dll_button = QPushButton("安装 version.all")
        self.install_dll_button.clicked.connect(self.install_dll)
        layout.addWidget(self.install_dll_button)


    def install_dll(self):
        # 调用installer
        from installer import  install_version_dll
        result = install_version_dll()
        self.status_label.setText(result)

def start_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

