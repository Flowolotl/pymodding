class ModComponent:
    def __init__(self, type: str, name: str) -> None:
        self.type = type
        self.name = name
        self.stradd = ""
        self.stradd += f"name={name}"


    def __str__(self) -> str:
        return f"{self.type}({self.stradd})"