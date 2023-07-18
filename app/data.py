# -*- coding: utf-8 -*-

import os
from mmap import mmap
from app.log import log
from itertools import cycle
from .file import file, folder, fmap


class Data:
    def __init__(self) -> None:

        self.encoded_file_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "data.pack"
        )

        self.decoded_file_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "data.plp"
        )

        self.data_folder_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "data"
        )

    # DECODER
    @staticmethod
    def xor(value: bytes, key: bytes) -> bytes:  # checked
        return bytes(a ^ b for a, b in zip(value, cycle(key)))

    @log.wrapper('DEBUG')
    def decode(self, signal) -> bool:  # checked

        self.encoded_file: int = file.get(
            path=self.encoded_file_path
        )

        if self.encoded_file is None:
            raise FileNotFoundError

        key = b'\x21\x0c\xed\x10\xd8\x81\xd7\xa3\xfa\x9b\xc9\x7a\xd3\xae\xeb\x6d\x98\x89\x31\x34\x2d\x39\x1e\x1f' \
              b'\xe1\xc4\x7c\xdd\x2d\xef\x26\x37\x7a\xfa\xbf\xd2\xd9\x60\x79\xf1\xca\x99\xd0\x32\xf7\xd8\x4d\x4e' \
              b'\xf6\xce\x45\xda\x0c\x67\x99\x09\xe6\x89\x75\x69\x5f\xd9\x12\xa2\x3e\x77\x74\x3c\xf5\xbe\x2e\x57' \
              b'\x64\x05\x1a\x71\x96\x62\x23\x25\x80\x63\xfc\xe7\xc6\xd4\xe7\xca\x76\x7d\x70\x3c\xcb\xe2\x31\xc5' \
              b'\xed\x03\x8d\xcc\xad\x1a\x75\x53\x4a\x61\x27\xb8\x30\xca\xeb\x73\xb4\xc6\xd6\xdb\xda\x00\x88\xe2' \
              b'\x11\x21\xef\xd5\xf3\x8a\x02\x1f\x06'

        encoded_map: mmap = fmap.get(
            descriptor=self.encoded_file
        )

        pescent = 0
        with open(self.decoded_file_path, 'wb') as decoded_file:
            while True:

                current_pescent = int(os.path.getsize(decoded_file.name) / (encoded_map.size() / 100))
                if current_pescent > pescent:
                    pescent = current_pescent
                    signal.emit(pescent)

                decoded_bytes = self.xor(encoded_map.read(len(key)), key)

                if decoded_bytes == b'':
                    encoded_map.close()
                    os.close(self.encoded_file)
                    break

                decoded_file.write(decoded_bytes)

        return True

    # EXTRACTOR
    @staticmethod
    @log.wrapper('DEBUG')
    def get_params(container_header: bytes) -> tuple[int, int, int]:  # checked
        """ reading first 10 bytes"""
        if container_header[4:5] == b'\x02' and container_header[10:] == b'\x00':

            container_length = int.from_bytes(
                bytes=container_header[:4],
                byteorder='little',
                signed=False
            )

            path_length = int.from_bytes(
                bytes=container_header[5:6],
                byteorder='little',
                signed=False
            )

            data_length = int.from_bytes(
                bytes=container_header[6:10],
                byteorder='little',
                signed=False
            )

            return container_length, path_length, data_length

        else:
            return 0, 0, 0

    def extract(self, signal) -> bool:

        self.decoded_file: int = file.get(
            path=self.decoded_file_path
        )

        if self.decoded_file is None:
            raise FileNotFoundError

        folder_path = os.path.join(os.getcwd(), "client", "files", "data", "")
        if not folder.exists(folder_path):
            folder.create(folder_path)

        decoded_map: mmap = fmap.get(
            descriptor=self.decoded_file
        )

        while True:
            cursor = decoded_map.find(b'\x02', decoded_map.tell())

            if cursor == -1:
                signal.emit(100)
                break
            signal.emit(int(decoded_map.tell() / (decoded_map.size() / 100)))

            decoded_map.seek(cursor - 4)
            container_length, path_length, data_length = self.get_params(decoded_map.read(11))

            if container_length == path_length + data_length + 19:
                decoded_map.seek(decoded_map.tell() + 4)

                file.write(
                    path=os.path.join(
                        folder_path,
                        decoded_map.read(path_length).decode("utf-8", "ignore").replace("/", "\\")
                    ),
                    container=decoded_map.read(data_length)
                )
                continue

            else:
                decoded_map.seek(cursor + 1)
                continue

        os.close(self.decoded_file)
        return True


data = Data()
