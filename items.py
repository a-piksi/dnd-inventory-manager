import textwrap

from tabulate import tabulate

class Item:
    def __init__(self, name: str, item_type: str, description: list, weight: int | float, 
                 rarity=None, quantity=1):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.weight = weight
        self.rarity = rarity
        self.quantity = quantity
    
    def __str__(self):
        text = [f"Name: {self.name}", f"Category: {self.item_type}"]
        if self.description:
            text.append(f"Description: {"\n".join(self.description)}")
        if self.rarity:
            text.append(f"Rarity: {self.rarity}")
        text.append(f"Weight: {self.weight if self.weight else 0} lb.")
        text.append(f"Quantity: {self.quantity}\n")
        wrapped_text = [textwrap.fill(line, 90, replace_whitespace=False) for line in text]
        return "\n" + tabulate([["\n".join(wrapped_text)]], tablefmt="grid")
    
    def get_full_weight(self):
        return self.weight * self.quantity

    
    @classmethod
    def create_from_data(cls, data: dict):
        return cls(
            name=data.get("name"),
            item_type=data.get("equipment_category", {}).get("name"),
            description=data.get("desc"),
            weight=data.get("weight", 0),
            rarity=data.get("rarity", {}).get("name"),
            quantity=data.get("quantity", 1)
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        if not value:
            raise ValueError("Item type cannot be empty.")
        self._item_type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative.")
        self._weight = value

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, value):
        self._rarity = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value

class Weapon(Item):
    def __init__(self, name: str, item_type: str, description: list, weight: int | float, 
                 weapon_type: str, damage: str, damage_type: list, properties: list, 
                 range: dict, throw_range=None, two_handed_damage=None, special=None, 
                 rarity=None, quantity=1):
        super().__init__(name, item_type, description, weight, rarity, quantity)
        self.weapon_type = weapon_type
        self.damage = damage
        self.damage_type = damage_type
        self.properties = properties
        self.range = range
        self.throw_range = throw_range
        self.two_handed_damage = two_handed_damage
        self.special = special
    
    def __str__(self):
        text = [f"Name: {self.name}", f"Category: {self.item_type}"]
        text.append(f"Weapon category: {self.weapon_type}")
        if self.description:
            text.append(f"Description: {"\n".join(self.description)}")
        if self.rarity:
            text.append(f"Rarity: {self.rarity}")
        if self.damage:
            text.append(f"Damage: {self.damage}")
            if self.two_handed_damage:
                text.append(f"Two-handed damage: {self.two_handed_damage}")
            text.append(f"Damage type: {self.damage_type}")
        if len(self.range) == 2:
            text.append(f"Range (normal/long): {self.range["normal"]}/{self.range["long"]}")
        else:
            text.append(f"Range (normal): {self.range["normal"]}")
            if self.throw_range:
                text.append(f"Throw range (normal/long): {self.throw_range["normal"]}/{self.throw_range["long"]}")
        text.append(f"Properties: {", ".join(self.properties)}")
        if self.special:
            text.append(f"Special: {self.special}")
        text.append(f"Weight: {self.weight if self.weight else 0} lb.")
        text.append(f"Quantity: {self.quantity}")
        wrapped_text = [textwrap.fill(line, 90, replace_whitespace=False) for line in text]
        return "\n" + tabulate([["\n".join(wrapped_text)]], tablefmt="grid")
    
    @classmethod
    def create_from_data(cls, data: dict):
        return cls(
            name=data.get("name"),
            item_type="Weapon",
            description=data.get("desc"),
            weight=data.get("weight", 0),
            weapon_type=data.get("category_range"),
            damage=data.get("damage", {}).get("damage_dice"),
            damage_type=data.get("damage", {}).get("damage_type", {}).get("name"),
            properties=[prop["name"] for prop in data.get("properties", [])],
            range=data.get("range"),
            throw_range=data.get("throw_range"),
            two_handed_damage=data.get("two_handed_damage", {}).get("damage_dice"),
            special=data.get("special"),
            rarity=data.get("rarity", {}).get("name"),
            quantity=data.get("quantity", 1)
            )

class Armor(Item):
    def __init__(self, name: str, item_type: str, description: list, weight: int | float, 
                 armor_type: str, armor_class: dict, str_minimum: int, stealth_disadvantage: bool, 
                 rarity=None, quantity=1):
        super().__init__(name, item_type, description, weight, rarity, quantity)
        self.armor_type = armor_type
        self.armor_class = armor_class
        self.str_minimum = str_minimum
        self.stealth_disadvantage = stealth_disadvantage
    
    def __str__(self):
        text = [f"Name: {self.name}", f"Category: {self.item_type}"]
        text.append(f"Armor category: {self.armor_type}")
        if self.description:
            text.append(f"Description: {"\n".join(self.description)}")
        if self.rarity:
            text.append(f"Rarity: {self.rarity}")
        text.append(f"Armor class: {self.armor_class["base"]}")
        text.append(f"Dexterity bonus: {"Yes" if self.armor_class["dex_bonus"] else "No"}")
        if self.armor_class.get("max_bonus"):
            text.append(f"Max bonus: +{self.armor_class["max_bonus"]}")
        text.append(f"Strength minimum: {self.str_minimum}")
        text.append(f"Stealth disadvantage: {"Yes" if self.stealth_disadvantage else "No"}")
        text.append(f"Weight: {self.weight if self.weight else 0} lb.")
        text.append(f"Quantity: {self.quantity}")
        wrapped_text = [textwrap.fill(line, 90, replace_whitespace=False) for line in text]
        return "\n" + tabulate([["\n".join(wrapped_text)]], tablefmt="grid")

    
    @classmethod
    def create_from_data(cls, data: dict):
        return cls(
            name=data.get("name"),
            item_type="Armor",
            description=data.get("desc"),
            weight=data.get("weight", 0),
            armor_type=data.get("armor_category"),
            armor_class=data.get("armor_class"),
            str_minimum=data.get("str_minimum"),
            stealth_disadvantage=data.get("stealth_disadvantage"),
            rarity=data.get("rarity", {}).get("name"),
            quantity=data.get("quantity", 1)
        )