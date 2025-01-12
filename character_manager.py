import os

from item_library import ItemLibrary
from utility import Utility
from character import Character, Inventory

class CharacterManager:
    def __init__(self):
        if os.path.isfile("characters.pkl"):
            self.characters = Utility.from_file("characters.pkl")
        else:
            self.characters = []
    
    def create_new_character(self, name: str, race: str, character_class: str, strength: int, items: list):
        inventory = Inventory()
        for item in items:
            inventory.add(item)
        
        character = Character(name, race, character_class, strength, inventory)
        self.characters.append(character)
    
    def remove_character(self, character: Character):
        self.characters.remove(character)
    
    @property
    def characters(self):
        return self._characters
    
    @characters.setter
    def characters(self, value):
        if not isinstance(value, list):
            raise TypeError("Characters attribute must be a list")
        self._characters = value