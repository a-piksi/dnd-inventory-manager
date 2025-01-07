class Item:
    def __init__(self, name: str, index: str, item_type: str, description: list, weight: float, quantity: int, 
                 rarity=None):
        self.name = name
        self.index = index
        self.item_type = item_type
        self.description = description
        self.weight = weight
        self.quantity = quantity
        self.rarity = rarity

class Weapon(Item):
    def __init__(self, name: str, index: str, item_type: str, description: list, weight: float, quantity: int, 
                 weapon_type: str, range: str, properties: list, rarity=None):
        super().__init__(name, index, item_type, description, weight, quantity, rarity)
        self.weapon_type = weapon_type
        self.range = range
        self.properties = properties

class Armor(Item):
    def __init__(self, name: str, index: str, item_type: str, description: list, weight: float, quantity: int, 
                 armor_type: str, ac_base: int, dex_bonus: bool, max_bonus: int, str_minimum: int, stealth_disadvantage: bool, 
                 rarity=None):
        super().__init__(name, index, item_type, description, weight, quantity, rarity)
        self.armor_type = armor_type
        self.ac_base = ac_base
        self.dex_bonus = dex_bonus
        self.max_bonus = max_bonus
        self.str_minimum = str_minimum
        self.stealth_disadvantage = stealth_disadvantage