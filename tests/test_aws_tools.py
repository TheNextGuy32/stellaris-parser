from __future__ import absolute_import, print_function, unicode_literals

import unittest
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

__path__ = os.path.abspath(__file__)

# Will probably want to add to the Travis CI matrix so that these tests run separately from the whole thing's tests.

class TestAwsUploadTool(unittest.TestCase):

    def test_common_contains_wanted_folders(self):
        from aws_tools.common import folders
        self.assertTrue()

    def test_events_valid_earley_grammar(self):
        grammar = os.join(__path__, GRAMMAR_PATH)
        try:
            with open(grammar, 'r') as f:
                Lark(f.read(), parser='earley')
        except:
            self.fail("Events grammar is not a valid Earley grammar")