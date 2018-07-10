import os

import pytest

@pytest.fixture(params=['1.8.3', '1.9.1', '2.0.1', '2.0.5', '2.1.0'], scope="session")
def game_files_versions(request):
    return os.path.abspath(os.path.join('../game_files', request.param))

@pytest.fixture(params=['common', 'events', 'localisation', 'localisation_synced', 'map', 'prescripted_countries'], scope="session")
def game_files_common_parents(request, game_files_versions):
    return os.path.join(game_files_versions, request.param)

def test_dummy(game_files_common_parents):
    print(game_files_common_parents)
