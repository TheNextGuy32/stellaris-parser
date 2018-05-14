from __future__ import absolute_import, print_function, unicode_literals

import unittest
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

__path__ = os.path.abspath(__file__)

from testing_utils import split_env_to_frozenset, is_pull_request

TESTING_VERS = split_env_to_frozenset("GAME_TEST_VERS")
TESTING_FOLDERS = split_env_to_frozenset("TEST_FOLDERS")
IS_PR = is_pull_request()

# Will probably want to add to the Travis CI matrix so that these tests run separately from the whole thing's tests.

class TestAwsToolsCommon(unittest.TestCase):

    def test_common_contains_wanted_folders(self):
        from aws_tools.common import folders
        for folder in TESTING_FOLDERS:
            self.assertTrue(folder in folders, "Folder {} not found in `aws_tools.common.folders`".format(folder))

    def test_common_contains_wanted_versions(self):
        from aws_tools.common import versions
        for ver in TESTING_VERS:
            self.assertTrue(ver in versions, "Version {} not found in `aws_tools.common.versions`".format(ver))

class TestAwsToolsUpload(unittest.TestCase):

    def test_folder_uploads_with_none(self):



class TestAwsToolsDownload(unittest.TestCase):



if __name__ == '__main__':
    unittest.main()
