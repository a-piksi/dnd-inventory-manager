import pytest
from character import Character, Inventory

@pytest.fixture
def inventory():
    inventory = Inventory()
    return inventory

@pytest.fixture
def character(inventory):
    return Character("Bob", "Human", "Fighter", 15, inventory)

def test_character_initialization(character, inventory):
    assert character.name == "Bob"
    assert character.race == "Human"
    assert character.character_class == "Fighter"
    assert character.strength == 15
    assert character.carry_capacity == 225
    assert character.inventory == inventory

def test_character_name_setter(character):
    character.name = "Shadow"
    assert character.name == "Shadow"

    with pytest.raises(ValueError, match="Name cannot be empty."):
        character.name = ""

def test_character_class_setter(character):
    character.character_class = "Rogue"
    assert character.character_class == "Rogue"

    with pytest.raises(ValueError, match="Character class cannot be empty."):
        character.character_class = ""

def test_inventory_setter(character, mocker):
    new_inventory = mocker.Mock(spec=Inventory)
    character.inventory = new_inventory
    assert character.inventory == new_inventory

    with pytest.raises(TypeError, match="Inventory must be an instance of the Inventory class."):
        character.inventory = "Not an inventory"