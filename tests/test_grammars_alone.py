import os

import pytest

def test_subdirs_exist(game_files_path):
    dirs = os.listdir(game_files_path)
    assert "common" in dirs
    assert "events" in dirs
    assert "localisation" in dirs
    assert "localisation_synced" in dirs
    assert "map" in dirs
    assert "prescripted_countries" in dirs