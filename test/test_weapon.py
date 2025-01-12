import pytest
from items import Weapon

@pytest.fixture
def sample_weapon():
    return Weapon(
        name="Longsword",
        item_type="Weapon",
        description=["A versatile blade favored by many adventurers."],
        weight=3,
        weapon_type="Martial Melee",
        damage="1d8",
        damage_type=["Slashing"],
        properties=["Versatile"],
        range={"normal": 0},
        two_handed_damage="1d10",
        rarity="Common",
        quantity=1
    )

def test_weapon_initialization(sample_weapon):
    assert sample_weapon.name == "Longsword"
    assert sample_weapon.item_type == "Weapon"
    assert sample_weapon.description == ["A versatile blade favored by many adventurers."]
    assert sample_weapon.weight == 3
    assert sample_weapon.weapon_type == "Martial Melee"
    assert sample_weapon.damage == "1d8"
    assert sample_weapon.damage_type == ["Slashing"]
    assert sample_weapon.properties == ["Versatile"]
    assert sample_weapon.range == {"normal": 0}
    assert sample_weapon.two_handed_damage == "1d10"
    assert sample_weapon.rarity == "Common"
    assert sample_weapon.quantity == 1

def test_create_weapon_from_data():
    data = {
        "name": "Javelin",
        "desc": ["A thrown weapon used for ranged attacks."],
        "weight": 2,
        "category_range": "Simple Melee",
        "damage": {"damage_dice": "1d6", "damage_type": {"name": "Piercing"}},
        "properties": [{"name": "Thrown"}],
        "range": {"normal": 30, "long": 120},
        "throw_range": {"normal": 30, "long": 120},
        "special": ["This weapon can be thrown."],
        "rarity": {"name": "Rare"},
        "quantity": 5
    }
    weapon = Weapon.create_from_data(data)
    assert weapon.name == "Javelin"
    assert weapon.weapon_type == "Simple Melee"
    assert weapon.damage == "1d6"
    assert weapon.damage_type == "Piercing"
    assert weapon.properties == ["Thrown"]
    assert weapon.range == {"normal": 30, "long": 120}
    assert weapon.throw_range == {"normal": 30, "long": 120}
    assert weapon.special == ["This weapon can be thrown."]
    assert weapon.rarity == "Rare"
    assert weapon.quantity == 5