from tnote.registry import CommandRegistry


class ListCommand(CommandRegistry):
    def __init__(self) -> None:
        pass

    def run(self, args):
        print("Hello World!")
        print(args)
