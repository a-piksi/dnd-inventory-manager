from utility import Utility
from program_manager import ProgramManager


def main():
    modes = ["Items library", "Character inventories"]

    while True:
        print("\nChoose the mode by inputing a number from the list.\nPress CTRL+C to exit the program.\n")
        index = Utility.menu_choice(modes)

        if index is None:
            print("\nExiting the program.")
            break

        match modes[index]:
            case "Items library":
                ProgramManager.library_mode()
            case "Character inventories":
                ProgramManager.character_mode()


if __name__ == "__main__":
    main()