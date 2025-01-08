class Item:
    def __init__(self, name: str, index: str, item_type: str, description: list, weight: float, 
                 rarity=None, quantity=1):
        self.name = name
        self.index = index
        self.item_type = item_type
        self.description = description
        self.weight = weight
        self.rarity = rarity
        self.quantity = quantity
    
    @classmethod
    def create_from_data(cls, data: dict):
        return cls(
            name=data.get("name"),
            index=data.get("index"),
            item_type=data.get("equipment_category", {}).get("name"),
            description=data.get("desc"),
            weight=data.get("weight"),
            rarity=data.get("rarity"),
            quantity=data.get("quantity")
        )

class Weapon(Item):
    def __init__(self, name: str, index: str, item_type: str, description: list, weight: float, 
                 weapon_type: str, damage: str, damage_type: list, properties: list, 
                 range: dict, throw_range=None, two_handed_damage=None, special=None, 
                 rarity=None, quantity=1):
        super().__init__(name, index, item_type, description, weight, rarity, quantity)
        self.weapon_type = weapon_type
        self.damage = damage
        self.damage_type = damage_type
        self.properties = properties
        self.range = range
        self.throw_range = throw_range
        self.two_handed_damage = two_handed_damage
        self.special = special
    
    @classmethod
    def create_from_data(cls, data: dict):
        return cls(
            name=data.get("name"),
            index=data.get("index"),
            item_type="Weapon",
            description=data.get("desc"),
            weight=data.get("weight"),
            weapon_type=data.get("category_range"),
            damage=data.get("damage", {}).get("damage_dice"),
            damage_type=data.get("damage", {}).get("damage_type", {}).get("name"),
            properties=[prop["name"] for prop in data.get("properties", [])],
            range_normal=data.get("range"),
            throw_range=data.get("throw_range"),
            two_handed_damage=data.get("two_handed_damage", {}).get("damage_dice"),
            special=data.get("special"),
            rarity=data.get("rarity"),
            quantity=data.get("quantity")
            )

class Armor(Item):
    def __init__(self, name: str, index: str, item_type: str, description: list, weight: float, 
                 armor_type: str, armor_class: dict, str_minimum: int, stealth_disadvantage: bool, 
                 rarity=None, quantity=1):
        super().__init__(name, index, item_type, description, weight, rarity, quantity)
        self.armor_type = armor_type
        self.armor_class = armor_class
        self.str_minimum = str_minimum
        self.stealth_disadvantage = stealth_disadvantage
    
    @classmethod
    def create_from_data(cls, data: dict):
        return cls(
            name=data.get("name"),
            index=data.get("index"),
            item_type="Armor",
            description=data.get("desc"),
            weight=data.get("weight"),
            armor_type=data.get("armor_category"),
            armor_class=data.get("armor_class"),
            str_minimum=data.get("str_minimum"),
            stealth_disadvantage=data.get("stealth_disadvantage"),
            rarity=data.get("rarity"),
            quantity=data.get("quantity")
        )