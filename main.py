# -*- coding: utf-8 -*-

import sys, os, pathlib, scripts
from PyQt5 import QtWidgets
from ui.window import AppWindow


class ESFM():

    def __init__(self) -> None:

        pathlib.Path(os.path.join(os.getcwd(), "client", "")).mkdir(parents = True, exist_ok = True)

        data = scripts.DataManager()
        # temp = scripts.TempManager()
        # cache = scripts.CacheManager()

        self.app = QtWidgets.QApplication(sys.argv)
        self.window = AppWindow(data)


esfm = ESFM()


if __name__ == "__main__":

    esfm.window.show()
    sys.exit(esfm.app.exec_())