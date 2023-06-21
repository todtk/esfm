# -*- coding: utf-8 -*-

import os
import sys
import scripts
import pathlib
from PyQt5 import QtWidgets
from ui.window import AppWindow


class ESFM:
    __version__: float = 0.02

    def __init__(self) -> None:
        pathlib.Path(os.path.join(os.getcwd(), "client", "")).mkdir(parents=True, exist_ok=True)
        pathlib.Path(os.path.join(os.getcwd(), "logs", "")).mkdir(parents=True, exist_ok=True)

        data = scripts.DataManager()
        # temp = scripts.TempManager()
        # cache = scripts.CacheManager()

        self.app = QtWidgets.QApplication(sys.argv)
        self.window = AppWindow(self.__version__, data)


esfm = ESFM()

if __name__ == "__main__":
    esfm.window.show()
    sys.exit(esfm.app.exec_())
