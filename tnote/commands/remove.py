from tnote.registry import CommandRegistry
from tnote.config import get_setting

import os
import json
from pyfzf import FzfPrompt
from pathlib import Path


class RemoveCommand(CommandRegistry):
    def __init__(self):
        self.subcommand_registry = {
            "tool": self.remove_tool,
            "reference": self.remove_reference,
        }

    def remove_tool(self, args):
        pyfzf = FzfPrompt()
        data_path = get_setting("Settings", "data_path")

        tool_list = os.listdir(data_path)
        tool_list = [tool.replace(".json", "") for tool in tool_list]

        selected_tool = pyfzf.prompt(tool_list)
        tool_file_path = Path(data_path) / f'{selected_tool[0]}.json'

        if os.path.exists(tool_file_path):
            answer = input(
                f'You are going to delete tool file "{tool_file_path}", are you sure?(yes)(no): '
            )
            if answer == "yes":
                os.remove(tool_file_path)

    def remove_reference(self, args):
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

        answer = input(
            f"You are going to delete reference title {selected_reference} in tool {selected_tool[0]}, are you sure?(yes)(no): "
        )
        if answer == "yes":
            del data[selected_reference[0]]

            with open(tool_file_path, "w") as file_handler:
                json.dump(data, file_handler, indent=4)
                file_handler.close()

    def run(self, args):
        self.subcommand_registry[args.subcommand](args)


# "remove": {
#     "tool": [("-n", "--name")],
#     "reference": [
#         ("-t", "--tool"),
#         ("-n", "--name"),
#     ],
# },
