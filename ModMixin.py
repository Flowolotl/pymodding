from ModComponent import ModComponent

class ModMixin(ModComponent):
    def __init__(self, name, target) -> None:
        super().__init__(__class__.__name__, name)
        self.target_class = target