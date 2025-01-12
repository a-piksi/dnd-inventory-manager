import pytest
from character import Inventory
from items import Item, Weapon, Armor

@pytest.fixture
def inventory():
    return Inventory()

@pytest.fixture
def sample_items():
    item = Item("Potion", "Item", ["Heals 10 HP"], 0.5, "Common", 2)
    weapon = Weapon("Sword", "Weapon", ["A sharp blade"], 3, "Martial Melee", 
                    "1d8", ["Slashing"], ["Versatile"], {"normal": 0}, "Rare", 1)
    armor = Armor("Shield", "Armor", ["Protects against attacks"], 6, "Heavy", 
                  {"base": 16, "dex_bonus": False}, 13, True, "Uncommon", 1)
    return item, weapon, armor

def test_inventory_initialization(inventory):
    assert inventory.items == []
    assert inventory.weapons == []
    assert inventory.armor == []
    assert inventory.total_weight == 0

def test_add_item_to_inventory(inventory, sample_items):
    item, weapon, armor = sample_items

    inventory.add(item)
    inventory.add(weapon)
    inventory.add(armor)

    assert item in inventory.items
    assert weapon in inventory.weapons
    assert armor in inventory.armor
    assert inventory.total_weight == (item.weight * item.quantity + weapon.weight * weapon.quantity + armor.weight * armor.quantity)

def test_remove_item_from_inventory(inventory, sample_items):
    item, weapon, armor = sample_items

    inventory.add(item)
    inventory.add(weapon)
    inventory.add(armor)
    inventory.remove(item)

    assert item not in inventory.items
    assert weapon in inventory.weapons
    assert armor in inventory.armor
    assert inventory.total_weight == (weapon.weight * weapon.quantity + armor.weight * armor.quantity)

def test_change_weight(inventory, sample_items):
    item, _, _ = sample_items
    inventory.add(item)

    inventory.change_weight(item.weight, item.quantity, 4)

    assert inventory.total_weight == (item.weight * 4)

def test_get_full_list(inventory, sample_items):
    item, weapon, armor = sample_items

    inventory.add(item)
    inventory.add(weapon)
    inventory.add(armor)

    full_list = inventory.get_full_list()
    assert len(full_list) == 3
    assert item in full_list
    assert weapon in full_list
    assert armor in full_list

def test_negative_total_weight(inventory):
    with pytest.raises(ValueError, match="Total weight cannot be negative."):
        inventory.total_weight = -10