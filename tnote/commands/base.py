from tnote.config import get_setting
from pathlib import Path


class BaseCommand:
    registry = {}

    def __init_subclass__(cls):
        name = cls.__name__.lower().replace("command", "")
        cls.registry[name] = cls()

        cls._data_path = get_setting("Settings", "data_path")

    @classmethod
    def _get_tool_file_path(cls, tool_name):
        tool_file_path = Path(cls._data_path) / f"{tool_name}.json"
        return tool_file_path
