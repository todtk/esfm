# -*- coding: utf-8 -*-

import os, pathlib
from data_ import DataManager
from temp_ import TempManager


CLIENT_PATH = os.path.join(os.getcwd(), "client", "")


class ESManager():

    def __init__(self) -> None:
        pathlib.Path(CLIENT_PATH).mkdir(parents=True, exist_ok=True)

    def get_start_window(self):
        ...

    def get_statusbar(self):
        ...

    def get_header(self):
        ...


esm = ESManager()
dm = DataManager(client_path=CLIENT_PATH)
tm = TempManager(client_path=CLIENT_PATH)


if __name__ == "__main__":

    if dm.start_decrypting():
        print("DECRYPTING COMPLETE")
    else:
        print("DECRYPTING ERROR")

    if dm.start_extracting():
        print("EXTRACTING COMPLETE")
    else:
        print("EXTRACTING ERROR")
