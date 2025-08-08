import configparser
import os
from platformdirs import user_data_dir, user_config_dir
from pathlib import Path

APP_NAME = "tnote"
AUTHOR = "tnote"

_data_dir = Path(user_data_dir(APP_NAME, AUTHOR)) / "data"
_data_dir.mkdir(parents=True, exist_ok=True)

_config_dir = Path(user_config_dir(APP_NAME, AUTHOR)) / "config"
_config_dir.mkdir(parents=True, exist_ok=True)
_config_file_path = _config_dir / "settings.ini"


def init_config() -> None:
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "data_path", str(_data_dir))

    with open(_config_file_path, "w") as config_file:
        config.write(config_file)


def _get_config():
    if not os.path.exists(_config_file_path):
        init_config()

    config = configparser.ConfigParser()
    config.read(_config_file_path)
    return config


def get_setting(section: str, setting: str) -> str:
    config = _get_config()
    value = config.get(section, setting)
    return value
