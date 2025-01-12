import pytest

from items import Item

@pytest.fixture
def sample_item():
    return Item(
        name="Sword",
        item_type="Weapon",
        description=["A sharp blade used for combat."],
        weight=3,
        rarity="Common",
        quantity=2
    )

def test_item_initialization(sample_item):
    assert sample_item.name == "Sword"
    assert sample_item.item_type == "Weapon"
    assert sample_item.description == ["A sharp blade used for combat."]
    assert sample_item.weight == 3
    assert sample_item.rarity == "Common"
    assert sample_item.quantity == 2

def test_item_full_weight(sample_item):
    assert sample_item.get_full_weight() == 6

def test_general_info_to_text(sample_item):
    text = sample_item._general_info_to_text()
    assert text == [
        ["Name", "Sword"],
        ["Category", "Weapon"],
        ["Description", "A sharp blade used for combat."],
        ["Rarity", "Common"],
        ["Weight", "3 lb."],
        ["Quantity", "2"]
    ]

def test_create_from_data():
    data = {
        "name": "Shield",
        "equipment_category": {"name": "Armor"},
        "desc": ["Provides protection."],
        "weight": 6,
        "rarity": {"name": "Uncommon"},
        "quantity": 1
    }
    item = Item.create_from_data(data)
    assert item.name == "Shield"
    assert item.item_type == "Armor"
    assert item.description == ["Provides protection."]
    assert item.weight == 6
    assert item.rarity == "Uncommon"
    assert item.quantity == 1

def test_invalid_name():
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Item(name="", item_type="Weapon", description=[], weight=2)

def test_invalid_item_type():
    with pytest.raises(ValueError, match="Item type cannot be empty."):
        Item(name="Sword", item_type="", description=[], weight=2)

def test_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative."):
        Item(name="Sword", item_type="Weapon", description=[], weight=-1)

def test_negative_quantity():
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Item(name="Sword", item_type="Weapon", description=[], weight=2, quantity=-1)