from tnote.registry import CommandRegistry
from tnote.config import get_setting

import os
import json
from pyfzf import FzfPrompt
from pathlib import Path

class ListCommand(CommandRegistry):
    def __init__(self) -> None:
        pass

    def run(self, args):
        pyfzf = FzfPrompt()
        data_path = get_setting("Settings", "data_path")

        tool_list = os.listdir(data_path)
        tool_list = [tool.replace(".json", "") for tool in tool_list]

        selected_tool = pyfzf.prompt(tool_list)
        tool_file_path = Path(data_path) / f'{selected_tool[0]}.json'

        with open(tool_file_path, "r") as file_handler:
            data = json.load(file_handler)
            file_handler.close()

        reference_list = [key for key in data]
        selected_reference = pyfzf.prompt(reference_list)

        print(data[selected_reference[0]])
