import configparser
import os
from platformdirs import user_data_dir, user_config_dir
from pathlib import Path

APP_NAME = "tnote"
AUTHOR = "tnote"

data_dir = Path(user_data_dir(APP_NAME, AUTHOR)) / "data"
data_dir.mkdir(parents=True, exist_ok=True)

config_dir = Path(user_config_dir(APP_NAME, AUTHOR)) / "config"
config_dir.mkdir(parents=True, exist_ok=True)
config_file_path = config_dir / "settings.ini"


def init_config():
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "data_path", str(data_dir))

    with open(config_file_path, "w") as config_file:
        config.write(config_file)


def get_config():
    """
    Returns the config object
    """
    if not os.path.exists(config_file_path):
        init_config()

    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config


def get_setting(section, setting):
    """
    Print out a setting
    """
    config = get_config()
    value = config.get(section, setting)
    return value
