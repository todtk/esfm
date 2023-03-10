# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class DataDecoderThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, data, parent = None) -> None:
        QtCore.QThread.__init__(self, parent = parent)

    def run(self):
        ...


class DataExtractThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, data, parent = None) -> None:
        QtCore.QThread.__init__(self, parent = parent)
        
    def run(self):
        ...
