import os
import copy

from utility import Utility
from items import Item, Weapon, Armor

OFFICIAL_FILE = "official.pkl"

class ItemLibrary:
    def __init__(self):
        if os.path.isfile(OFFICIAL_FILE):
            self.official = Utility.from_file(OFFICIAL_FILE)
        else:
            self.official = self.from_api()
    
    def from_api(self) -> list:
        print("Updating database...")
        item_list = []

        equipment_url = "https://www.dnd5eapi.co/api/equipment"
        equipment_response = Utility.get_response(equipment_url)

        for result in equipment_response["results"]:
            item_response = Utility.get_response(equipment_url + f"/{result["index"]}")
            match item_response["equipment_category"]["name"]:
                case "Weapon":
                    item_list.append(Weapon.create_from_data(item_response))
                case "Armor":
                    item_list.append(Armor.create_from_data(item_response))
                case _:
                    item_list.append(Item.create_from_data(item_response))
        
        magic_url = "https://www.dnd5eapi.co/api/magic-items"
        magic_response = Utility.get_response(magic_url)

        for result in magic_response["results"]:
            item_response = Utility.get_response(magic_url + f"/{result["index"]}")
            item_list.append(Item.create_from_data(item_response))
        
        print("Done!")
        Utility.to_file(OFFICIAL_FILE, item_list)
        return item_list
    
    def search_items(self, keyword: str):
        items_found = [item for item in self.official if keyword.lower() in item.name.lower()]
        return items_found
    
    def create_magic_item(self, magic_item: Item, non_magic_item: Weapon | Armor, quantity: int):
        merged_item = copy.deepcopy(non_magic_item)
        merged_item.name = f"{magic_item.name} ({merged_item.name})"
        merged_item.rarity = magic_item.rarity
        merged_item.description += ["Magical properties:"] + magic_item.description
        merged_item.quantity = quantity
        return merged_item
    
    def create_regular_item(self, item: Item, quantity: int):
        copied_item = copy.deepcopy(item)
        copied_item.quantity = quantity
        return copied_item


def main():
    item_library = ItemLibrary()


if __name__ == "__main__":
    main()