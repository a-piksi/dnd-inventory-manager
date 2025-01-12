from tabulate import tabulate

from items import Item, Weapon, Armor

class Inventory:
    def __init__(self):
        self.items = []
        self.weapons = []
        self.armor = []
        self.total_weight = 0
    
    def __str__(self):
        text = ""
        counter = iter(range(1, (1 + len(self.items) + len(self.weapons) + len(self.armor))))

        if self.items:
            item_list = [f"{next(counter)}. {item.quantity}x {item.name}" for item in self.items]
            text += f"\nItems:\n{"\n".join(item_list)}\n"
        if self.weapons:
            weapon_list = [f"{next(counter)}. {weapon.quantity}x {weapon.name}" for weapon in self.weapons]
            text += f"\nWeapons:\n{"\n".join(weapon_list)}\n"
        if self.armor:
            armor_list = [f"{next(counter)}. {armor.quantity}x {armor.name}" for armor in self.armor]
            text += f"\nArmor:\n{"\n".join(armor_list)}\n"
        
        return text
    
    def add(self, item: Item):
        attribute_by_type = {Item: self.items, Weapon: self.weapons, Armor: self.armor}
        attribute_by_type[type(item)].append(item)

        self.total_weight += item.weight * item.quantity
    
    def get_full_list(self) -> list:
        return self.items + self.weapons + self.armor
    
    def change_weight(self, weight: int | float, old_quantity: int, new_quantity: int):
        difference = new_quantity - old_quantity
        self.total_weight += difference * weight
    
    def remove(self, item: Item):
        attribute_by_type = {Item: self.items, Weapon: self.weapons, Armor: self.armor}
        attribute_by_type[type(item)].remove(item)

        self.total_weight -= item.weight * item.quantity


class Character:
    def __init__(self, name: str, race: str, character_class: str, strength: int, inventory: Inventory):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.strength = strength
        self.carry_capacity = strength * 15
        self.inventory = inventory
    
    def __str__(self):
        text = (f"\nName: {self.name} | Race: {self.race} | Class: {self.character_class} | "
                + f"Strength score: {self.strength}\n\nCurrent load: {self.inventory.total_weight}"
                + f"/{self.carry_capacity} lb.")
        if self.inventory.total_weight > self.carry_capacity:
            text += " *ENCUMBERED*"
        text += f"\n{self.inventory}"
        return "\n" + tabulate([[text]], tablefmt="grid") + "\n"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def character_class(self):
        return self._character_class

    @character_class.setter
    def character_class(self, value):
        if not value:
            raise ValueError("Character class cannot be empty.")
        self._character_class = value

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        if not isinstance(value, Inventory):
            raise TypeError("Inventory must be an instance of the Inventory class.")
        self._inventory = value
