# -*- coding: utf-8 -*-

import os, mmap, platform, pathlib


class File_Manager():

    def __init__(self) -> None:
        ...

    @classmethod
    def open_file(self, file_path: str, write = False) -> int:
        
        if platform.system() == 'Windows':
            if write is True:
                file = os.open(file_path, os.O_CREAT | os.O_RDWR | os.O_BINARY)
            else:
                file = os.open(file_path, os.O_RDONLY | os.O_BINARY)
        else:
            if write is True:
                file = os.open(file_path, os.O_CREAT | os.O_RDWR)
            else:
                file = os.open(file_path, os.O_RDONLY)

        return file

    @classmethod
    def check_file(self, file_path: str, byte_count: int) -> bool:

        if os.path.exists(file_path):
            if os.path.getsize(file_path) == byte_count:
                return False

        return True

    @classmethod
    def write_file(self, file_path: str, file_content: bytes) -> None:

        path = file_path[:-(len(file_path.split("\\")[-1]))]
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

        if self.check_file(file_path, len(file_content)):
            file = self.open_file(file_path, write=True)

            if file > 0:
                os.truncate(file, 0)

            os.write(file, file_content)
            print(f"EXTRACT: {file_path}")
            os.close(file)
        else:
            pass

    @classmethod
    def open_memory(self, file: int, length: int, offset: int = 0) -> mmap:

        if platform.system() == 'Windows':
            memory = mmap.mmap(file, length=length, offset=offset, access=mmap.ACCESS_READ)
        else:
            memory = mmap.mmap(file, length=length, offset=offset, prot=mmap.PROT_READ)

        return memory