# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from .elems import WindowElems
from .slots import WindowSlots


class AppWindow(QtWidgets.QWidget):

    def __init__(self, data, parent = None) -> None: 

        QtWidgets.QWidget.__init__(self, parent)

        self.ui = WindowElems()
        self.ui.setupUi(self)

        self.obj = WindowSlots(ui=self.ui, data=data)
        self.obj.check_all()

        # refresh buttons
        self.ui.data_button_1_2.clicked.connect(self.obj.check_data1)
        self.ui.data_button_2_2.clicked.connect(self.obj.check_data2)
        self.ui.temp_button_1_2.clicked.connect(self.obj.check_temp)
        self.ui.cache_button_1_2.clicked.connect(self.obj.check_cache)

        # functional buttons
        self.ui.data_button.clicked.connect(self.obj.decode_data_clicked)
        self.ui.data_button_2.clicked.connect(self.obj.extract_data_clicked)