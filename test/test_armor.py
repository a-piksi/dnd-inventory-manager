import pytest
from items import Armor

@pytest.fixture
def sample_armor():
    return Armor(
        name="Chainmail",
        item_type="Armor",
        description=["A heavy armor offering excellent protection."],
        weight=55,
        armor_type="Heavy",
        armor_class={"base": 16, "dex_bonus": False},
        str_minimum=13,
        stealth_disadvantage=True,
        rarity="Common",
        quantity=1
    )

def test_armor_initialization(sample_armor):
    assert sample_armor.name == "Chainmail"
    assert sample_armor.item_type == "Armor"
    assert sample_armor.description == ["A heavy armor offering excellent protection."]
    assert sample_armor.weight == 55
    assert sample_armor.armor_type == "Heavy"
    assert sample_armor.armor_class == {"base": 16, "dex_bonus": False}
    assert sample_armor.str_minimum == 13
    assert sample_armor.stealth_disadvantage is True
    assert sample_armor.rarity == "Common"
    assert sample_armor.quantity == 1

def test_create_armor_from_data():
    data = {
        "name": "Leather Armor",
        "desc": ["A lightweight armor offering basic protection."],
        "weight": 10,
        "armor_category": "Light",
        "armor_class": {"base": 11, "dex_bonus": True, "max_bonus": None},
        "str_minimum": 0,
        "stealth_disadvantage": False,
        "rarity": {"name": "Legendary"},
        "quantity": 1
    }
    armor = Armor.create_from_data(data)
    assert armor.name == "Leather Armor"
    assert armor.item_type == "Armor"
    assert armor.description == ["A lightweight armor offering basic protection."]
    assert armor.weight == 10
    assert armor.armor_type == "Light"
    assert armor.armor_class == {"base": 11, "dex_bonus": True, "max_bonus": None}
    assert armor.str_minimum == 0
    assert armor.stealth_disadvantage is False
    assert armor.rarity == "Legendary"
    assert armor.quantity == 1