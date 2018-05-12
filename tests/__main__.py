from __future__ import absolute_import, print_function

import unittest
import logging

logging.basicConfig(level=logging.INFO)

from .test_grammars import(


    )

from .test_aws_tools import(

    )

if __name__ == '__main__':
    test_arg = str(sys.argv[2])
    if test_arg == "aws":
        unittest.main()
    elif test_arg == "grammars":
        unittest.main()
    unittest.main()