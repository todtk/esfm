# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from scripts import data


class DataDecodeThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        QtCore.QThread.__init__(self, parent=parent)

        self.data = data.DataManager()

    def run(self):
        self.data.get_decode(self.mysignal)


class DataExtractThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        QtCore.QThread.__init__(self, parent=parent)
        
        self.data = data.DataManager()

    def run(self):
        self.data.get_extract(self.mysignal)


class TempExtractThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(dict)

    def __init__(self, temp, parent=None) -> None:
        QtCore.QThread.__init__(self, parent=parent)
        
    def run(self):
        ...


class CacheExtractThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(dict)

    def __init__(self, cache, parent=None) -> None:
        QtCore.QThread.__init__(self, parent=parent)
        
    def run(self):
        ...
