"""
Test configuration loading

@author aevans
"""

import os
import unittest

from nlp_server.config import load_config


class TestConfigurationLoader(unittest.TestCase):
    """
    Tests for the configuration loader
    """

    def test_load_config(self):
        """
        Test loading a configuration
        """
        current_dir = os.path.curdir
        test_path = os.path.sep.join([current_dir, 'data', 'test_config.json'])
        cfg = load_config.load_config(test_path)
        assert cfg is not None
        assert cfg.use_gpu is False
