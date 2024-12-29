import  sys
from enum import auto
from enum import Enum, auto

from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QApplication


class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()

class Logger:
    _log_widget = None

    @classmethod
    def set_log_widget(cls, log_widget):
        cls._log_widget = log_widget

    @classmethod
    def log(cls, message, level=LogLevel.INFO):
        # 格式化日志
        timestamp = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        log_message = f"[{timestamp}] [{level.name}] {message}"

        # 输出到控制台
        print(log_message)

        # 输出到logger
        if cls._log_widget is not None:
            cls._log_widget.appendPlainText(log_message)
            cls._log_widget.repaint()
            QApplication.processEvents()

    @classmethod
    def debug(cls, message):
        cls.log(message, LogLevel.DEBUG)

    @classmethod
    def info(cls, message):
        cls.log(message, LogLevel.INFO)

    @classmethod
    def warning(cls, message):
        cls.log(message, LogLevel.WARNING)

    @classmethod
    def error(cls, message):
        cls.log(message, LogLevel.ERROR)


