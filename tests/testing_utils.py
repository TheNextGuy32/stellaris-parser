import os

def split_env_to_frozenset(var):
    var_val = os.getenv(var)
    var_list = var_val.split(",")
    var_set = frozenset(var_list)
    return var_set

def is_pull_request():
    return bool(os.getenv("TRAVIS_PULL_REQUEST", default=False))

def is_ci():
    return bool(os.getenv("CONTINUOUS_INTEGRATION", default=False))