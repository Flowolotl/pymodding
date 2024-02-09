from ModComponent import ModComponent
from ModBlock import ModBlock
from ModItem import ModItem
from ModMixin import ModMixin
from ModLoader import ModLoader
from ModSettings import ModSettings


class Mod:
    def __init__(self, settings: ModSettings, id=None,) -> None:
        if id is None:
            return TypeError()
        self.id = id
        self.settings = {
            "loaders": []
        }
        self.items: dict[ModItem, dict] = {}
        self.blocks: dict[ModBlock, dict] = {}
        self.mixin: dict[ModMixin, dict] = {}


    def register(self, comp: ModComponent):
        print(f"registering on id '{self.id}': {comp}")


    def build(self):
        print("building mod")