# -*- coding: utf-8 -*-

import os
import sys
import pathlib
from PyQt5 import QtWidgets
from ui.window import AppWindow


class ESFM():
    __version__: float = 0.04

    def __init__(self) -> None:

        self.app = QtWidgets.QApplication(sys.argv)
        self.window = AppWindow(self.__version__)


if __name__ == "__main__":

    pathlib.Path(os.path.join(os.getcwd(), 'client', 'cache')).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(os.getcwd(), 'client', 'files', 'temp')).mkdir(parents=True, exist_ok=True)

    esfm = ESFM()

    esfm.window.show()
    sys.exit(esfm.app.exec_())
