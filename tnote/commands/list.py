from argparse import Namespace
from tnote.commands.base import BaseCommand

import os
import json
import sys
from pyfzf import FzfPrompt


class ListCommand(BaseCommand):
    """Lists available tools and references.

    Uses fuzzy finder (`pyfzf`) to prompt the user to select a tool and then
    a reference within that tool, printing the selected reference content.
    """

    def run(self, args: Namespace) -> None:
        pyfzf = FzfPrompt()

        tool_list = [tool.replace(".json", "") for tool in os.listdir(self._data_path)]

        selected_tool = pyfzf.prompt(tool_list)
        if not selected_tool:
            sys.exit()

        tool_file = self._get_tool_file_path(selected_tool[0])

        with open(tool_file, "r") as file_handler:
            data = json.load(file_handler)

        reference_list = list(data.keys())

        selected_reference = pyfzf.prompt(reference_list)
        if not selected_reference:
            sys.exit()

        print(data[selected_reference[0]])
