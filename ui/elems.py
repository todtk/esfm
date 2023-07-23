# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui


class WindowElems(object):

    def setup_ui(self, window) -> None:
        QtGui.QFontDatabase.addApplicationFont("./ui/fonts/Acumin Pro Semibold.ttf")
        style_sheet = """font: 8pt Acumin Pro;"""

        window.setObjectName("window")
        window.setFixedSize(500, 300)
        window.setWindowTitle(f"Epic Seven File Manager")
        window.setWindowIcon(QtGui.QIcon("./ui/images/icon.png"))
        window.setWindowFlags(QtCore.Qt.Window)
        window.setStyleSheet(style_sheet)

        self.tab_menu = QtWidgets.QTabWidget(window)
        self.tab_menu.setEnabled(True)
        self.tab_menu.setGeometry(QtCore.QRect(5, 5, 490, 290))
        self.tab_menu.setObjectName("tab_menu")

        # DATA
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")

        self.button_data_decode = QtWidgets.QPushButton(self.data_tab)
        self.button_data_decode.setEnabled(False)
        self.button_data_decode.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.button_data_decode.setText("DECODE")
        self.button_data_decode.setObjectName("button_data_decode")

        self.button_data_decode_refresh = QtWidgets.QPushButton(self.data_tab)
        self.button_data_decode_refresh.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.button_data_decode_refresh.setText("⭯")
        self.button_data_decode_refresh.setObjectName("button_data_decode_refresh")

        self.checkbox_data_decode_delete_after = QtWidgets.QCheckBox(self.data_tab)
        self.checkbox_data_decode_delete_after.setGeometry(QtCore.QRect(10, 50, 450, 20))
        self.checkbox_data_decode_delete_after.setText("Delete encoded archive after decoding")
        self.checkbox_data_decode_delete_after.setObjectName("checkbox_data_decode_delete_after")

        self.progressbar_data_decode = QtWidgets.QProgressBar(self.data_tab)
        self.progressbar_data_decode.setGeometry(QtCore.QRect(130, 10, 340, 30))
        self.progressbar_data_decode.setProperty("value", 0)
        self.progressbar_data_decode.setTextVisible(False)
        self.progressbar_data_decode.setFormat("%p%")
        self.progressbar_data_decode.setObjectName("progressbar_data_decode")

        self.label_data_decode = QtWidgets.QLabel(self.data_tab)
        self.label_data_decode.setGeometry(QtCore.QRect(250, 40, 220, 15))
        self.label_data_decode.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_data_decode.setObjectName("label_data_decode")

        self.button_data_extract = QtWidgets.QPushButton(self.data_tab)
        self.button_data_extract.setEnabled(False)
        self.button_data_extract.setGeometry(QtCore.QRect(10, 80, 80, 30))
        self.button_data_extract.setText("UNPACK")
        self.button_data_extract.setObjectName("button_data_extract")

        self.button_data_extract_refresh = QtWidgets.QPushButton(self.data_tab)
        self.button_data_extract_refresh.setGeometry(QtCore.QRect(90, 80, 30, 30))
        self.button_data_extract_refresh.setText("⭯")
        self.button_data_extract_refresh.setObjectName("button_data_extract_refresh")

        self.checkbox_data_extract_delete_after = QtWidgets.QCheckBox(self.data_tab)
        self.checkbox_data_extract_delete_after.setGeometry(QtCore.QRect(10, 120, 450, 20))
        self.checkbox_data_extract_delete_after.setText("Delete decoded archive after unpacking")
        self.checkbox_data_extract_delete_after.setObjectName("checkbox_data_extract_delete_after")

        self.checkbox_data_open_logs_folder = QtWidgets.QCheckBox(self.data_tab)
        self.checkbox_data_open_logs_folder.setGeometry(QtCore.QRect(10, 140, 450, 20))
        self.checkbox_data_open_logs_folder.setText("Open log file after unpacking")
        self.checkbox_data_open_logs_folder.setObjectName("checkbox_data_open_logs_folder")

        self.checkbox_data_open_data_folder = QtWidgets.QCheckBox(self.data_tab)
        self.checkbox_data_open_data_folder.setGeometry(QtCore.QRect(10, 160, 450, 20))
        self.checkbox_data_open_data_folder.setText("Open data folder after unpacking")
        self.checkbox_data_open_data_folder.setObjectName("checkbox_data_open_data_folder")

        self.progressbar_data_extract = QtWidgets.QProgressBar(self.data_tab)
        self.progressbar_data_extract.setGeometry(QtCore.QRect(130, 80, 340, 30))
        self.progressbar_data_extract.setProperty("value", 0)
        self.progressbar_data_extract.setTextVisible(False)
        self.progressbar_data_extract.setFormat("%p%")
        self.progressbar_data_extract.setObjectName("progressbar_data_extract")

        self.label_data_extract = QtWidgets.QLabel(self.data_tab)
        self.label_data_extract.setGeometry(QtCore.QRect(250, 110, 220, 15))
        self.label_data_extract.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_data_extract.setObjectName("label_data_extract")

        self.tab_menu.addTab(self.data_tab, "Data")

        # TEMP
        self.temp_tab = QtWidgets.QWidget()
        self.temp_tab.setObjectName("temp_tab")

        self.button_temp_extract = QtWidgets.QPushButton(self.temp_tab)
        self.button_temp_extract.setEnabled(False)
        self.button_temp_extract.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.button_temp_extract.setText("UNPACK")
        self.button_temp_extract.setObjectName("button_temp_extract")

        self.button_temp_extract_refresh = QtWidgets.QPushButton(self.temp_tab)
        self.button_temp_extract_refresh.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.button_temp_extract_refresh.setText("⭯")
        self.button_temp_extract_refresh.setObjectName("button_temp_extract_refresh")

        self.progressbar_temp_extract = QtWidgets.QProgressBar(self.temp_tab)
        self.progressbar_temp_extract.setGeometry(QtCore.QRect(130, 10, 340, 30))
        self.progressbar_temp_extract.setProperty("value", 0)
        self.progressbar_temp_extract.setTextVisible(False)
        self.progressbar_temp_extract.setFormat("%p%")
        self.progressbar_temp_extract.setObjectName("progressbar_temp_extract")

        self.label_temp_extract = QtWidgets.QLabel(self.temp_tab)
        self.label_temp_extract.setGeometry(QtCore.QRect(300, 40, 170, 15))
        self.label_temp_extract.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_temp_extract.setObjectName("label_temp_extract")

        self.tab_menu.addTab(self.temp_tab, "Temp")

        # CACHE
        self.cache_tab = QtWidgets.QWidget()
        self.cache_tab.setObjectName("cache_tab")
        self.cache_tab.setDisabled(True)

        self.button_cache_extract = QtWidgets.QPushButton(self.cache_tab)
        self.button_cache_extract.setEnabled(False)
        self.button_cache_extract.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.button_cache_extract.setText("UNPACK")
        self.button_cache_extract.setObjectName("button_cache_extract")

        self.button_cache_extract_refresh = QtWidgets.QPushButton(self.cache_tab)
        self.button_cache_extract_refresh.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.button_cache_extract_refresh.setText("⭯")
        self.button_cache_extract_refresh.setObjectName("button_cache_extract_refresh")

        self.checkbox_cache_extract = QtWidgets.QCheckBox(self.cache_tab)
        self.checkbox_cache_extract.setGeometry(QtCore.QRect(10, 50, 450, 20))
        self.checkbox_cache_extract.setText("Delete sourse files after unpaking")
        self.checkbox_cache_extract.setObjectName("checkbox_cache_extract")

        self.progressbar_cache_extract = QtWidgets.QProgressBar(self.cache_tab)
        self.progressbar_cache_extract.setGeometry(QtCore.QRect(130, 10, 340, 30))
        self.progressbar_cache_extract.setProperty("value", 0)
        self.progressbar_cache_extract.setTextVisible(False)
        self.progressbar_cache_extract.setFormat("%p%")
        self.progressbar_cache_extract.setObjectName("progressbar_cache_extract")

        self.label_cache_extract = QtWidgets.QLabel(self.cache_tab)
        self.label_cache_extract.setGeometry(QtCore.QRect(300, 40, 170, 15))
        self.label_cache_extract.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_cache_extract.setObjectName("label_cache_extract")

        self.tab_menu.addTab(self.cache_tab, "Cache")
        self.tab_menu.setCurrentIndex(0)

        self.label_owner = QtWidgets.QLabel(window)
        self.label_owner.setGeometry(QtCore.QRect(315, 275, 170, 15))
        self.label_owner.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_owner.setObjectName("label_owner")
        self.label_owner.setText("by todtk")

        QtCore.QMetaObject.connectSlotsByName(window)
