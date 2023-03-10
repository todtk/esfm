# -*- coding: utf-8 -*-

import os
from .files import FileManager


class TempManager():

    def __init__(self) -> None:

        self.temp_path = os.path.join(
            os.getcwd(),
            "client",
            "files",
            "temp",
            "inet",
            ""
        )

    def search_data(self, memory) -> str | bytes:

        memory.seek(0)
        header_length = self.get_length(memory.read(4))

        memory.seek(20)
        container_data = []
        while memory.tell() < header_length - 4:
            length = self.get_length(memory.read(4))
            if length != 0 and memory.size() != header_length + length:
                container_data.append(memory.read(length).decode("utf-8", "ignore"))
            elif memory.size() == header_length + length:
                container_length = length

        name = container_data[-1]
        name = name.split("Live/")[-1]

        memory.seek(header_length)
        content = memory.read(container_length)

        return name, content
    
    def get_length(self, four_bytes: bytearray) -> int:

        return int.from_bytes(four_bytes, byteorder='little', signed=False)  

    def get_content_list(self, path: str) -> list:

        content_list = os.listdir(path)

        return content_list
    
    def extract(self, client_path: str):

        temp_path = os.path.join(client_path, "files", "temp", "inet", "")

        for folder_name in self.get_content_list(temp_path):
            for file_name in self.get_content_list(os.path.join(temp_path, folder_name, "")):

                temp_file = FileManager.open_file(
                    file_path=os.path.join(temp_path, folder_name, file_name),
                    write=False
                    )
                
                memory = FileManager.open_memory(
                    file=temp_file,
                    length=os.path.getsize(os.path.join(temp_path, folder_name, file_name))
                    )

                name, content = self.search_data(memory=memory)

                FileManager.write_file(
                    file_path=os.path.join(client_path, "files", "temp", name.replace("/", "\\")),
                    file_content=content
                    )