from __future__ import absolute_import, print_function, unicode_literals

import unittest
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

__path__ = os.path.abspath(__file__)

from testing_utils import split_env_to_frozenset, is_pull_request, is_ci

TESTING_VERS = split_env_to_frozenset("GAME_TEST_VERS")
TESTING_FOLDERS = split_env_to_frozenset("TEST_FOLDERS")
IS_PR = is_pull_request()
IN_TRAVIS = is_ci()

# Will probably want to add to the Travis CI matrix so that these tests run separately from the whole thing's tests.

class TestAwsToolsCommon(unittest.TestCase):

    def test_common_contains_wanted_folders(self):
        from aws_tools.common import folders
        for folder in TESTING_FOLDERS:
            self.assertTrue(folder in folders,
                "Folder {} not found in `aws_tools.common.folders`".format(folder))

    def test_common_contains_wanted_versions(self):
        from aws_tools.common import versions
        for ver in TESTING_VERS:
            self.assertTrue(ver in versions,
                "Version {} not found in `aws_tools.common.versions`".format(ver))

class TestAwsToolsUpload(unittest.TestCase):

    AWS_UPLOAD_SCRIPT = os.path.normpath(os.path.join(__path__, "../aws_tools/upload.py"))

    def test_upload_script_exists(self):
        self.assertTrue(os.path.exists(AWS_UPLOAD_SCRIPT),
            "Upload script `{}` not found, are tests in the right folder?".format(AWS_UPLOAD_SCRIPT))

    @unittest.skipIf(not IS_PR and IN_TRAVIS, "pull request doesn't have access to secret environment variables")
    def test_dummy_file_upload(self):
        import subprocess
        # Create a dummy test file
        # Upload it to the S3 dumping bucket.
        # Read it from the S3 dumping bucket.
        # Make sure it's the right file (we'll writ the timestamp to it)
        # Delete it from the dumping bucket then at the end in tearDown()

    @unittest.skipIf(not IS_PR and IN_TRAVIS, "pull request doesn't have access to secret environment variables")
    def test_cached_files_upload(self):
        import subprocess
        # Upload cached `game_data/` fiels to a directory made for this test in the dumping bucket in a directory.
        # Check to see they're in the S3 bucket.
        # If they aren't, something is wrong.
        # Then delete it from the dumpingbucket at the end in tearDown()



class TestAwsToolsDownload(unittest.TestCase):

    AWS_DOWNLOAD_SCRIPT = os.path.normpath(os.path.join(__path__, "../aws_tools/download.py"))

    @unittest.skipIf(not IS_PR and IN_TRAVIS, "pull request doesn't have access to secret environment variables")
    def test_download_game_data_if_aws(self):




if __name__ == '__main__':
    unittest.main()
