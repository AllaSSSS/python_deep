""" Код, который запускается из командной строки и получает на вход путь до директории ПК.
    Соберите информацию о содержимом в виде объектов namedtuple.
    Каждый объект хранит: имя файла без расширения или название каталога; расширение, если это файл;
    флаг каталога; название родительского каталога
    В процессе сбора сохраните данные в текстовый файл, используя логирование. """

import os
import sys
import logging
from collections import namedtuple


FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.INFO, filename='dir.log', encoding='utf-8',
                    format=FORMAT, style="{")
logger = logging.getLogger(__name__)


FileInfo = namedtuple('FileInfo', ['name', 'ext', 'flags', 'dir'])

path = sys.argv[1]
dir = os.path.basename(path)

for e in os.scandir(path):
    name, ext = e.name, ""
    if e.is_file():
        name, ext = os.path.splitext(name)
    st = e.stat()
    fi = FileInfo(name=name, ext=ext, flags=st.st_mode, dir=dir)
    logger.info(fi)
    print(fi)
