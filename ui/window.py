# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from .elems import WindowElems
from .slots import WindowSlots


class AppWindow(QtWidgets.QWidget):

    def __init__(self, data, parent = None) -> None: 

        QtWidgets.QWidget.__init__(self, parent)

        self.ui = WindowElems()
        self.ui.setupUi(self)

        self.obj = WindowSlots(self.ui, data)
        self.obj.get_all_checks()

        # refresh buttons
        self.ui.data_button_1_2.clicked.connect(self.obj.get_check_pack)
        self.ui.data_button_2_2.clicked.connect(self.obj.get_check_pck)
        # self.ui.temp_button_1_2.clicked.connect(self.obj.get_check_temp)
        # self.ui.cache_button_1_2.clicked.connect(self.obj.get_check_cache)

        # functional buttons
        self.ui.data_button.clicked.connect(self.obj.decode_data)
        self.ui.data_button_2.clicked.connect(self.obj.extract_data)