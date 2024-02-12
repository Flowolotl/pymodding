from ModComponent import ModComponent

class ModItem(ModComponent):
    def __init__(self, name) -> None:
        super().__init__(__class__.__name__, name)
