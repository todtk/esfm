# -*- coding: utf-8 -*-

import os
from file_manage import File_Manager


class Extractor():

    def __init__(self) -> None:
        ...

    @classmethod
    def search_data(self, memory, size: int) -> str | bytes:

        cursor = memory.find(b'\x68\x74\x74\x70\x73\x3A\x2F\x2F', 0)
        memory.seek(cursor - 4)

        name_lenght = int.from_bytes(memory.read(4), byteorder='little', signed=False)
        name = memory.read(name_lenght).decode("utf-8", "ignore")

        memory.read(4)
        cursor = memory.tell()
        content = memory.read(size-cursor)

        return name, content
    
    @classmethod
    def get_content_list(self, path: str) -> list:

        content_list = os.listdir(path)

        return content_list
    
    @classmethod
    def extract(self, client_path: str):

        temp_path = os.path.join(client_path, "files", "temp", "inet", "")

        for folder_name in self.get_content_list(temp_path):
            for file_name in self.get_content_list(os.path.join(temp_path, folder_name, "")):

                file = File_Manager.open_file(
                    file_path=os.path.join(temp_path, folder_name, file_name),
                    write=False
                    )
                
                memory = File_Manager.open_memory(
                    file=file,
                    length=os.path.getsize(os.path.join(temp_path, folder_name, file_name))
                    )

                name, content = self.search_data(
                    memory=memory,
                    size=os.path.getsize(os.path.join(temp_path, folder_name, file_name))
                    )

                File_Manager.write_file(
                    file_path=os.path.join(client_path, "files", "temp", name.replace("/", "\\")[8:]),
                    file_content=content
                    )