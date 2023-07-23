# -*- coding: utf-8 -*-

import os
from mmap import mmap
from .file import file, folder, fmap


class Temp:

    def __init__(self) -> None:

        self.temp_folder_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "temp",
            ""
        )

    def get_path(self, _mmap: mmap):

        _mmap.seek(_mmap.find(b'\x68\x74\x74\x70') - 4)

        path = _mmap.read(
            int.from_bytes(
                bytes=_mmap.read(4),
                byteorder='little',
                signed=False)
        ).decode(
            "utf-8",
            "ignore"
        ).replace(
            "/",
            "\\"
        )

        if "world_kor\\" in path:
            return path.split("world_kor\\\\")[-1]
        else:
            return path.split("Live\\")[-1]

    def get_data(self, _mmap: mmap) -> bytes:
        _mmap.seek(0)
        _mmap.seek(
            int.from_bytes(
                bytes=_mmap.read(4),
                byteorder='little',
                signed=False
            )
        )

        return _mmap.read()

    def extract(self, signal) -> None:
        inet_folder = os.path.join(os.path.join(self.temp_folder_path, "inet"))
        folders = os.listdir(inet_folder)
        for folder_name in folders:
            signal.emit(int(folders.index(folder_name) / (len(folders) / 100)))
            for file_name in os.listdir(os.path.join(inet_folder, folder_name)):

                descriptor: int = file.get(
                    path=os.path.join(
                        inet_folder,
                        folder_name,
                        file_name),
                    write_mode=False
                )

                mmf: mmap = fmap.get(descriptor=descriptor)

                if mmf.size() == int.from_bytes(bytes=mmf.read(4), byteorder='little', signed=False):
                    mmf.close()
                    os.close(descriptor)
                    continue

                file.write(
                    path=os.path.join(
                        self.temp_folder_path,
                        self.get_path(_mmap=mmf).replace("/", "\\")
                    ),
                    container=self.get_data(
                        _mmap=mmf
                    )
                )

                mmf.close()
                os.close(descriptor)

            folder.delete(os.path.join(inet_folder, folder_name))


temp = Temp()
