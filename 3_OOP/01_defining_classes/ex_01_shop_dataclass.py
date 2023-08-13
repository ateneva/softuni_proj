from dataclasses import dataclass


@dataclass()
class Shop:
    name: str
    items: list

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())