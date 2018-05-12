import os

def split_env_to_frozenset(var):
    var_val = os.getenv(var)
    var_list = var_val.split(",")
    var_set = frozenset(var_list)
    return var_set

def is_pull_request():
    return bool(os.getenv("TRAVIS_PULL_REQUEST"))