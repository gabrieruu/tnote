from tnote.registry import CommandRegistry


class AddCommand(CommandRegistry):
    def __init__(self) -> None:
        pass

    def run(self, args):
        print("Hello World!")
        print(args)
        print(self.registry)
