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
        text = self._general_info_to_text()
        return "\n" + tabulate(text, tablefmt="grid")
    
    def get_full_weight(self):
        return self.weight * self.quantity
    
    def _general_info_to_text(self) -> list:
        text = [["Name", self.name], ["Category", self.item_type]]
        if self.description:
            wrapped_description = [textwrap.fill(line, 70, replace_whitespace=False) for line in self.description]
            text.append(["Description", "\n".join(wrapped_description)])
        if self.rarity:
            text.append(["Rarity", self.rarity])
        text.append(["Weight", f"{self.weight if self.weight else 0} lb."])
        text.append(["Quantity", str(self.quantity)])
        return text
    
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
        text = self._general_info_to_text()
        text.append(["Weapon Category", self.weapon_type])
        if self.damage:
            text.append(["Damage", self.damage])
            if self.two_handed_damage:
                text.append(["Two-Handed Damage", self.two_handed_damage])
            text.append(["Damage Type", self.damage_type])
        if len(self.range) == 2:
            text.append(["Range (Normal/Long)", f"{self.range['normal']}/{self.range['long']}"])
        else:
            text.append(["Range (Normal)", f"{self.range['normal']}"])
            if self.throw_range:
                text.append(["Throw Range (Normal/Long)", f"{self.throw_range['normal']}/{self.throw_range['long']}"])
        text.append(["Properties", ", ".join(self.properties)])
        if self.special:
            text.append(["Special", self.special])
        return "\n" + tabulate(text, tablefmt="grid")
    
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
        text = self._general_info_to_text()
        text.append(["Armor Category", self.armor_type])
        text.append(["Armor Class", self.armor_class["base"]])
        text.append(["Dexterity Bonus", "Yes" if self.armor_class["dex_bonus"] else "No"])
        if self.armor_class.get("max_bonus"):
            text.append(["Max Bonus", f"+{self.armor_class['max_bonus']}"])
        text.append(["Strength Minimum", self.str_minimum])
        text.append(["Stealth Disadvantage", "Yes" if self.stealth_disadvantage else "No"])
        return "\n" + tabulate(text, tablefmt="grid")

    
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