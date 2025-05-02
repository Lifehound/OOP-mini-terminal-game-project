from .player import Player
import json
import os


class Scanner:
    def read_int(self, value, option_list: list,
                 minus_one: bool = False) -> bool:
        """
        Validates and checks if user's input is one of the options
        :param value: User's input
        :param option_list: The current option list
        :param minus_one: Boolean if '-1' is an option
        :return: boolean if input is correct (True) or incorrect (False)
        """
        if minus_one is True:
            option_list.append(-1)
        try:
            value = int(value)
            if value not in option_list:
                print("That is not an option")
                return False
            return True
        except ValueError:
            print("Please input an integer number")
            return False


class Saver:
    def quicksave(self) -> None:
        """
        Creates savedgames folder if non existent and saves game in JSON format
        """
        print("\nTrying to save file...")
        if not os.path.exists("savedgames"):
            os.makedirs("savedgames")
        player_dict = self.player.toJSON()
        with open("savedgames/quicksave.json", "w") as json_file:
            json.dump(player_dict, json_file, indent=2)
            print("\nFile successfully saved!")

    def quickload(self) -> None:
        """
        Checks if there is a savedgames map with file in it
        Loads file from JSON to python class if file loading went successful
        """
        print("\nLoading file...")
        if not os.path.exists("savedgames"):
            print("\nThere are no saved games.")
        elif not os.path.exists("savedgames/quicksave.json"):
            print("\nFolder exists but has no saved games.")
        else:
            try:
                with open("savedgames/quicksave.json", "r") as file:
                    data = json.load(file)
                    self.player = Player.fromJSON(data)
                    print("\nGame successfully loaded!")
            except Exception:
                print("\nLoading failed. Please save again before loading.")
