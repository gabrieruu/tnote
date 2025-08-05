from tnote.registry import BaseCommand

import os
import json
from pyfzf import FzfPrompt


class RemoveCommand(BaseCommand):
    def __init__(self):
        self.subcommand_registry = {
            "tool": self.remove_tool,
            "reference": self.remove_reference,
        }

        self.pyfzf = FzfPrompt()

    def get_selected_tool_path(self):
        selected_tool = self.pyfzf.prompt(self.tool_list)
        tool_file_path = self.get_tool_file_path(selected_tool[0])
        return tool_file_path

    def remove_tool(self, args):
        tool_file = self.get_selected_tool_path()

        if os.path.exists(tool_file):
            answer = input(
                f'You are going to delete tool file "{tool_file}", are you sure?(yes)(no): '
            )
            if answer == "yes":
                os.remove(tool_file)

    def remove_reference(self, args):
        tool_file = self.get_selected_tool_path()

        with open(tool_file, "r") as file_handler:
            data = json.load(file_handler)
            file_handler.close()

        reference_list = [key for key in data]
        selected_reference = self.pyfzf.prompt(reference_list)

        answer = input(
            f"You are going to delete reference title {selected_reference} in tool file {tool_file}, are you sure?(yes)(no): "
        )
        if answer == "yes":
            del data[selected_reference[0]]

            with open(tool_file, "w") as file_handler:
                json.dump(data, file_handler, indent=4)
                file_handler.close()

    def run(self, args):
        self.tool_list = os.listdir(self.data_path)
        self.tool_list = [tool.replace(".json", "") for tool in self.tool_list]
        self.subcommand_registry[args.subcommand](args)
