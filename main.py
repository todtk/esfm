# -*- coding: utf-8 -*-

import os, pathlib

from data_decrypt import Decryptor
from temp_extract import Extractor


CLIENT_PATH = os.path.join(os.getcwd(), "client", "")
FILES_PATH = os.path.join(os.getcwd(), "client", "files", "")
TEMP_PATH = os.path.join(CLIENT_PATH, "files", "temp", "inet", "")
DATA_PATH = os.path.join(CLIENT_PATH, "files", "data", "")

class Launcher():

    def __init__(self) -> None:
        ...

    def check_client(self) -> None:

        if not os.path.exists(CLIENT_PATH):
            pathlib.Path(CLIENT_PATH).mkdir(parents=True, exist_ok=True)

    def data_decrypt(self) -> None:
        if Decryptor.decrypt(FILES_PATH):
            print("DECRYPT COMPLETE")
        else:
            print("UNKNOWN ERROR")



if __name__ == "__main__":
    Extractor.extract(client_path=CLIENT_PATH)
