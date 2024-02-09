from ModLoader import ModLoader
from ModEnvironment import ModEnvironment


class ModSettings:
    def __init__(self, loaders=[ModLoader.Fabric], environment=ModEnvironment.Both) -> None:
        self.loaders: list[ModLoader] = loaders
        self.environment: ModEnvironment = environment