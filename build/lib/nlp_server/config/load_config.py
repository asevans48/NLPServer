"""
Load a configuration.

@author aevans
"""

from python_json_config import ConfigBuilder


BUILDER = ConfigBuilder()


def load_config(config_path):
    """
    Load the configuration

    :param config_path: The path to the configuration
    :return:    The configbullder object
    """
    return BUILDER.parse_config(config_path)


def get_set_in_memcached():
    pass
