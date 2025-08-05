import os
import json

from tnote.registry import BaseCommand


class AddCommand(BaseCommand):
    def __init__(self):
        self.subcommand_registry = {
            "reference": self.add_reference,
            "tool": self.add_tool,
        }

    def add_reference(self, args):
        if not os.path.exists(self.tool_file):
            print(
                f'error: tool {args.tool} doesn\'t exist, run "tnote tool add -n <toolname>" first to create the tool file'
            )
            return

        with open(self.tool_file, "r") as file_handler:
            data = json.load(file_handler)
            file_handler.close()

        data[args.name] = args.content

        with open(self.tool_file, "w") as file_handler:
            json.dump(data, file_handler, indent=4)
            file_handler.close()

    def add_tool(self, args):
        if os.path.exists(self.tool_file):
            print(f"error: tool {args.name} already exists")
            return

        with open(self.tool_file, "w") as file_handler:
            file_handler.write(json.dumps({}))
            file_handler.close()

    def run(self, args):
        if hasattr(args, "tool"):
            self.tool_file = self.get_tool_file_path(args.tool)
        else:
            self.tool_file = self.get_tool_file_path(args.name)
        self.subcommand_registry[args.subcommand](args)
