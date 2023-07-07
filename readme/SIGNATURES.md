
# FILES FROM DATA.PCK

| ____DATA____ | __SIZE__ | ___DESCRIPTION___ | ___TYPE___ | ________________________VALUE________________________ |
|--------------|----------|-------------------|------------|-------------------------------------------------------|
| 0E-0C-00-00  | 4 bytes  | _Contain Length_  | int        | 3086                                                  |                            
| 02           | 1 byte   | _PARAMS ↓↓↓_      | int        | 2                                                     |                             
| 20           | 1 byte   | _Path Length_     | int        | 32                                                    |                              
| DB-0B-00-00  | 4 bytes  | _Data Length_     | int        | 3035                                                  |                            
| 00           | 1 bytes  | _FILE ↓↓↓_        | int        | 0                                                     |
| 00-00-00-00  | 4 bytes  | ...               | bytes      | 0                                                     |
| 74-6...9-FF  | * bytes  | _Path_            | str        | musicplayer/music_s_sub_mt_1.png                      |
| A6-3...1-00  | * bytes  | _Data_            | bytearray  | [ file content ]                                      |
| 21-08-00-00  | 4 bytes  | ...               | ...        | ...                                                   |

# FILES FROM TEMP FOLDER

| ____DATA____ | __SIZE__ | ___DESCRIPTION___ | ___TYPE___ | ________________________VALUE________________________ |
|--------------|----------|-------------------|------------|-------------------------------------------------------|
| CC-00-00-00  | 4 bytes  | _Header Length_   | int        | 204                                                   |
| 8F-6...0-63  | 8 bytes  | ...               | ...        | ...                                                   |
| 00-00-00-00  | 4 bytes  | ...               | bytes      | 0                                                     |
| 79-19-00-00  | 4 bytes  | _PARAMS ↓↓↓_      | bytes      | 6521                                                  |
| 00-0...0-00  | 8 bytes  | ...               | bytes      | 0                                                     |
| 50-CC-06-00  | 4 bytes  | _Data Len_        | int        | 445520                                                |
| 00-00-00-00  | 4 bytes  | ...               | bytes      | 0                                                     |
| 50-CC-06-00  | 4 bytes  | _Data Len_        | int        | 445520                                                |
| 00-00-00-00  | 4 bytes  | ...               | bytes      | 0                                                     |
| 34-00-00-00  | 4 bytes  | _Config Length_   | int        | 52                                                    |
| 22-3...7-22  | * bytes  | _Config_          | ...        | "1cfb64bbc03f47b0c075d4a6ab96cb8e:1671070489.277383"  |
| 11-00-00-00  | 4 bytes  | _Key Length_      | int        | 17                                                    |
| 30-6...1-30  | * bytes  | _Key_             | ...        | 0c99547e22073b490                                     |
| 62-00-00-00  | 4 bytes  | _Path Length_     | int        | 75                                                    |
| 68-7...E-67  | * bytes  | _Path_            | int        | https:// ... /substoryweek02_EN.jpg                   |
| 79-19-00-00  | 4 bytes  | _FILE ↓↓↓_        | bytes      | 6521                                                  |
| FF-D...F-D9  | * bytes  | _Data_            | bytearray  | [ file content ]                                      |
