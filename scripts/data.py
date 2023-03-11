# -*- coding: utf-8 -*-

import os
from io import BytesIO
from itertools import cycle
from .files import open_file, open_memory, write_file


class DataManager():

    def __init__(self) -> None:
        
        self.pack_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "data.pack"
        )
        self.pck_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "data.pck"
        )
        self.data_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "data",
            ""
        )

    ####################################################################################################
    ### DECODER                                                                                      ###
    ####################################################################################################
    def check_data1(self) -> bool:
        return os.path.exists(self.pack_path)

    def get_xor(self, data: bytearray, key: bytearray) -> bytes:
        return bytes(a ^ b for a, b in zip(data, cycle(key)))
    
    def get_decode(self, signal) -> None:
        try:

            key = b'\x21\x0c\xed\x10\xd8\x81\xd7\xa3\xfa\x9b\xc9\x7a\xd3\xae\xeb\x6d\x98\x89\x31\x34\x2d\x39\x1e\x1f\xe1\xc4\x7c\xdd\x2d\xef\x26\x37\x7a\xfa\xbf\xd2\xd9\x60\x79\xf1\xca\x99\xd0\x32\xf7\xd8\x4d\x4e\xf6\xce\x45\xda\x0c\x67\x99\x09\xe6\x89\x75\x69\x5f\xd9\x12\xa2\x3e\x77\x74\x3c\xf5\xbe\x2e\x57\x64\x05\x1a\x71\x96\x62\x23\x25\x80\x63\xfc\xe7\xc6\xd4\xe7\xca\x76\x7d\x70\x3c\xcb\xe2\x31\xc5\xed\x03\x8d\xcc\xad\x1a\x75\x53\x4a\x61\x27\xb8\x30\xca\xeb\x73\xb4\xc6\xd6\xdb\xda\x00\x88\xe2\x11\x21\xef\xd5\xf3\x8a\x02\x1f\x06'
            stream = BytesIO(open(self.pack_path, "rb").read())
            
            size = os.path.getsize(os.path.join(self.pack_path))
            cur_persent = 0

            with open(self.pck_path, "wb") as pck:

                while True:

                    persent = int(os.path.getsize(os.path.join(self.pck_path)) / (size / 100))
                    if cur_persent != persent:
                        signal.emit(persent)
                        cur_persent = persent

                    decrypted_bytes = self.get_xor(stream.read(len(key)), key)
                    pck.write(decrypted_bytes)

                    if decrypted_bytes == b'':
                        break

        except:
            ...

    ####################################################################################################
    ### EXTRACTOR                                                                                    ###
    ####################################################################################################
    def check_data2(self) -> bool:
        return os.path.exists(self.pck_path)

    def read_header(self, header: bytes) -> int:

        if header[4:5] == b'\x02' and header[10:] == b'\x00':

            length_block = int.from_bytes(
                header[:4],
                byteorder='little',
                signed=False
            )

            length_path = int.from_bytes(
                header[5:6],
                byteorder='little',
                signed=False
            )

            length_container = int.from_bytes(
                header[6:10],
                byteorder='little',
                signed=False
            )

            return length_block, length_path, length_container
        
        else:
            return 0, 0, 0

    def get_extract(self, signal) -> None:

        pck_file = open_file(
            file_path = self.pck_path,
            write=False
        )

        size = os.path.getsize(os.path.join(self.pck_path))

        mfile = open_memory(
            file = pck_file,
            length = size
        )

        # counters
        success = 0
        errors = 0

        # cursors
        cur = 0
        flag = 0

        while True:

            if cur >= flag:
                flag = cur

                status_dict = {
                    "persent": int(cur / (size / 100)),
                    "success:errors": [success, errors]
                }
                signal.emit(status_dict)

                try:

                    cur = mfile.find(b'\x02', cur)
                    mfile.seek(cur - 4)

                    length_block, length_path, length_container = self.read_header(mfile.read(11))

                    if length_path or length_container != 0:

                        if length_block == length_path + length_container + 19:

                            cur = mfile.tell()
                            mfile.seek(cur + 4)

                            path = mfile.read(length_path).decode("utf-8", "ignore").replace("/", "\\")
                            full_path = os.path.join(self.data_path, path)

                            container = mfile.read(length_container)

                            status = write_file(path=full_path, container=container)
                            if status:
                                success += 1
                                print("EXTRACTED: ", full_path)

                            cur += 4 + length_path + length_container + 4
                            continue

                except:
                    errors += 1

                cur += 1
                continue

            else:
                break