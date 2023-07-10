# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from app import data


class DataDecodeThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        QtCore.QThread.__init__(self, parent=parent)

    def run(self):
        data.decode(self.mysignal)


class DataExtractThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        QtCore.QThread.__init__(self, parent=parent)

    def run(self):
        data.extract(self.mysignal)


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
