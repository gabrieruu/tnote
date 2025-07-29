class CommandRegistry:
    registry = {}

    def __init_subclass__(cls):
        name = cls.__name__.lower().replace("command", "")
        cls.registry[name] = cls()
