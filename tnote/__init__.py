from tnote.config import init_config
from tnote.parser import Parser
from tnote.registry import CommandRegistry
import tnote.commands
import sys

CLI_CONFIG = {
    "add": {
        "tool": [
            ("-n", "--name"),
        ],
        "reference": [
            ("-t", "--tool"),
            ("-n", "--name"),
            ("-c", "--content"),
        ],
    },
    "list": {},
    "remove": {
        "tool": [],
        "reference": [],
    },
}


def main():
    init_config()
    parser = Parser(CLI_CONFIG)
    args = parser.parse_args()

    command = CommandRegistry.registry.get(args.command)
    if command:
        command.run(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    sys.exit(main())
