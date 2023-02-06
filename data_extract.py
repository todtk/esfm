# -*- coding: utf-8 -*-

import os
from file_manage import File_Manager
from main import DATA_PATH


class Extractor():

    def __init__(self) -> None:
        ...

    def get_file_path(self, file_name) -> str:

        indent = 1
        file_name, file_extension = os.path.splitext(file_name)
        while True:
            if indent > 1:
                file_name = file_name + " (" + str(indent) + ")"

            file_fullname = os.path.split(os.path.abspath(DATA_PATH + file_name + file_extension))

            if os.path.isfile(file_fullname[0] + "\\" + file_fullname[1]):
                indent = indent + 1
            else:
                break

        return file_fullname

    def search_signature(self, mfile) -> int:

        extracted_files = 0
        errors = 0

        cursor = 0
        shift = 0
        while True:
            if cursor >= shift:
                shift = cursor
                try:
                    cursor = mfile.find(b'\x02', cursor)
                    mfile.seek(cursor + 1)
                    length_file_name = int.from_bytes(mfile.read(1), byteorder='little', signed=False)
                    length_file_content = int.from_bytes(mfile.read(4), byteorder='little', signed=False)
                    if mfile.read(1) == b'\x00':
                        if length_file_name and length_file_content != 0:
                            mfile.seek(cursor - 4)
                            block_size = int.from_bytes(mfile.read(4), byteorder='little', signed=False)
                            if block_size == length_file_name + length_file_content + 19:
                                mfile.read(11)
                                file_name = mfile.read(length_file_name).decode("utf-8", "ignore")
                                file_content = mfile.read(length_file_content)
                                self.extract_file(file_name, file_content)
                                print("EXTRACT: ", file_name, length_file_content, "bytes")
                                cursor += length_file_name + length_file_content + 15
                                extracted_files += 1
                                continue
                    cursor += 1
                    continue
                except:
                    errors += 1
                    cursor += 1
                    continue
            else:
                break
        
        return extracted_files, errors