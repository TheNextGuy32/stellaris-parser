from __future__ import absolute_import, print_function, unicode_literals

import os

from lark import Lark

event_parser = Lark(open('./stellaris_parser/grammars/lark/events.lark'), parser='lalr')

FILE_DIR = './game_files/'
VER_DIR = '2.1.0/'
EVENTS_DIR = 'events/'

test_dir = os.path.join(FILE_DIR, VER_DIR, EVENTS_DIR)

file_names = os.listdir(test_dir)

file_path = [ os.path.join(test_dir, file) for file in file_names ]

for file_name in file_path:
    text = ""
    with open(file_name) as file:
        text = file.read()
    text += "\n"
    try:
        parsed = event_parser.parse(text)
        print("{} worked fine".format(file_name))
    except:
        print("{} threw exception".format(file_name))