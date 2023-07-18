# -*- coding: utf-8 -*-

import os
import mmap
import pathlib
import platform
from app.log import log


class File:

    def __init__(self) -> None:
        ...

    @log.wrapper('DEBUG')
    def exists(self, path: str) -> bool:

        if os.path.exists(path):
            return True

        return False

    @log.wrapper('DEBUG')
    def comparison(self, path: str, length_container: int) -> bool:

        if os.path.getsize(path) == length_container:
            return True

        return False

    @log.wrapper('DEBUG')
    def get(self, path: str, write_mode: bool = False) -> int:

        try:

            if platform.system() == 'Windows':
                if write_mode:
                    file_descriptor = os.open(path, os.O_CREAT | os.O_RDWR | os.O_BINARY)
                else:
                    file_descriptor = os.open(path, os.O_RDONLY | os.O_BINARY)

            else:
                if write_mode:
                    file_descriptor = os.open(path, os.O_CREAT | os.O_RDWR)
                else:
                    file_descriptor = os.open(path, os.O_RDONLY)

            return file_descriptor

        except FileNotFoundError:
            pass

    @log.wrapper('DEBUG')
    def open(self, path: str) -> bool:

        if os.path.isfile(path):
            os.system(path)
            return True
        return False

    @log.wrapper('INFO')
    def write(self, path: str, container: bytes) -> bool:

        parent_path = path[:-(len(path.split("\\")[-1]))]
        pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)

        if not self.exists(path):
            file_descriptor = self.get(path, write_mode=True)

            if file_descriptor > 0:
                os.truncate(file_descriptor, 0)

            os.write(file_descriptor, container)
            os.close(file_descriptor)
            return True

        else:
            return False

    @log.wrapper('DEBUG')
    def delete(self, path: str) -> None:
        os.remove(path)


class Folder:

    def __init__(self) -> None:
        ...

    @log.wrapper('DEBUG')
    def get(self, path: str):
        """ ... """
        ...

    @log.wrapper('DEBUG')
    def exists(self, path: str) -> bool:
        return not os.path.isfile(path)

    @log.wrapper('DEBUG')
    def create(self, path: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    @log.wrapper('DEBUG')
    def open(self, path: str) -> None:
        os.startfile(filepath=path, operation='open', show_cmd=1)

    @log.wrapper('DEBUG')
    def delete(self):
        """ ... """
        ...


class MMap:

    def __init__(self) -> None:
        ...

    @log.wrapper('DEBUG')
    def get(self, descriptor: int, length: int = 0, offset: int = 0, write: bool = False) -> mmap.mmap:
        """ ... """
        if platform.system() == 'Windows':
            if write:
                access = mmap.ACCESS_WRITE
            else:
                access = mmap.ACCESS_READ
        else:
            if write:
                access = mmap.PROT_WRITE
            else:
                access = mmap.PROT_READ

        memory_map = mmap.mmap(fileno=descriptor, length=length, offset=offset, access=access)

        return memory_map


file = File()
folder = Folder()
fmap = MMap()
