import os
from zipfile import ZipFile
import json
import datetime
import shutil

source = input('Введите то, что вы хотите поместить в архив: ')
dest = input('Куда вы хотите поместить архив: ')
data = []

name_file = str(datetime.datetime.now()).replace(':', '.') + '.zip'


if source == '':
    source = os.curdir
if dest == '':
    dest = os.curdir


def make_reserve_arc(source, dest):
    for dir, i, files in os.walk(source):
        for name in files:
            if dir != '.' and name != name_file:
                data.append(f'{os.path.join(dir, name)}')
            else:
                data.append(name)

    with ZipFile(name_file, 'a') as myzip:
        for name in data:
            myzip.write(name)

make_reserve_arc(source, dest)