# -*- coding: utf-8 -*-

"""

THIS SCRIPT LOOKS FOR CRITICAL CHANKS IN THE DATA ARRAY AND EXTRACTS FILES.

FILE SIGNATURE EXAMPLE
            ^^                ^^
64-DB-07-00 02 1F 32-DB-07-00 00 00-00-00-00 74-69-74-6C-65-2F-62-67-2F-31-73-74-5F-61-6E-6E-69-76-65-72-73-61-72-79-5F-62-67-2E-70-6E-67-89
⎡           ⎡   ⎡  ⎡           ⎡   ⎡           ⎡
⎢           ⎢   ⎢  ⎢           ⎢   ⎢           ⎣ FILE NAME musicplayer/music_s_sub_mt_1.png
⎢           ⎢   ⎢  ⎢           ⎢   ⎢
⎢           ⎢   ⎢  ⎢           ⎢   ⎣ 4 BYTES - UNKNOWN
⎢           ⎢   ⎢  ⎢           ⎢
⎢           ⎢   ⎢  ⎢           ⎣ 1 BYTE - CRITICAL CHUNK [00]
⎢           ⎢   ⎢  ⎢
⎢           ⎢   ⎢  ⎣ 4 BYTES - CONTENT LENGTH 3035
⎢           ⎢   ⎢
⎢           ⎢   ⎣ 1 BYTE - NAME LENGTH 32
⎢           ⎢
⎢           ⎣ 1 BYTE - CRITICAL CHUNK [02]
⎢
⎣ 4 BYTES FILE BLOCK SIZE 3086

:copyright: (c) 2022-present todtk
:license: no license

"""