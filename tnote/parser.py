import argparse


class Parser:
    """
    Parses CLI commands and subcommands for the `tnote` tool using argparse.

    Commands, subcommands, and arguments are defined in the `CLI_CONFIG`
    constant and dynamically registered via subparsers.

    See: https://docs.python.org/3/library/argparse.html
    """

    def __init__(self, cli_config):
        self.parser = argparse.ArgumentParser()
        subparsers = self.parser.add_subparsers(dest="command")

        self._register_commands(subparsers, cli_config)

    def _register_arguments(self, parser, arguments):
        for short, long in arguments:
            parser.add_argument(short, long, required=True)

    def _register_subcommands(self, subparsers, subcommands_config):
        for subcmd_name, arguments in subcommands_config.items():
            parser = subparsers.add_parser(subcmd_name)
            self._register_arguments(parser, arguments)

    def _register_commands(self, subparsers, cli_config):
        for cmd_name, subcmds in cli_config.items():
            cmd_parser = subparsers.add_parser(cmd_name)

            if subcmds:
                cmd_subparsers = cmd_parser.add_subparsers(
                    dest="subcommand", required=True
                )
                self._register_subcommands(cmd_subparsers, subcmds)

    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()

    def print_help(self) -> None:
        return self.parser.print_help()
