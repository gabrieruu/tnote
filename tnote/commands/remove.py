from tnote.commands.base import BaseCommand

import os
import json
import sys
from pyfzf import FzfPrompt


class RemoveCommand(BaseCommand):
    """Handles the 'remove' command for tnote.

    Supports deleting either an entire tool file or a specific reference within it.
    Uses an interactive fuzzy finder (fzf) to select targets.
    """

    _pyfzf = FzfPrompt()

    def __init__(self):
        self._subcommand_registry = {
            "tool": self._remove_tool,
            "reference": self._remove_reference,
        }

    def _confirm(self, message):
        while True:
            answer = input(f"{message} [Y/n]").strip().lower()
            if answer in ("", "y", "yes"):
                return True
            elif answer in ("n", "no"):
                return False
            else:
                print("Please answer with 'yes', 'no', 'y', or 'n'.")

    def _remove_tool(self):
        message = f"You are about to delete tool file '{self._tool_file}'.\nDo you want to continue?"

        if self._confirm(message):
            os.remove(self._tool_file)
            print("Tool file deleted.")
        else:
            print("Operation cacelled.")

    def _remove_reference(self):
        reference_list = list(self._data.keys())

        selected_reference = self._pyfzf.prompt(reference_list)
        if not selected_reference:
            sys.exit()

        message = f"You are about to delete reference {selected_reference} in tool '{self._selected_tool[0]}'."

        if self._confirm(message):
            del self._data[selected_reference[0]]
            with open(self._tool_file, "w") as file_handler:
                json.dump(self._data, file_handler, indent=4)

            print("Reference deleted.")
        else:
            print("Operation cancelled.")

    def run(self, args):
        tool_list = [tool.replace(".json", "") for tool in os.listdir(self._data_path)]

        self._selected_tool = self._pyfzf.prompt(tool_list)
        if not self._selected_tool:
            sys.exit()

        self._tool_file = self._get_tool_file_path(self._selected_tool[0])

        with open(self._tool_file, "r") as file_handler:
            self._data = json.load(file_handler)

        self._subcommand_registry[args.subcommand]()
