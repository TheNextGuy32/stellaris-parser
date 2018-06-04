from __future__ import absolute_import, print_function, unicode_literals

import os

from lark import Lark

event_parser = Lark(open('./stellaris_parser/grammars/lark/events.lark'), parser='lalr')

FILE_DIR = './game_files/'
VER_DIR = '2.1.0/'
EVENTS_DIR = 'events/'

test_dir = os.path.join(FILE_DIR, VER_DIR, EVENTS_DIR)

file_path = os.path.join(test_dir, sys.argv[1])

text = ""
with open(file_path) as file:
    text = file.read()
text += "\n"

parsed = event_parser.parse(text)
print("{} worked fine".format(file_name))