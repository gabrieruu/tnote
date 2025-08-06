from tnote.commands.base import BaseCommand

import os
import json
import sys
from pyfzf import FzfPrompt


class RemoveCommand(BaseCommand):
    def __init__(self):
        self._subcommand_registry = {
            "tool": self._remove_tool,
            "reference": self._remove_reference,
        }

        self.pyfzf = FzfPrompt()

    def _get_selected_tool_path(self):
        selected_tool = self.pyfzf.prompt(self._tool_list)
        if not selected_tool:
            sys.exit()

        tool_file = self._get_tool_file_path(selected_tool[0])
        return tool_file

    def _remove_tool(self, args):
        tool_file = self._get_selected_tool_path()

        while True:
            if os.path.exists(tool_file):
                answer = (
                    input(
                        f'You are about to delete tool file "{tool_file}".\nDo you want to continue? [Y/n] '
                    )
                    .strip()
                    .lower()
                )
                if answer in ("", "y", "yes"):
                    os.remove(tool_file)
                    print("Tool file deleted.")
                    break
                elif answer in ("n", "no"):
                    print("Operation cancelled.")
                    break
                else:
                    print("Please answer with 'yes', 'no', 'y', or 'n'.")

    def _remove_reference(self, args):
        tool_file = self._get_selected_tool_path()

        with open(tool_file, "r") as file_handler:
            data = json.load(file_handler)
            file_handler.close()

        reference_list = [key for key in data]
        selected_reference = self.pyfzf.prompt(reference_list)
        if not selected_reference:
            sys.exit()

        while True:
            answer = (
                input(
                    f"You are about to delete reference title '{selected_reference}' in tool file '{tool_file}'.\nDo you want to continue? [Y/n] "
                )
                .strip()
                .lower()
            )
            if answer in ("", "y", "yes"):
                del data[selected_reference[0]]

                with open(tool_file, "w") as file_handler:
                    json.dump(data, file_handler, indent=4)
                    file_handler.close()

                print("Reference deleted.")
                break
            elif answer in ("n", "no"):
                print("Operation cancelled.")
                break
            else:
                print("Please answer with 'yes', 'no', 'y', or 'n'.")

    def run(self, args):
        self._tool_list = os.listdir(self._data_path)
        self._tool_list = [tool.replace(".json", "") for tool in self._tool_list]
        self._subcommand_registry[args.subcommand](args)
