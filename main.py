from Mod import Mod
from ModBlock import ModBlock
from ModItem import ModItem
from ModMixin import ModMixin
from ModEnvironment import ModEnvironment
from ModLoader import ModLoader
from ModSettings import ModSettings
from ModEntity import ModEntity


def main():
    settings = ModSettings(environment=ModEnvironment.Client, loaders=[ModLoader.Fabric])
    mod = Mod(settings, name="PlayFlawed")
    block = ModBlock("test_block")
    item = ModItem("test_item")
    mixin = ModMixin("test_mixin", "LivingEntity")
    # entity = ModEntity("ExampleEntity")
    mod.register(block)
    mod.register(item)
    mod.register(mixin)
    mod.build()


if __name__ == "__main__":
    main()