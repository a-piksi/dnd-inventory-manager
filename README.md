# DnD Inventory Tracker

A Python-based tool to manage and organize character inventories for Dungeons & Dragons 5e. The program provides two primary modes of operation:
1. **Items Library**: Search for items.
2. **Character Inventories**: Create characters, manage their inventories, and add or remove items.

---

## Features

### Items Library
- Search for items by name or category using keywords.
- View detailed information about items.

### Character Inventories
- Create new characters with attributes like name, race, class, and strength.
- Add items to characters' inventories from the library or as custom items.
- Modify existing characters:
  - View inventory.
  - Add or remove items.
  - Change item quantities.
- Delete characters and their inventories.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/a-piksi/dnd-inventory-manager
   ```
2. Navigate to the project directory:
   ```bash
   cd dnd-inventory-tracker
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program:
   ```bash
   python main.py
   ```

---

## Usage Instructions

### Starting the Program
Upon running, you'll be presented with the main menu:
1. **Items Library**
2. **Character Inventories**

### Items Library
- **Search Items**: Enter a keyword to search for items in the library.

### Character Inventories
- **Add a New Character**: Define character attributes (name, race, class, strength) and add items to their inventory.
- **Use Existing Character**: View or modify an existing character's inventory.
  - Add items from the library.
  - Change item quantities or remove items.
- **Delete a Character**: Permanently remove a character and their inventory.

---

## Key Functionalities

### Item Management
- Items can include weapons, armor, or general equipment.
- Each item has attributes like name, type, description, weight, rarity, and quantity.

### Inventory Management
- Dynamically calculates the total weight of items.
- Ensures carry capacity is not exceeded based on character strength.

### Data Persistence
- Saves character data and custom items locally for future sessions.

---

## Dependencies
- `requests`: For getting all the items from the API (If `characters.pkl` does not exist)
- `tabulate`: For displaying items in a table format.
- `pytest`: For testing functionality.
- `pytest-mock`: For mocking during tests.

---

## Testing
Run the tests using `pytest`:
```bash
pytest test
```