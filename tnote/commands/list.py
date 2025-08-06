from tnote.commands.base import BaseCommand

import os
import json
from pyfzf import FzfPrompt


class ListCommand(BaseCommand):
    def __init__(self) -> None:
        pass

    def run(self, args):
        pyfzf = FzfPrompt()

        tool_list = os.listdir(self._data_path)
        tool_list = [tool.replace(".json", "") for tool in tool_list]

        selected_tool = pyfzf.prompt(tool_list)
        tool_file = self._get_tool_file_path(selected_tool[0])

        with open(tool_file, "r") as file_handler:
            data = json.load(file_handler)
            file_handler.close()

        reference_list = [key for key in data]
        selected_reference = pyfzf.prompt(reference_list)

        print(data[selected_reference[0]])
