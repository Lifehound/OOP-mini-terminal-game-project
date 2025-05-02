from .room import Room
from .weapon import Weapon
from .base_models import JsonSerializable
from .base_models import Attackable
from .enemy import Enemy
import random


class Player(JsonSerializable, Attackable):
    def __init__(self, description: str = "You", current_room: "Room" = None,
                 health: int = 100, max_health: int = 100,
                 weapon: "Weapon" = None) -> None:
        """
        Initializes the Player class
        :param description: Player's name or description
        :param current_room: Room class of the room the player is currently in
        :param health: Current amount of health points
        :param max_health: Maximum amount of health points
        :param damage: Amount of damage dealt per attack without multiplier
        """
        self._description = description
        self._current_room = current_room
        self._health = health
        self._max_health = max_health
        self._weapon = weapon
        self._in_fight = False

    @property
    def description(self) -> str:
        """Getter for description"""
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        """Setter for description"""
        self._description = new_description

    @property
    def current_room(self) -> "Room":
        """
        Getter for self._current_room
        :return: Room the player is currently in
        """
        return self._current_room

    @current_room.setter
    def current_room(self, new_room: "Room") -> None:
        """
        Setter for self._current_room
        :param new_room: New room the player is moving to
        """
        self._current_room = new_room

    @property
    def health(self) -> int:
        """Getter for health"""
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        """Setter for health"""
        self._health = min(new_health, self._max_health)

    @property
    def max_health(self) -> int:
        """Getter for max health"""
        return self._max_health

    @property
    def weapon(self) -> "Weapon":
        """Getter for weapon"""
        return self._weapon

    @weapon.setter
    def weapon(self, new_weapon: "Weapon") -> None:
        """Setter for weapon"""
        self._weapon = new_weapon

    @property
    def in_fight(self) -> bool:
        """Getter for in_fight"""
        return self._in_fight

    @in_fight.setter
    def in_fight(self, boolean: bool) -> None:
        self._in_fight = boolean

    def move_to_room(self, new_room: "Room") -> None:
        """
        Assigns the player's current room attribute to the new given room.
        :param new_room: Class of the new room the player moves to.
        """
        self.current_room = new_room

    def equip(self, new_weapon: "Weapon") -> None:
        self.weapon = new_weapon

    def attack(self, enemy: "Enemy", player: "Player",
               original_damage: int) -> str | None:
        """
        Enemy is being successfully being attacked by player.
        """
        min_damage = max(8, int(original_damage * 0.8))
        max_damage = int(original_damage * 1.2)
        new_damage = random.randint(min_damage, max_damage)
        player.health -= new_damage

        if self.health <= 0:
            self.killed(enemy, player)
            return "dead"
        else:
            print(f"\nThe {enemy.description} hit you"
                  f" and dealt {new_damage} damage.")
            return None

    def killed(self, enemy: "Enemy", player: "Player") -> None:
        print(f"\nThe {enemy.description} hit you. {player.description} died.")
        print("\nGAME OVER!\n")

    def check_room(self) -> str:
        """
        Checks the player's current room
        :return: returns the inspect method for the player's current room
        """
        return self.current_room.inspect()

    def toJSON(self) -> dict:
        """
        Serializing the class, turning it into JSON format
        :return: dictionary in JSON format
        """
        return {"description": self.description,
                "current_room": self.current_room.toJSON(),
                "health": self.health,
                "max_health": self.max_health,
                "weapon": self.weapon.toJSON()
                if self.weapon is not None else None}

    def fromJSON(data: dict) -> "Player":
        """
        Deserializing from JSON format to python objects
        :param data: JSON string that needs to be converted
        :return: Player class using all attributes stored in the JSON string
        """
        return Player(description=data['description'],
                      current_room=Room.fromJSON(data['current_room']),
                      health=data['health'],
                      max_health=data['max_health'],
                      weapon=Weapon.fromJSON(data['weapon']))
