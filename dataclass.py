from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    tags: list = field(default_factory=list)


if __name__ == "__main__":
    item = Item("apple", 100, ["fresh", "fruit"])
    print(item)
