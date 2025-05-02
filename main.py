from rpg.room import Room
from rpg.player import Player
from rpg.game import Game
from rpg.weapon import Weapon


class Initializer(Game):
    def __init__(self) -> None:
        """
        Initializes the Player, Rooms, Doors and NPCs
        """
        self.broom = Weapon("Clunky broom", True, 100, 30)
        self._initialize_rooms()
        self._initialize_doors()
        self._initialize_npcs()
        self.player = Player("Tim")
        self.player.move_to_room(self.lecture_hall)

    def initialize_player(self, name) -> None:
        """
        Initializes player and sets it to starting room.
        """
        self.player = Player(name)
        self.player.move_to_room(self.lecture_hall)

    def _initialize_rooms(self) -> None:
        """
        Initializes all rooms.
        """
        # First stage
        self.lecture_hall = Room("The lecture hall of Nijenborg.")
        self.first_floor = Room("The first floor of Nijenborg,"
                                " there appears to be classrooms "
                                "and an office.")
        self.cs_room = Room("A seemingly empty laboratory, "
                            "it doesn't look like the right place.")
        self.office = Room("This appears to be the office of a professor. "
                           "\nMaybe you can try and find him and ask "
                           "for directions to the right classroom.")
        self.empty_tutorial = Room("It looks to be a normal classroom. "
                                   "\nUnfortunately not the right classroom "
                                   "for the tutorial.")
        self.cs_room2 = Room("A seemingly empty laboratory, "
                             "it doesn't look like the right place.")
        self.office2 = Room("This appears to be the office of a professor. "
                            "\nMaybe you can try and find him and ask "
                            "for directions to the right classroom.")
        self.empty_tutorial2 = Room("It looks to be a normal classroom. "
                                    "\nUnfortunately not the right classroom "
                                    "for the tutorial.")
        self.cs_room3 = Room("A seemingly empty laboratory, "
                             "it doesn't look like the right place.")
        self.office3 = Room("This appears to be the office of a professor. "
                            "\nMaybe you can try and find him and ask "
                            "for directions to the right classroom.")
        self.empty_tutorial3 = Room("It looks to be a normal classroom. "
                                    "\nUnfortunately not the right classroom "
                                    "for the tutorial.")
        self.cs_room4 = Room("A seemingly empty laboratory, "
                             "it doesn't look like the right place.")
        self.office4 = Room("This appears to be the office of a professor. "
                            "\nMaybe you can try and find him and ask "
                            "for directions to the right classroom.")
        self.empty_tutorial4 = Room("It looks to be a normal classroom. "
                                    "\nUnfortunately not the right classroom "
                                    "for the tutorial.")
        # Second stage
        self.new_building = Room("You moved to a new building starting "
                                 "with 511_.___ "
                                 "\nIt appears to be just as big of a maze "
                                 "as the last one. "
                                 "\nYet you feel like you are slightly "
                                 "closer to your destination.")
        self.maze_room = Room("A room that feels exactly the same "
                              "as every other room. "
                              "\nYou feel like you are going "
                              "round in circles. "
                              "\nWill you ever actually reach the tutorial?")
        self.asbestos_room = Room("A room that appears to be very aged "
                                  "and decaying because of it. "
                                  "\nThe air is very heavy and makes "
                                  "it difficult to breathe.")
        self.maze_room2 = Room("A room that feels exactly the same "
                               "as every other room. "
                               "\nYou feel like you are going "
                               "round in circles. "
                               "\nWill you ever actually reach the tutorial?")
        self.asbestos_room2 = Room("A room that appears to be very aged "
                                   "and decaying because of it. "
                                   "\nThe air is very heavy and makes "
                                   "it difficult to breathe.")
        # Third stage
        self.final_hallway = Room("A hallway that looks very familair. "
                                  "\nThe classrooms appear to actually "
                                  "be filled "
                                  "with teaching assistants and students.")
        self.wrong_room1 = Room("That this is not the right tutorial. "
                                "\nWalking into a class filled with strangers "
                                "staring straight at you sure makes it more "
                                "uncomfortable.")
        self.wrong_room2 = Room("That this is not the right tutorial. "
                                "\nWalking into a class filled with strangers "
                                "staring straight at you sure makes it more "
                                "uncomfortable.")
        self.wrong_room3 = Room("That once more this is not "
                                "the right tutorial classroom. "
                                "\nWalking once more into the wrong classroom,"
                                " with this time even presentations going on, "
                                "makes you feel a whole new "
                                "level of discomfort.")
        self.right_room = Room("Finally the right tutorial! "
                               "\nAnd you barely made it on time to! "
                               "\nCongratulations, now the real challenge of "
                               "learning can start.")
        # Set goal room
        self.right_room.goal = True

    def _initialize_doors(self) -> None:
        """
        Initializes all doors.
        """
        # First stage
        self.lecture_hall.add_door("Big stairs, maybe they lead to where "
                                   "you have to be.", self.first_floor)
        self.first_floor.add_door("A door leading to "
                                  "a room numbered 511_.0140", self.cs_room)
        self.first_floor.add_door("A door leading to "
                                  "a room numbered 511_.0144", self.office)
        self.first_floor.add_door("A door leading to "
                                  "a room numbered 511_.0139",
                                  self.empty_tutorial)
        self.cs_room.add_door("A door leading to "
                              "a room numbered 511_.0144", self.office2)
        self.cs_room.add_door("A door leading to "
                              "a room numbered 511_.0139",
                              self.empty_tutorial2)
        self.office.add_door("A door leading to "
                             "a room numbered 511_.0140", self.cs_room3)
        self.office.add_door("A door leading to "
                             "a room numbered 511_.0139", self.empty_tutorial3)
        self.empty_tutorial.add_door("A door leading to "
                                     "a room numbered 511_.0144", self.office3)
        self.empty_tutorial.add_door("A door leading to "
                                     "a room numbered 511_.0140",
                                     self.cs_room2)
        self.cs_room3.add_door("A door leading to "
                               "a room numbered 511_.0139",
                               self.empty_tutorial4)
        self.cs_room2.add_door("A door leading to "
                               "a room numbered 511_.0144",
                               self.office4)
        self.office2.add_door("A door leading to "
                              "a room numbered 511_.0139",
                              self.empty_tutorial4)
        self.office3.add_door("A door leading to "
                              "a room numbered 511_.0140", self.cs_room4)
        self.empty_tutorial3.add_door("A door leading to "
                                      "a room numbered 511_.0140",
                                      self.cs_room4)
        self.empty_tutorial2.add_door("A door leading to "
                                      "a room numbered 511_.0144",
                                      self.office4)
        self.cs_room4.add_door("A door leading to "
                               "what seems to be a new building.",
                               self.new_building)
        self.office4.add_door("A door leading to "
                              "what seems to be a new building.",
                              self.new_building)
        self.empty_tutorial4.add_door("A door leading to "
                                      "what seems to be a new building.",
                                      self.new_building)
        # Second stage
        self.new_building.add_door("A door leading to "
                                   "a room numbered 511_.0103", self.maze_room)
        self.new_building.add_door("A door leading to "
                                   "a room numbered 511_.0113",
                                   self.asbestos_room)
        self.maze_room.add_door("A door leading to "
                                "a room numbered 511_.0113",
                                self.asbestos_room2)
        self.asbestos_room.add_door("A door leading to "
                                    "a room numbered 511_.0103",
                                    self.maze_room2)
        self.asbestos_room2.add_door("A door leading to "
                                     "a new hallway. "
                                     "\nyou feel like you are getting close.",
                                     self.final_hallway)
        self.maze_room2.add_door("A door leading to "
                                 "a new hallway. "
                                 "\nYou feel like you are getting close.",
                                 self.final_hallway)
        # Third stage
        self.final_hallway.add_door("A door leading to "
                                    "a room numbered 511_.0116",
                                    self.wrong_room1)
        self.final_hallway.add_door("A door leading to "
                                    "a room numbered 511_.0118",
                                    self.wrong_room2)
        self.final_hallway.add_door("A door leading to "
                                    "a room numbered 511_.0122",
                                    self.right_room)
        self.wrong_room1.add_door("A door leading to "
                                  "a room numbered 511_.0118",
                                  self.wrong_room3)
        self.wrong_room1.add_door("A door leading to "
                                  "a room numbered 511_.0122",
                                  self.right_room)
        self.wrong_room2.add_door("A door leading to "
                                  "a room numbered 511_.0116",
                                  self.wrong_room3)
        self.wrong_room2.add_door("A door leading to "
                                  "a room numbered 511_.0122",
                                  self.right_room)
        self.wrong_room3.add_door("A door leading to "
                                  "a room numbered 511_.0122",
                                  self.right_room)

    def _initialize_npcs(self) -> None:
        """
        Initializes all NPCs.
        """
        # Enemies
        # Chemical spill
        self.cs_room.add_npc("A weird blob of what seems to be chemical spill",
                             classification="Enemy",
                             health=50, damage=10, reward=self.broom)
        self.cs_room2.add_npc("A weird blob of what seems to be "
                              "chemical spill",
                              classification="Enemy",
                              health=50, damage=10, reward=self.broom)
        self.cs_room3.add_npc("A weird blob of what seems to be "
                              "chemical spill",
                              classification="Enemy",
                              health=50, damage=10, reward=self.broom)
        self.cs_room4.add_npc("A weird blob of what seems to be "
                              "chemical spill",
                              classification="Enemy",
                              health=50, damage=10, reward=self.broom)
        # Asbestos monster
        self.asbestos_room.add_npc("A hostile creature seemingly composed "
                                   "out of asbestos",
                                   classification="Enemy",
                                   health=50, damage=10)
        self.asbestos_room2.add_npc("A hostile creature seemingly composed "
                                    "out of asbestos",
                                    classification="Enemy",
                                    health=50, damage=10)
        # Maze monster
        self.maze_room.add_npc("A monster that appears to be made "
                               "out of furniture",
                               classification="Enemy",
                               health=50, damage=10)
        self. maze_room2.add_npc("A monster that appears to be made "
                                 "out of furniture",
                                 classification="Enemy",
                                 health=50, damage=10)
        # Healing
        # office
        self.office.add_npc("Professor Dr. Marco Zullich",
                            classification="Healer",
                            health=50, heal_amount=10)
        self.office2.add_npc("Professor Dr. Marco Zullich",
                             classification="Healer",
                             health=50, heal_amount=10)
        self.office3.add_npc("Professor Dr. Marco Zullich",
                             classification="Healer",
                             health=50, heal_amount=10)
        self.office4.add_npc("Professor Dr. Marco Zullich",
                             classification="Healer",
                             health=50, heal_amount=10)
        # final hallway
        self.final_hallway.add_npc("The vending machine "
                                   "filled with delicious goods.",
                                   classification="Healer",
                                   health=50, heal_amount=30)


class Main:
    def run_game(self) -> None:
        """
        Creates some of the statements that the user sees.
        """
        while True:
            print("Please enter your player name")
            player_name = input("> ")
            while len(player_name) > 20:
                print("Player name can have at most 20 characters")
                player_name = input("> ")
            game = Initializer()
            game.initialize_player(player_name)
            result = game.start_game()
            if result == "end game":
                print("Want to play again? Yes / No:")
                choice = input("> ").lower()
                while choice not in ["yes", "no"]:
                    print("\nPlease enter 'Yes' or 'No':")
                    choice = input("> ").lower()
                match choice:
                    case "yes":
                        print("\nYou chose to play again.")
                        continue
                    case "no":
                        print("\nYou chose not to play again.")
                        break


if __name__ == "__main__":
    Main.run_game()
