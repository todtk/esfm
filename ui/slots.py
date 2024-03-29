# -*- coding: utf-8 -*-

from app import file, folder
from .threads import *


class WindowSlots(QtCore.QObject):

    def __init__(self, ui):
        QtCore.QObject.__init__(self)

        self.ui = ui

        self.dd_thread = DataDecodeThread()
        self.dd_thread.started.connect(self.decode_data_started)
        self.dd_thread.finished.connect(self.decode_data_finished)
        self.dd_thread.mysignal.connect(self.decode_data_change, QtCore.Qt.QueuedConnection)

        self.de_thread = DataExtractThread()
        self.de_thread.started.connect(self.extract_data_started)
        self.de_thread.finished.connect(self.extract_data_finished)
        self.de_thread.mysignal.connect(self.extract_data_change, QtCore.Qt.QueuedConnection)

        self.te_thread = TempExtractThread()
        self.te_thread.started.connect(self.extract_temp_started)
        self.te_thread.finished.connect(self.extract_temp_finished)
        self.te_thread.mysignal.connect(self.extract_temp_change, QtCore.Qt.QueuedConnection)

    def check_all(self):
        self.check_data1()
        self.check_data2()
        self.check_temp()
        self.check_cache()

    # TAB_DATA
    # DECODE
    def check_data1(self) -> None:
        """check data pack file, swicth buttons status"""
        if file.exists(data.encoded_file_path):
            self.ui.button_data_decode.setEnabled(True)
            self.ui.label_data_decode.setText("ready")
        else:
            self.ui.button_data_decode.setDisabled(True)
            self.ui.label_data_decode.setText('"./client/files/data.pack" not found')

        self.ui.button_data_decode_refresh.setEnabled(True)
        self.ui.progressbar_data_decode.setProperty("value", 0)

    def decode_data_clicked(self) -> None:
        """disable buttons, change window status"""
        self.ui.button_data_decode.setDisabled(True)
        self.ui.button_data_extract.setDisabled(True)
        self.ui.button_data_decode_refresh.setDisabled(True)
        self.ui.button_data_extract_refresh.setDisabled(True)
        self.dd_thread.start()

    def decode_data_started(self) -> None:
        """change window status"""
        self.ui.label_data_decode.setText("decoding...")

    def decode_data_finished(self) -> None:
        """enable buttons, change window status"""
        if self.ui.checkbox_data_decode_delete_after.checkState() == 2:
            file.delete(data.encoded_file_path)

        self.check_all()

        self.ui.progressbar_data_decode.setProperty("value", 100)
        self.ui.label_data_decode.setText("decoded")

    def decode_data_change(self, current_percent: int) -> None:
        self.ui.progressbar_data_decode.setProperty("value", current_percent)

    # EXTRACT
    def check_data2(self) -> None:
        """check data.pck file, swicth buttons status"""
        if file.exists(data.decoded_file_path):
            self.ui.button_data_extract.setEnabled(True)
            self.ui.label_data_extract.setText("ready")
        else:
            self.ui.button_data_extract.setDisabled(True)
            self.ui.label_data_extract.setText('"./client/files/data.pck" not found')

        self.ui.button_data_extract_refresh.setEnabled(True)
        self.ui.progressbar_data_extract.setProperty("value", 0)

    def extract_data_clicked(self) -> None:
        """disable buttons, start extract"""
        self.ui.button_data_decode.setDisabled(True)
        self.ui.button_data_extract.setDisabled(True)
        self.ui.button_data_decode_refresh.setDisabled(True)
        self.ui.button_data_extract_refresh.setDisabled(True)
        self.de_thread.start()

    def extract_data_started(self) -> None:
        """change window status"""
        self.ui.label_data_extract.setText("extracting...")

    def extract_data_change(self, cur_persent: int) -> None:
        self.ui.progressbar_data_extract.setProperty("value", cur_persent)

    def extract_data_finished(self) -> None:
        """enable buttons, change window status"""
        if self.ui.checkbox_data_extract_delete_after.checkState() == 2:
            file.delete(data.decoded_file_path)

        if self.ui.checkbox_data_open_logs_folder.checkState() == 2:
            folder.open('logs')

        if self.ui.checkbox_data_open_data_folder.checkState() == 2:
            folder.open(data.data_folder_path)

        self.check_all()

        self.ui.progressbar_data_extract.setProperty("value", 100)
        self.ui.label_data_extract.setText("extracted")

    # TAB_TEMP
    def check_temp(self):

        if folder.exists(temp.temp_folder_path):
            self.ui.button_temp_extract.setEnabled(True)
            self.ui.label_temp_extract.setText("ready")
        else:
            self.ui.button_temp_extract.setDisabled(True)
            self.ui.label_temp_extract.setText("not ready")

        self.ui.button_temp_extract_refresh.setEnabled(True)
        self.ui.progressbar_temp_extract.setProperty("value", 0)

    def extract_temp_clicked(self) -> None:
        """disable buttons, start extract"""
        self.ui.button_temp_extract.setDisabled(True)
        self.ui.button_temp_extract_refresh.setDisabled(True)
        self.te_thread.start()

    def extract_temp_started(self) -> None:
        """change window status"""
        self.ui.label_temp_extract.setText("extracting...")

    def extract_temp_change(self, cur_persent: int) -> None:
        self.ui.progressbar_temp_extract.setProperty("value", cur_persent)

    def extract_temp_finished(self) -> None:
        self.check_all()

        self.ui.progressbar_temp_extract.setProperty("value", 100)
        self.ui.label_temp_extract.setText("extracted")

    # TAB_CACHE
    def check_cache(self):
        self.ui.label_cache_extract.setText("dev in progress")
    #     if self.cache.check_files():
    #         self.ui.button_cache_extract.setEnabled(True)
    #         self.ui.label_cache_extract.setText("<files found>")
    #     else:
    #         self.ui.button_cache_extract.setDisabled(True)
    #         self.ui.label_cache_extract.setText("<files not found>")
