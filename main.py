from Mod import Mod
from ModBlock import ModBlock
from ModItem import ModItem
from ModMixin import ModMixin
from ModEnvironment import ModEnvironment
from ModLoader import ModLoader
from ModSettings import ModSettings


def main():
    print("Hello world")
    mod = Mod(ModSettings(environment=ModEnvironment.Client, loaders=[ModLoader.Fabric]), id="flawed")
    block = ModBlock("test_block")
    item = ModItem("test_item")
    mixin = ModMixin("test_mixin")
    mod.register(block)
    mod.register(item)
    mod.register(mixin)


if __name__ == "__main__":
    main()