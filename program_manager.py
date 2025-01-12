from item_library import ItemLibrary
from character_manager import CharacterManager
from utility import Utility
from character import Character
from items import Item

class ProgramManager:
    item_library = ItemLibrary()
    character_manager = CharacterManager()

    @classmethod
    def library_mode(cls):
        while True:
            selected_item = cls._search(exit_message="exit to the previous menu")
            if selected_item is None:
                break
            print(selected_item)
    
    @classmethod
    def character_mode(cls):
        while True:
            modes = ["Add new character"]
            if cls.character_manager.characters:
                modes += ["Use existing character", "Delete a character"]
            print("\nChoose the mode by inputing a number from the list.\nPress CTRL+C to exit to the main menu.\n")
            index = Utility.menu_choice(modes)
            if index is None:
                break

            match modes[index]:
                case "Add new character":
                    cls._add_character_mode()
                case "Use existing character":
                    cls._existing_character_mode()
                case "Delete a character":
                    cls._delete_character_mode()
        
        # Update character.pkl file
        Utility.to_file("characters.pkl", cls.character_manager.characters)
    
    @classmethod
    def _search(cls, exit_message: str, item_type=None):
        while True:
            print(f"\nEnter a keyword or part of the item's name to search for matching items.\nPress CTRL+C to {exit_message}.")
            try:
                keyword = input("Keyword: ").strip()
            except KeyboardInterrupt:
                print()
                return None

            found_items = cls.item_library.search_items(keyword, item_type)
            if not found_items:
                print("\nNo matches found.")
                continue

            found_items_names = [item.name for item in found_items]
            print("\nSelect an item to see it's information by entering a number from the list.\nPress CTRL+C to enter another keyword.\n")
            index = Utility.menu_choice(found_items_names)
            if index is None:
                continue
            
            return found_items[index]
    
    @classmethod
    def _add_character_mode(cls):
        print("\nEnter the attributes of your character.\nPress CTRL+C to exit to the previous menu\n")
        try:
            name = Utility.get_not_empty_str("Name: ")
            race = Utility.get_not_empty_str("Race: ")
            character_class = Utility.get_not_empty_str("Class: ")
        except KeyboardInterrupt:
            return
        
        strength = Utility.get_non_negative_int("Strength score: ")
        if strength is None: return
        
        items_to_add = []
        print(f"\nAdd item(s) to {name}'{"s" if not name.endswith("s") else ""} inventory.")
        while True:
            new_item = cls._add_item_to_inventory()
            if new_item is None: break

            items_to_add.append(new_item)
        
        cls.character_manager.create_new_character(name, race, character_class, strength, items_to_add)
        print(f"\nCharacter \"{name}\" has been created successfully!")
    
    @classmethod
    def _add_item_to_inventory(cls):
        while True:
            selected_item = cls._search(exit_message="stop adding items")
            if selected_item is None:
                return None

            print(selected_item)
            print("\nWould you like to add this item to the inventory?")
            index = Utility.menu_choice(["Yes", "No"])
            if index is None or index == 1: continue

            quantity = Utility.get_non_negative_int("\nSelect quantity: ")
            if quantity is None: continue

            # Items are magical if rarity attribute exist; Magic items of type "Weapon" or "Armor"
            # need to be merged with a regular item of the same type
            if selected_item.rarity and selected_item.item_type in ["Weapon", "Armor"]:
                print(f"\nSelect an item of category \"{selected_item.item_type}\", which is mentioned in the description.")
                selected_sub_item = cls._search("cancel adding this item", selected_item.item_type)
                if selected_sub_item is None: continue

                new_item = cls.item_library.create_magic_item(selected_item, selected_sub_item, quantity)
            else:
                new_item = cls.item_library.create_regular_item(selected_item, quantity)
            
            print(f"\nAn item \"{new_item.name}\" has been added successfully!")
            return new_item
    
    @classmethod
    def _existing_character_mode(cls):
        while True:
            character = cls._choose_character_from_list()
            if character is None: return

            while True:
                print(character)
                print("Choose the mode by inputing a number from the list.\nPress CTRL+C to exit to the previous menu\n")
                modes = ["Choose an item", "Add an item"]
                index = Utility.menu_choice(modes)
                if index is None: break

                match modes[index]:
                    case "Choose an item":
                        cls._choose_item_mode(character)
                    case "Add an item":
                        cls._add_item_to_inventory_mode(character)
    
    @classmethod
    def _choose_character_from_list(cls):
        print("\nChoose a character by inputing a number from the list.\nPress CTRL+C to exit to the previous menu\n")

        characters = cls.character_manager.characters
        character_names = [f"{character.name}, {character.character_class}" for character in characters]
        index = Utility.menu_choice(character_names)
        if index is None: return None

        return characters[index]
    
    @classmethod
    def _choose_item_mode(cls, character: Character):
        items = character.inventory.get_full_list()
        while True:
            print(character)
            print("Choose an item by inputing a number.\nPress CTRL+C to exit to the previous menu\n")
            index = Utility.menu_choice(items, print_list=False)
            if index is None: return

            chosen_item = items[index]
            print(chosen_item)
            print("\nChoose the mode by inputing a number from the list.\nPress CTRL+C to exit to the previous menu\n")
            modes = ["Change quantity", "Remove item from inventory"]
            index = Utility.menu_choice(modes)
            if index is None: continue

            match modes[index]:
                case "Change quantity":
                    cls._change_quantity_mode(character, chosen_item)
                case "Remove item from inventory":
                    cls._remove_item_mode(character, chosen_item)
    
    @classmethod
    def _change_quantity_mode(cls, character: Character, chosen_item: Item):
        quantity = Utility.get_non_negative_int("\nSelect quantity: ")
        if quantity is None: return
         
        old_quantity = chosen_item.quantity
        chosen_item.quantity = quantity
        character.inventory.change_weight(chosen_item.weight, old_quantity, quantity)
        print("\nQuantity has been changed successfully!")
    
    @classmethod
    def _remove_item_mode(cls, character: Character, chosen_item: Item):
        print("\nWould you like to remove this item from the inventory?")
        index = Utility.menu_choice(["Yes", "No"])
        if index is None or index == 1: return

        character.inventory.remove(chosen_item)
        print("\nThe item has been removed successfully!")
    
    @classmethod
    def _add_item_to_inventory_mode(cls, character: Character):
        new_item = cls._add_item_to_inventory()
        if new_item is None: return

        character.inventory.add(new_item)
    
    @classmethod
    def _delete_character_mode(cls):
        while True:
            character = cls._choose_character_from_list()
            if character is None: return

            print(f"\nAre you sure you want to delete {character.name}, {character.character_class}?")
            index = Utility.menu_choice(["Yes", "No"])
            if index is None or index == 1: continue

            cls.character_manager.remove_character(character)


def main():
    print("Testing")
    # ProgramManager._search_mode()
    ProgramManager._add_character_mode()
    # ProgramManager._existing_character_mode()


if __name__ == "__main__":
    main()
