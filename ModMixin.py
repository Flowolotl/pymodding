from ModComponent import ModComponent

class ModMixin(ModComponent):
    def __init__(self, name) -> None:
        super().__init__("ModMixin", name)