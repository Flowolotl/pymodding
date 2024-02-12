import re
import os
import shutil


from ModComponent import ModComponent
from ModBlock import ModBlock
from ModItem import ModItem
from ModMixin import ModMixin
from ModLoader import ModLoader
from ModSettings import ModSettings


class Mod:
    def __init__(self, settings: ModSettings, name=None, id=None,) -> None:
        if name is None:
            return TypeError()
        self.name = name
        self.id = id or re.sub(r'(?<!^)(?=[A-Z])', "_", name).lower()
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
        if os.path.exists("./out"):
            shutil.rmtree("./out")
        os.mkdir("./out")