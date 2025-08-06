from types import SimpleNamespace

from tnote.commands import add
from tnote.commands import list
from tnote.commands import remove
from tnote.commands.base import BaseCommand

command = BaseCommand.registry.get("add")

populate_tools = ["nvim", "python", "osx", "iterm"]
populate_references = {
    "x": "this is reference x",
    "y": "this is reference y",
    "z": "this is reference z",
}

for tool in populate_tools:
    args = SimpleNamespace(command="add", subcommand="tool", name=tool)
    command.run(args)

    for name, content in populate_references.items():
        args = SimpleNamespace(
            command="add", subcommand="reference", tool=tool, name=name, content=content
        )
        command.run(args)
