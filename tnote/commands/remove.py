from tnote.registry import CommandRegistry


class RemoveCommand(CommandRegistry):
    def __init__(self) -> None:
        pass

    def run(self, args):
        print("Hello World!")
        print(args)
