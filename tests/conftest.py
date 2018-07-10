import os

import pytest

from stellaris_parser.aws_tools import download

@pytest.fixture(params=['1.8.3', '1.9.1', '2.0.1', '2.0.5', '2.1.0'], scope="session")
def game_files_path(request):
    this_ver = os.path.abspath(os.path.join('game_files', request.param))
    if not os.path.exists(this_ver):
        # Just use default bucket name.
        download.main(this_ver, bucket_name=os.getenv('BUCKET_NAME'), remote=os.path.join('game_files', request.param))
    return this_ver
