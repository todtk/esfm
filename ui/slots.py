# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class WindowSlots(QtCore.QObject):

    def __init__(self, ui, data):
        QtCore.QObject.__init__(self)

        self.ui = ui

        self.data = data

    def get_all_checks(self):
        self.get_check_pack()
        self.get_check_pck()
        self.get_check_temp()
        self.get_check_cache()

    def get_check_pack(self):
        if self.data.check_datapack_file():
            self.ui.data_button.setEnabled(True)
            self.ui.data_label.setText("<files found>")
        else:
            self.ui.data_button.setDisabled(True)
            self.ui.data_label.setText("<files not found>")

    def get_check_pck(self):
        if self.data.check_datapck_file():
            self.ui.data_button_2.setEnabled(True)
            self.ui.data_label_2.setText("<files found>")
        else:
            self.ui.data_button_2.setDisabled(True)
            self.ui.data_label_2.setText("<files not found>")

    def get_check_temp(self):
        self.ui.temp_label.setText("<files not found>")
    #     if self.temp.check_files():
    #         self.ui.temp_button.setEnabled(True)
    #         self.ui.temp_label.setText("<files found>")
    #     else:
    #         self.ui.temp_button.setDisabled(True)
    #         self.ui.temp_label.setText("<files not found>")

    def get_check_cache(self):
        self.ui.cache_label.setText("<files not found>")
    #     if self.cache.check_files():
    #         self.ui.cache_button.setEnabled(True)
    #         self.ui.cache_label.setText("<files found>")
    #     else:
    #         self.ui.cache_button.setDisabled(True)
    #         self.ui.cache_label.setText("<files not found>")

    def decode_data(self):
        self.data.get_decode_datapack()

    def extract_data(self):
        self.data.get_extract_datapck()