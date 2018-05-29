from __future__ import absolute_import, print_function, unicode_literals

import unittest
import logging
import os
import sys

from lark import Lark

logging.basicConfig(level=logging.INFO)

__path__ = os.path.abspath(__file__)

from testing_utils import split_env_to_frozenset, is_pull_request, is_ci

TESTING_VERS = split_env_to_frozenset("GAME_TEST_VERS")
TESTING_FOLDERS = split_env_to_frozenset("TEST_FOLDERS")
IS_PR = is_pull_request()
IN_TRAVIS = is_ci()

def file_to_text(path):
    with open(path, 'r') as f:
        return f.read() + '\n'

def get_all_dir_versions(folder):
    return [ os.path.join(d, folder) for d in version_dirs ]

class TestValidGrammars(unittest.TestCase):

    # Might try to make this in some sort of generic
    GRAMMAR_PATH = '../stellaris_parser/grammars/lark/'

    def test_events_valid_lalr_grammar(self):
        grammar = os.path.join(__path__, GRAMMAR_PATH)
        try:
            with open(grammar, 'r') as f:
                Lark(f.read(), parser='lalr')
        except:
            self.fail("Events grammar is not a valid Lalr(1) grammar")

    def test_events_valid_earley_grammar(self):
        grammar = os.join(__path__, GRAMMAR_PATH)
        try:
            with open(grammar, 'r') as f:
                Lark(f.read(), parser='earley')
        except:
            self.fail("Events grammar is not a valid Earley grammar")


class TestEventsLarkGrammars(unittest.TestCase):

    LARK_GRAMMAR_PATH = '../stellaris_parser/grammars/lark/events.lark'
    GAME_FILE_DIR_FROM_HERE = '../game-files/'

    def setUp(self):
        self.grammar_files_path = os.path.join(__path__, LARK_GRAMMAR_PATH)
        self.game_files_path = os.path.join(__path__, GAME_FILE_DIR_FROM_HERE)
        self.game_version_dirs = [ os.path.join(self.game_files_path, subdir) for subdir in TESTING_VERS ]

        # If we have access to secret ENVs, feel free to download the game files from S3.
        if not IS_PR and IN_TRAVIS:
            from aws_tools import download
            download.main("../game_files/", "stellaris-parser-travis-ci-alfa")

    def test_lalr_parses_all_events(self):

        # Read in grammar text, but make default
        grammar_text = ""
        with open(self.grammar_files_path, 'r') as f:
            grammar_text = f.read()
        # Must add \n at end in order to make sure it parses correctly
        grammar_text += "\n"

        # Create parser using grammar text
        event_parser = Lark(grammar_text, parser='lalr')

        # Go through all the game versions.
        for ver_dir in self.game_version_dirs:

            events_dir = os.path.join(ver_dir, "events/")
            test_files = [ os.join(events_dir, event) for event in os.listdir(events_dir) ]

            for file_name in test_files:
                try:
                    data_text = ""
                    with open(file_name, 'r') as f:
                        data_text = f.read()
                    data_text += "\n"
                    event_parser.parse(data_text)
                except:
                    self.fail("Events grammar did not work on {}".format(file_name))

    def test_earley_parses_all_events(self):

        # Read in grammar text, but make default
        grammar_text = ""
        with open(self.grammar_files_path, 'r') as f:
            grammar_text = f.read()
        # Must add \n at end in order to make sure it parses correctly
        grammar_text += "\n"

        # Create parser using grammar text
        event_parser = Lark(grammar_text, parser='earley')

        # Go through all the game versions.
        for ver_dir in self.game_version_dirs:

            events_dir = os.path.join(ver_dir, "events/")
            test_files = [ os.join(events_dir, event) for event in os.listdir(events_dir) ]

            for file_name in test_files:
                try:
                    data_text = ""
                    with open(file_name, 'r') as f:
                        data_text = f.read()
                    data_text += "\n"
                    event_parser.parse(data_text)
                except:
                    self.fail("Events grammar did not work on {}".format(file_name))


if __name__ == '__main__':
    unittest.main()