# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from .threads import *


class WindowSlots(QtCore.QObject):

    def __init__(self, ui, data):
        QtCore.QObject.__init__(self)

        self.ui = ui

        self.data = data

        self.dd_thread = DataDecodeThread()
        self.dd_thread.started.connect(self.decode_data_started)
        self.dd_thread.finished.connect(self.decode_data_finished)
        self.dd_thread.mysignal.connect(self.decode_data_change, QtCore.Qt.QueuedConnection)

        self.de_thread = DataExtractThread()
        self.de_thread.started.connect(self.extract_data_started)
        self.de_thread.finished.connect(self.extract_data_finished)
        self.de_thread.mysignal.connect(self.extract_data_change, QtCore.Qt.QueuedConnection)

    def check_all(self):
        self.check_data1()
        self.check_data2()
        self.check_temp()
        self.check_cache()

    ####################################################################################################
    ### TAB_DATA                                                                                     ###
    ####################################################################################################

    # DECODE
    def check_data1(self) -> None:
        """check data.pack file, swicth buttons status"""
        if self.data.check_data1():
            self.ui.data_button.setEnabled(True)
            self.ui.data_label.setText("< ready >")
        else:
            self.ui.data_button.setDisabled(True)
            self.ui.data_label.setText("< copy file in 'client' folder >")

        self.ui.data_button_1_2.setEnabled(True)
        self.ui.data_progress.setProperty("value", 0)

    def decode_data_clicked(self) -> None:
        """disable buttons, change window status"""
        self.ui.data_button.setDisabled(True)
        self.ui.data_button_2.setDisabled(True)
        self.ui.data_button_1_2.setDisabled(True)
        self.ui.data_button_2_2.setDisabled(True)
        self.dd_thread.start()

    def decode_data_started(self) -> None:
        """change window status"""
        self.ui.data_label.setText("< decoding... >")

    def decode_data_finished(self) -> None:
        """enable buttons, change window status"""
        self.check_all()

        self.ui.data_progress.setProperty("value", 100)
        self.ui.data_label.setText("< decoded >")

    def decode_data_change(self, cur_persent: int) -> None:
        self.ui.data_progress.setProperty("value", cur_persent)

    # EXTRACT
    def check_data2(self) -> None:
        """check data.pck file, swicth buttons status"""
        if self.data.check_data2():
            self.ui.data_button_2.setEnabled(True)
            self.ui.data_label_2.setText("< ready >")
        else:
            self.ui.data_button_2.setDisabled(True)
            self.ui.data_label_2.setText("< pls decrypt first >")

        self.ui.data_button_2_2.setEnabled(True)
        self.ui.data_progress_2.setProperty("value", 0)

    def extract_data_clicked(self) -> None:
        """disable buttons, start extract"""
        self.ui.data_button.setDisabled(True)
        self.ui.data_button_2.setDisabled(True)
        self.ui.data_button_1_2.setDisabled(True)
        self.ui.data_button_2_2.setDisabled(True)
        self.de_thread.start()

    def extract_data_started(self) -> None:
        """change window status"""
        self.ui.data_label_2.setText("< extracting... >")

    def extract_data_finished(self) -> None:
        """enable buttons, change window status"""
        self.check_all()

        self.ui.data_progress_2.setProperty("value", 100)
        self.ui.data_label_2.setText("< extracted... >")

    def extract_data_change(self, cur_persent: int) -> None:
        self.ui.data_progress_2.setProperty("value", cur_persent)

    ####################################################################################################
    ### TAB_TEMP                                                                                     ###
    ####################################################################################################
    def check_temp(self):
        self.ui.temp_label.setText("< dev in progress >")
    #     if self.temp.check_files():
    #         self.ui.temp_button.setEnabled(True)
    #         self.ui.temp_label.setText("<files found>")
    #     else:
    #         self.ui.temp_button.setDisabled(True)
    #         self.ui.temp_label.setText("<files not found>")

    ####################################################################################################
    ### TAB_CACHE                                                                                    ###
    ####################################################################################################
    def check_cache(self):
        self.ui.cache_label.setText("< dev in progress >")
    #     if self.cache.check_files():
    #         self.ui.cache_button.setEnabled(True)
    #         self.ui.cache_label.setText("<files found>")
    #     else:
    #         self.ui.cache_button.setDisabled(True)
    #         self.ui.cache_label.setText("<files not found>")