# -*- coding: utf-8 -*-

import os


class UserWindow():

    def __init__(self) -> None:
        self.width = 100

    @classmethod
    def get_window(self) -> None:

        os.system('cls')
    
    @classmethod
    def get_header(self) -> str:

        header = """
        ########  ########  ###     ###  by todtk                                                               \n
        ########  ########  ####   ####  v 0.1                                                                  \n
        ###       ###  ###  ##### #####                                                                         \n
        ###       ###       ###########                                                                         \n
        ########  ########  ###########                                                                         \n
        ########  ########  ### ### ###                                                                         \n
        ###            ###  ###  #  ###                                                                         \n
        ###       ###  ###  ###     ###                                                                         \n
        ########  ########  ###     ###                                                                         \n
        ########  ########  ###     ###                                                                         \n
        """.format()

        return header

    @classmethod
    def get_statusbar(self, curent: int, max: int) -> str:

        progress = ((max / self.width) / curent) * "\\"
        delimiter = "#" * self.width
        statusbar = """
        ##{}##\n
        ##{}##\n
        ##{}##\n
        """.format(delimiter, progress, delimiter)

        return statusbar
    
    @classmethod
    def get_description(self) -> str:

        description = """
        """.format()

        return description