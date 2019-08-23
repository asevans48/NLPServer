"""
Test configuration loading

@author aevans
"""

import os

from nlp_server.config import load_config


def test_load_config():
    """
    Test loading a configuration
    """
    current_dir = os.path.curdir
    test_path = os.path.sep.join([current_dir, 'data', 'test_config.json'])
    cfg = load_config.load_config(test_path)
    assert cfg is not None
    assert cfg.use_gpu is False
