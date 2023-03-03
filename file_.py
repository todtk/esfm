# -*- coding: utf-8 -*-

import os, mmap, platform, pathlib


def check_file(file_path: str, length_container: int) -> bool:

    if os.path.exists(file_path):
        if os.path.getsize(file_path) == length_container:
            return False

    return True

def open_file(file_path: str, write = False) -> int:
        
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

def write_file(path: str, container: bytes) -> bool:

    parent_path = path[:-(len(path.split("\\")[-1]))]
    pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)

    if check_file(path, len(container)):
        file = open_file(path, write=True)

        if file > 0:
            os.truncate(file, 0)

        os.write(file, container)
        os.close(file)
        return True

    else:
        return False

def open_memory(file: int, length: int, offset: int = 0) -> mmap.mmap:

    if platform.system() == 'Windows':
        memory = mmap.mmap(file, length=length, offset=offset, access=mmap.ACCESS_READ)
    else:
        memory = mmap.mmap(file, length=length, offset=offset, prot=mmap.PROT_READ)

    return memory