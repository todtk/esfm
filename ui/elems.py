# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui


class WindowElems(object):

    def setupUi(self, Window):

        QtGui.QFontDatabase.addApplicationFont("./ui/fonts/Acumin Pro Semibold.ttf")
        style_sheet = """
            font: 8pt Acumin Pro;
            """
        
        Window.setObjectName("Window")
        Window.setFixedSize(500, 300)
        Window.setWindowTitle("Epic Seven File Manager")
        Window.setWindowIcon(QtGui.QIcon("./ui/images/icon.png"))
        Window.setWindowFlags(QtCore.Qt.Window)
        Window.setStyleSheet(style_sheet)

        self.TabMenu = QtWidgets.QTabWidget(Window)
        self.TabMenu.setEnabled(True)
        self.TabMenu.setGeometry(QtCore.QRect(5, 5, 490, 290))
        self.TabMenu.setObjectName("TabMenu")

        #######################################################################
        ### DATA                                                            ###
        #######################################################################
        self.data = QtWidgets.QWidget()
        self.data.setObjectName("data")

        # BUTTON_DECODE
        self.data_button = QtWidgets.QPushButton(self.data)
        self.data_button.setEnabled(False)
        self.data_button.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.data_button.setText("DECODE")
        self.data_button.setObjectName("data_button")

        # BUTTON_REFRESH
        self.data_button_1_2 = QtWidgets.QPushButton(self.data)
        self.data_button_1_2.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.data_button_1_2.setObjectName("data_button_1_2")

        # CHECKBOX_DELETE
        self.data_checkbox = QtWidgets.QCheckBox(self.data)
        self.data_checkbox.setGeometry(QtCore.QRect(10, 50, 450, 20))
        self.data_checkbox.setText("Delete data.pack after decoding")
        self.data_checkbox.setObjectName("data_checkbox")

        # STATUS_PROGRESSBAR
        self.data_progress = QtWidgets.QProgressBar(self.data)
        self.data_progress.setGeometry(QtCore.QRect(130, 10, 340, 30))
        self.data_progress.setProperty("value", 0)
        self.data_progress.setTextVisible(False)
        self.data_progress.setFormat("%p%")
        self.data_progress.setObjectName("data_progress")

        # STATUS_TEXT
        self.data_label = QtWidgets.QLabel(self.data)
        self.data_label.setGeometry(QtCore.QRect(300, 40, 170, 15))
        self.data_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.data_label.setObjectName("data_label")

        # BUTTON_EXTRACT
        self.data_button_2 = QtWidgets.QPushButton(self.data)
        self.data_button_2.setEnabled(False)
        self.data_button_2.setGeometry(QtCore.QRect(10, 80, 80, 30))
        self.data_button_2.setText("UNPACK")
        self.data_button_2.setObjectName("data_button_2")

        # BUTTON_REFRESH
        self.data_button_2_2 = QtWidgets.QPushButton(self.data)
        self.data_button_2_2.setGeometry(QtCore.QRect(90, 80, 30, 30))
        self.data_button_2_2.setObjectName("data_button_2_2")

        # CHECKBOX_DELETE
        self.data_checkbox_2 = QtWidgets.QCheckBox(self.data)
        self.data_checkbox_2.setGeometry(QtCore.QRect(10, 120, 450, 20))
        self.data_checkbox_2.setText("Delete data.pck after unpacking")
        self.data_checkbox_2.setObjectName("data_checkbox_2")

        # CHECKBOX_LOGS
        self.data_checkbox_2_2 = QtWidgets.QCheckBox(self.data)
        self.data_checkbox_2_2.setGeometry(QtCore.QRect(10, 140, 450, 20))
        self.data_checkbox_2_2.setText("Open log file after unpacking")
        self.data_checkbox_2_2.setObjectName("data_checkbox_2_2")

        # STATUS_PROGRESSBAR
        self.data_progress_2 = QtWidgets.QProgressBar(self.data)
        self.data_progress_2.setGeometry(QtCore.QRect(130, 80, 340, 30))
        self.data_progress_2.setProperty("value", 0)
        self.data_progress_2.setTextVisible(False)
        self.data_progress_2.setFormat("%p%")
        self.data_progress_2.setObjectName("data_progress_2")

        # STATUS_TEXT
        self.data_label_2 = QtWidgets.QLabel(self.data)
        self.data_label_2.setGeometry(QtCore.QRect(300, 110, 170, 15))
        self.data_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.data_label_2.setObjectName("data_label_2")

        self.TabMenu.addTab(self.data, "Data")

        #######################################################################
        ### TEMP                                                            ###
        #######################################################################
        self.temp = QtWidgets.QWidget()
        self.temp.setObjectName("temp")
        self.temp.setDisabled(True)

        # BUTTON_EXTRACT
        self.temp_button_1 = QtWidgets.QPushButton(self.temp)
        self.temp_button_1.setEnabled(False)
        self.temp_button_1.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.temp_button_1.setText("UNPACK")
        self.temp_button_1.setObjectName("temp_button_1")

        # BUTTON_REFRESH
        self.temp_button_1_2 = QtWidgets.QPushButton(self.temp)
        self.temp_button_1_2.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.temp_button_1_2.setObjectName("temp_button_1_2")

        # CHECKBOX_DELETE
        self.temp_checkbox_1 = QtWidgets.QCheckBox(self.temp)
        self.temp_checkbox_1.setGeometry(QtCore.QRect(10, 50, 450, 20))
        self.temp_checkbox_1.setText("Delete sourse files after unpaking")
        self.temp_checkbox_1.setObjectName("temp_checkbox_1")

        # STATUS_PROGRESSBAR
        self.temp_progress_1 = QtWidgets.QProgressBar(self.temp)
        self.temp_progress_1.setGeometry(QtCore.QRect(130, 10, 340, 30))
        self.temp_progress_1.setProperty("value", 0)
        self.temp_progress_1.setTextVisible(False)
        self.temp_progress_1.setFormat("%p%")
        self.temp_progress_1.setObjectName("temp_progress_1")

        # STATUS_TEXT
        self.temp_label = QtWidgets.QLabel(self.temp)
        self.temp_label.setGeometry(QtCore.QRect(300, 40, 170, 15))
        self.temp_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_label.setObjectName("temp_label")

        self.TabMenu.addTab(self.temp, "Temp")

        #######################################################################
        ### CACHE                                                           ###
        #######################################################################
        self.cache = QtWidgets.QWidget()
        self.cache.setObjectName("cache")
        self.cache.setDisabled(True)

        # BUTTON_EXTRACT
        self.cache_button_1 = QtWidgets.QPushButton(self.cache)
        self.cache_button_1.setEnabled(False)
        self.cache_button_1.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.cache_button_1.setText("UNPACK")
        self.cache_button_1.setObjectName("cache_button_1")

        # BUTTON_REFRESH
        self.cache_button_1_2 = QtWidgets.QPushButton(self.cache)
        self.cache_button_1_2.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.cache_button_1_2.setObjectName("cache_button_1_2")

        # CHECKBOX_EXTRACT
        self.cache_checkbox_1 = QtWidgets.QCheckBox(self.cache)
        self.cache_checkbox_1.setGeometry(QtCore.QRect(10, 50, 450, 20))
        self.cache_checkbox_1.setText("Delete sourse files after unpaking")
        self.cache_checkbox_1.setObjectName("cache_checkbox_1")

        # STATUS_PROGRESSBAR
        self.cache_progress_1 = QtWidgets.QProgressBar(self.cache)
        self.cache_progress_1.setGeometry(QtCore.QRect(130, 10, 340, 30))
        self.cache_progress_1.setProperty("value", 0)
        self.cache_progress_1.setTextVisible(False)
        self.cache_progress_1.setFormat("%p%")
        self.cache_progress_1.setObjectName("cache_progress_1")

        # STATUS_TEXT
        self.cache_label = QtWidgets.QLabel(self.cache)
        self.cache_label.setGeometry(QtCore.QRect(300, 40, 170, 15))
        self.cache_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cache_label.setObjectName("cache_label")
        
        self.TabMenu.addTab(self.cache, "Cache")
        self.TabMenu.setCurrentIndex(0)

        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(320, 280, 170, 15))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setText("by todtk")

        QtCore.QMetaObject.connectSlotsByName(Window)