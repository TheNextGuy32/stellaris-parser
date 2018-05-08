import os

from lark import Lark

event_parser = Lark(open('./grammars/lark/events.lark'), parser='lalr')

FILE_DIR = './game-files/'
VER_DIR = '2.0.1/'
EVENTS_DIR = 'events/'

test_dir = FILE_DIR + VER_DIR + EVENTS_DIR

file_names = os.listdir(test_dir)

file_path = [ test_dir + file for file in file_names ]

for file in file_path:
    print(file)