from pathlib import Path
import os
import json

from tnote.registry import CommandRegistry
from tnote.config import get_setting


class AddCommand(CommandRegistry):
    def __init__(self):
        self.subcommand_registry = {
            "reference": self.add_reference,
            "tool": self.add_tool,
        }

    def add_reference(self, args):
        tool_file_path = Path(get_setting("Settings", "data_path")) / args.tool

        if not os.path.exists(tool_file_path):
            print(
                f'error: tool {args.tool} doesn\'t exist, run "tnote tool add -n <toolname>" first to create the tool file'
            )
            return

        with open(tool_file_path, "r") as file_handler:
            data = json.load(file_handler)
            file_handler.close()

        data[args.name] = args.content

        with open(tool_file_path, "w") as file_handler:
            json.dump(data, file_handler, indent=4)
            file_handler.close()

    def add_tool(self, args):
        tool_file_path = Path(get_setting("Settings", "data_path")) / f'{args.name}.json'

        if os.path.exists(tool_file_path):
            print(f"error: tool {args.name} already exists")
            return

        with open(tool_file_path, "w") as file_handler:
            file_handler.write(json.dumps({}))
            file_handler.close()

    def run(self, args):
        self.subcommand_registry[args.subcommand](args)
