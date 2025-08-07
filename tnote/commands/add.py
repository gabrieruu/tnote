import os
import json
import sys

from tnote.commands.base import BaseCommand


class AddCommand(BaseCommand):
    """Handles the 'add' command functionality for tnote.

    Supports adding either a new tool or a reference to an existing tool,
    based on the subcommand provided (`tool` or `reference`).

    Tool files are stored as JSON and created or updated accordingly.
    Dispatching is handled via an internal subcommand registry.
    """

    def __init__(self):
        self._subcommand_registry = {
            "reference": self._add_reference,
            "tool": self._add_tool,
        }

    def _add_reference(self, args):
        if not os.path.exists(self._tool_file):
            print(
                f"E: Tool '{args.tool}' does not exist. Please run:\n"
                f"  tnote tool add -n <toolname>\n"
                f"to create the tool file first."
            )
            sys.exit()

        with open(self._tool_file, "r") as file_handler:
            data = json.load(file_handler)

        data[args.name] = args.content

        with open(self._tool_file, "w") as file_handler:
            json.dump(data, file_handler, indent=4)

    def _add_tool(self, args):
        if os.path.exists(self._tool_file):
            print(f"E: Tool {args.name} already exists.")
            sys.exit()

        with open(self._tool_file, "w") as file_handler:
            file_handler.write(json.dumps({}))

    def run(self, args):
        if hasattr(args, "tool"):
            self._tool_file = self._get_tool_file_path(args.tool)
        else:
            self._tool_file = self._get_tool_file_path(args.name)
        self._subcommand_registry[args.subcommand](args)
