from __future__ import absolute_import, print_function, unicode_literals

import unittest
import logging
import os
import sys

from lark import Lark

GAME_FILE_DIR_FROM_HERE = '../game-files/'

logging.basicConfig(level=logging.INFO)

__path__ = os.path.abspath(__file__)

game_file_path = os.path.join(__path__, GAME_FILE_DIR_FROM_HERE)

def file_to_text(path):
    with open(path, 'r') as f:
        return f.read() + '\n'

version_dirs = [ os.path.join(game_file_path, subdir) for subdir in os.listdir(game_file_path) ]

def get_all_dir_versions(folder):
    return [ os.path.join(d, folder) for d in version_dirs ]

class TestEventsLarkGrammars(unittest.TestCase):

    def test_no_grammar_syntax_error(self):
        grammar = os.join(__path__, '../grammars/lark/events.lark')
        try:
            with open(grammar, 'r') as f:
                Lark(f.read(), parser='lalr')
        except:
            self.fail("Forming grammar raised exception.")

    def test_no_error_with_grammars_all_versions(self):
        ver_dirs = get_all_dir_versions('events/')

        grammar_file = os.join(__path__, '../grammars/lark/events.lark')

        grammar_text = ""
        with open(grammar_file, 'r') as f:
            grammar_text = f.read()
        grammar_text = [ text + "\n" for text in grammar_text ]

        event_parser = Lark(grammar_text, parser='lalr')

        for this_ver_dir in ver_dirs:
            test_files = [ os.join(this_ver_dir, event) for event in os.listdir(this_ver_dir) ]
            for file_name in test_files:
                try:
                    data_text = ""
                    with open(file_name, 'r') as f:
                        data_text = f.read()
                    data_text += "\n"
                    event_parser.parse()
                except:
                    self.fail("Events grammar did not work on {}".format(file_name))
