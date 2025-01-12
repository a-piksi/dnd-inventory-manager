import sys
import pickle

import requests

class Utility:
    @staticmethod
    def menu_choice(choices: list, print_list=True) -> int | None:
        if print_list:
            for index, choice in enumerate(choices):
                print(f"[{index + 1}] {choice.upper()}")
        
        while True:
            number = Utility.get_non_negative_int("Choice: ")
            if number is None:
                return None
            if 0 < number <= len(choices):
                return number - 1
            else:
                print("Input must be a number in the list")
    
    @staticmethod
    def get_non_negative_int(message: str) -> int | None:
        while True:
            try:
                number = int(input(message))
            except KeyboardInterrupt:
                print()
                return None
            except ValueError:
                print("Input must be an integer")
            else:
                if number >= 0:
                    return number
                
                print("Input must be a non-negative integer")
    
    @staticmethod
    def get_response(url: str) -> dict:
        headers = {
        'Accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            sys.exit("Did not receive a response from the API")
    
    @staticmethod
    def from_file(file_name: str) -> list:
        with open(file_name, "rb") as file:
            loaded_items = pickle.load(file)
        
        return loaded_items
    
    @staticmethod
    def to_file(file_name: str, items: list):
        with open(file_name, "wb") as file:
            pickle.dump(items, file)
    
    @staticmethod
    def get_not_empty_str(message):
        while True:
            user_input = input(message).strip()

            if user_input:
                return user_input

            print("The input cannot be empty")
            