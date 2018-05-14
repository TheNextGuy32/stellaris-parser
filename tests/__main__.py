from __future__ import absolute_import, print_function, unicode_literals

import unittest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def import_aws_tests():
    from .test_aws_tools import(
        TestAwsToolsCommon,
        TestAwsToolsUpload,
        TestAwsToolsDownload
    )

def import_grammars_tests():
    from .test_grammars import(
            TestValidGrammars,
            TestEventsLarkGrammars
    )

def main():
    if len(sys.argv) > 1:
        test_arg = str(sys.argv[2])
        if test_arg == "aws":
            import_aws_tests()
            unittest.main()
        elif test_arg == "grammars":
            import_grammars_tests()
            unittest.main()
        else:
            logger.error("Unknown test argument passed.")
    else:
        import_aws_tests()
        import_grammars_tests()
        unittest.main()

if __name__ == '__main__':
    main()