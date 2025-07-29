import argparse


def register_arguments(parser, arguments):
    for short, long in arguments:
        parser.add_argument(short, long)


def register_subcommands(subparsers, subcommands_config):
    for subcmd_name, arguments in subcommands_config.items():
        subparser = subparsers.add_parser(subcmd_name)
        register_arguments(subparser, arguments)


def register_commands(subparsers, config):
    for cmd_name, subcmds in config.items():
        cmd_parser = subparsers.add_parser(cmd_name)
        cmd_subparsers = cmd_parser.add_subparsers(dest="subcommand")
        register_subcommands(cmd_subparsers, subcmds)


class Parser:
    def __init__(self, config):
        self.parser = argparse.ArgumentParser()
        subparsers = self.parser.add_subparsers(dest="command")
        register_commands(subparsers, config)

    def parse_args(self):
        return self.parser.parse_args()
