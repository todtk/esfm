# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from .elems import WindowElems
from .slots import WindowSlots


class AppWindow(QtWidgets.QWidget):

    def __init__(self, version: float, parent=None) -> None:

        QtWidgets.QWidget.__init__(self, parent)

        self.version = version

        self.ui = WindowElems()
        self.ui.setup_ui(self)

        self.obj = WindowSlots(ui=self.ui)
        self.obj.check_all()

        # refresh buttons
        self.ui.button_data_decode_refresh.clicked.connect(self.obj.check_data1)
        self.ui.button_data_extract_refresh.clicked.connect(self.obj.check_data2)
        self.ui.button_temp_extract_refresh.clicked.connect(self.obj.check_temp)
        self.ui.button_cache_extract_refresh.clicked.connect(self.obj.check_cache)

        # functional buttons
        self.ui.button_data_decode.clicked.connect(self.obj.decode_data_clicked)
        self.ui.button_data_extract.clicked.connect(self.obj.extract_data_clicked)
        self.ui.button_temp_extract.clicked.connect(self.obj.extract_temp_clicked)
