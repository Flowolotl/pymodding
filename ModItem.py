from ModComponent import ModComponent

class ModItem(ModComponent):
    def __init__(self, name) -> None:
        super().__init__("ModItem", name)