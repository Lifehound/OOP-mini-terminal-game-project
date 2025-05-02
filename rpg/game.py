from .io_utils import Scanner, Saver
from .weapon import Weapon
import sys
import time
from .player import Player
from .enemy import Enemy
from typing import Union
import curses
import random


class Game(Saver):
    def start_game(self) -> str:
        """
        Starts the game, creates the game loop
        """
        # Create infinite loop
        while True:
            if self.player.current_room.goal is True:
                print("\nFinally the right tutorial room! "
                      "And you barely made it on time too! "
                      "Congratulations, now the real challenge of "
                      "learning can start!!"
                      "\n----- GAME COMPLETED -----\n")
                self.show_credits()
                return "end game"

            # Loop through possible options
            print("\nWhat do you want to do?")
            first_options = ["Look around", "Look for a way out",
                             "Look for company", "QuickSave",
                             "QuickLoad", "Restart Game or Quit"]
            choice_indices = self.give_options(first_options)
            inp_digit = input("> ")
            if Scanner.read_int(self, inp_digit, choice_indices) is False:
                continue

            # Use specific function for corresponding input
            match inp_digit:
                case "0":
                    self.look_around()
                case "1":
                    if self.look_for_a_way_out() == "goal reached":
                        break
                case "2":
                    if self.look_for_company() == "game over":
                        break
                case "3":
                    self.quicksave()
                case "4":
                    self.quickload()
                case "5":
                    return "end game"

    def give_options(self, options: list[str]) -> list[int]:
        """
        Loops over the options and prints them
        :param options: List of strings of options
        :return: List of integers of option indices
        """
        indices = []
        for index, option in enumerate(options):
            try:
                print(f"({index}): {option.inspect()}")
            except AttributeError:
                print(f"({index}) {option}")
            indices.append(index)
        return indices

    def look_around(self) -> None:
        """
        Checks the room the player is currently in
        """
        # Inspects the room the player is currently in.
        print(f"\nYou see: {self.player.check_room()}")

    def look_for_a_way_out(self) -> None:
        """
        Looks for doors, checks if room is blocked, lets the player interact
        """
        print("\nYou look around for doors.")

        # Check if room has doors
        if len(self.player.current_room.doors) < 1:
            print("\nThis room has no doors.")
            return None

        # Check if there is an Enemy in the current room, which blocks the door
        enemy_list = []
        for npc in self.player.current_room._npc_list:
            if npc._classification == "Enemy":
                enemy_list.append(npc)
        if len(enemy_list) > 0:
            print("\nThere is an enemy blocking the door.")
            print("You have to kill all enemies before you can enter doors.")
            return None

        # Give door options
        print("\nYou see:")
        choices_indices = self.give_options(self.player.current_room.doors)
        print("\nWhich door do you take? (-1 : stay here)")

        # Validate the input if its an option
        inp_digit = input("> ")
        validation = Scanner.read_int(self, inp_digit, choices_indices,
                                      minus_one=True)

        # Create loop until input is a valid option
        while validation is False:
            inp_digit = input("> ")
            validation = Scanner.read_int(self, inp_digit, choices_indices,
                                          minus_one=True)

        # Check if player wants to stay in current room
        if inp_digit == "-1":
            print(f"\nYou stay in: {self.player.current_room.inspect()}")
            return None

        # Move player to the new room
        chosen_door = self.player.current_room.doors[int(inp_digit)]
        chosen_door.interact(self.player)

    def look_for_company(self) -> None:
        """
        Looks for NPCs, starts fight if interacted with enemy
        """
        print("You look if there's someone here.")

        # Check if there are NPCs in the room
        if len(self.player.current_room._npc_list) < 1:
            print("\nThere is nothing to interact with in this room.")

        # If there are NPCs, loop over the them and print them as options
        else:
            npcs_indices = []
            print("\nYou see:")
            for index, npc in enumerate(self.player.current_room._npc_list):
                npcs_indices.append(index)
                print(f"({index}) {npc.inspect()}")
            print("\nInteract? (-1 : do nothing)")

            # Validate user input as one of the options.
            inp_digit = input("> ")
            validator = Scanner.read_int(self, inp_digit, npcs_indices,
                                         minus_one=True)

            # Create loop until input is a valid option
            while validator is False:
                inp_digit = input("> ")
                validator = Scanner.read_int(self, inp_digit, npcs_indices,
                                             minus_one=True)

            # If player does not want to interact, do nothing
            if inp_digit == "-1":
                pass

            # If NPC is chosen to interact with, start fight.
            else:
                npc = self.player.current_room._npc_list[int(inp_digit)]
                npc.interact(self.player)
                if self.player.in_fight is True:

                    # If player died, return game over
                    if self.start_fight(self.player, npc) == "died":
                        return "game over"
                    self.player.in_fight = False
                else:
                    self.show_healthbar(self.player)

    def start_fight(self, player: "Player", enemy: "Enemy") -> str | None:
        # Create infinite loop for letting the user only choose a valid option
        while True:

            # Create the fighter options as classes with attributes.
            fight_options = [Weapon("Fists", True, 100, 5),
                             Weapon("Run away", False)]
            if player.weapon is not None:
                fight_options.insert(0, player.weapon)
            option_indices = []
            # Print the attack options, loop over the created options
            print("\nWhat do you want to do? Attack options:")
            option_indices = self.give_options(fight_options)
            inp_digit = input("> ")

            # Validate user input, if no option, give options again, asks input
            if Scanner.read_int(self, inp_digit, option_indices) is not False:
                chosen_attack = fight_options[int(inp_digit)]

                # If its an offensive move, player attacks first
                if chosen_attack.offensive is True:

                    # Use success rate per attack, update enemy health
                    if random.randint(1, 100) <= int(chosen_attack.success):
                        critical_hit = False
                        if curses.wrapper(self.timing_mechanism) is True:
                            critical_hit = True
                        enemy.attack(player, enemy, chosen_attack,
                                     critical_hit)

                        # If enemy is dead, only show own healthbar
                        if enemy.health <= 0:
                            self.show_healthbar
                            break
                    else:
                        print(f"{chosen_attack.description} failed.")

                    # Enemy attacks player
                    if player.attack(enemy, player,
                                     enemy.damage) == "dead":
                        return "died"
                    self.show_healthbar(player)
                    self.show_healthbar(enemy)

                # Defensive move: enemy attacks and go back to first options
                else:
                    if player.attack(enemy, player, enemy.damage) == "dead":
                        return "died"
                    self.show_healthbar(player)
                    break
        return None

    def timing_mechanism(self, stdscr: curses.window) -> bool:
        """
        A timing mechanism where the user needs to press a key when indicator
        is in the middle.
        :param stdscr: Curses object to cover terminal
        :return: Boolean if it was perfect timing or not
        """
        # Hide cursor / make getch non-blocking / refresh every 10 milliseconds
        curses.curs_set(False)
        stdscr.nodelay(True)
        stdscr.timeout(10)

        # Initiate bar and indicator parameters
        width = 20
        indicator_pos = 0
        direction = 1

        # Define middle (perfect score) indices
        perfect_hit_start = 8
        perfect_hit_end = 10

        # Add instructions
        stdscr.clear()
        stdscr.addstr(1, 0, "Press any key when indicator is in the middle:")
        pressed = False

        # Create loop until user presses any key
        while not pressed:
            indicator_pos += direction

            # Create the bar
            bar = ["-"] * (width)
            bar[perfect_hit_start:perfect_hit_end + 1] = ["="] * (
                perfect_hit_end - perfect_hit_start + 1)
            bar[indicator_pos] = "|"

            # Print the bar
            stdscr.addstr(3, 0, "[" + "".join(bar) + "]")
            stdscr.refresh()

            # Move the indicator
            if indicator_pos == 0 or indicator_pos == width - 1:
                direction *= -1  # Change direction at the edges

            # Check for key press
            if stdscr.getch() != -1:
                pressed = True

                # Determine if it was a perfect hit and pause to show result
                if perfect_hit_start <= indicator_pos <= perfect_hit_end:
                    stdscr.addstr(5, 0, "Critical hit!")
                    stdscr.refresh()
                    time.sleep(2)
                    return True
                else:
                    stdscr.addstr(5, 0, "Missed timing!")
                    stdscr.refresh()
                    time.sleep(2)
                    return False

            # Sleep to control the indicator speed
            time.sleep(0.01)

    def show_healthbar(self, character: Union["Player", "Enemy"]) -> None:
        """
        Shows colored healthbar of the corresponding player or enemy.
        Healthbar is red below 50 hp otherwise red.
        :param character: Player or Enemy class
        """
        red_color = "\033[91m"
        green_color = "\033[92m"
        default_color = "\033[0m"
        remaining_bars = round(character.health / character.max_health * 20)
        lost_bars = 20 - remaining_bars
        print(f"\n{character.description}'s HP: "
              f"{character.health}/{character.max_health}")
        print(f"|"
              f"{red_color if remaining_bars < 10 else green_color}"
              f"{remaining_bars * "#"}"
              f"{lost_bars * "_"}"
              f"{default_color}"
              f"|")

    def title_screen(self) -> None:
        """
        Prints the title screen and makes it fancy by having a typing effect
        """
        line = "\n- Welcome to this RPG! -"\
               "\n\n This RPG will lead you"\
               "\n through the dungeon of"\
               "\n     the dangerous"\
               "\n  Nijenborgh building\n"
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        time.sleep(1)
  
    def show_credits(self) -> None:
        """
        Prints end screen / credits
        """
        time.sleep(3)
        line = "\n   Credits"\
               "\n\nPRODUCER"\
               "\nYannick & Emily"\
               "\n\nSCRIPT WRITER"\
               "\nYannick & Emily"\
               "\n\nGAME DESIGNER"\
               "\nYannick & Emily"\
               "\n\nGAME DEVELOPER"\
               "\nYannick & Emily"\
               "\n\nGAME DESIGNER"\
               "\nYannick & Emily"\
               "\n\nTHANKS TO:"\
               "\nDr. Marco Zullich"\
               "\nAleksandar Todorov"\
               "\nMohammad al Shakoush"\
               "\nChristian Kobriger"\
               "\nIustin Lungu"\
               "\nIvaylo Rusinov"\
               "\nMo Assaf"\
               "\nSebastian Pusch"\
               "\nTeun Boersma\n\n"

        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
