from .base_models import Inspectable
from .door import Door
from .npc import NPC
from .enemy import Enemy
from .healer import Healer
from .weapon import Weapon
from copy import deepcopy


class Room(Inspectable):
    def __init__(self, description: str,
                 doors: list["Door"] = None,
                 npc_list: list["NPC"] = None, goal: bool = False) -> None:
        """
        Initializer of the room
        :param description: Room description
        :param doors: List of Door classes
        :param npc_list: List of NPC classes
        :param goal: Boolean if room is the goal room or not
        """
        self._description = description
        self._doors = doors if doors is not None else []
        self._npc_list = npc_list if npc_list is not None else []
        self._goal = goal

    @property
    def description(self) -> str:
        """
        Getter for description
        :return: Room description
        """
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        """
        Setter for description
        :param new_description: New room description
        """
        self._description = new_description

    @property
    def doors(self) -> list["Door"]:
        """
        Getter for door list
        :return: deepcopy of door list to avoid external mutation
        """
        return deepcopy(self._doors)

    @doors.setter
    def doors(self, door_list: list["Door"]) -> None:
        """
        Setter for door list
        :param door_list: New list of Door classes
        """
        self._doors = door_list

    @property
    def npc_list(self) -> list["NPC"]:
        """
        Getter for npc list
        :return: deepcopy of npc_list to avoid external mutation
        """
        return deepcopy(self._npc_list)

    @npc_list.setter
    def npc_list(self, new_list: list["NPC"]) -> None:
        """
        Setter for npc list
        :param new_list: New list of NPC classes
        """
        self._npc_list = new_list

    @property
    def goal(self) -> bool:
        """
        Getter for goal
        :return: Boolean if the room is the goal room
        """
        return self._goal

    @goal.setter
    def goal(self, new_goal: bool) -> None:
        """
        Setter for goal
        :param new_goal: Boolean if the room is the goal room or not
        """
        self._goal = new_goal

    def inspect(self) -> str:
        """
        Inspects player's current room, prints the description and door amount
        :return: String with room description and amount of doors
        """
        return (f"{self.description} The room has {len(self.doors)}" +
                f" {'door' if len(self.doors) == 1 else 'doors'}.")

    def add_door(self, door: str, connected_room: "Room" = None) -> None:
        """
        Adds door class to the door list of this room
        :param door: String with description of the door
        :param connected_room: Room class which is behind the door
        """
        self._doors.append(Door(door, connected_room))

    def add_npc(self, name: str, classification: str = "Enemy",
                health: int = 50, max_health: int = 50, damage: int = 5,
                heal_amount: int = 30, reward: "Weapon" = None) -> None:
        """
        Adds Enemy or Healer class to the room's npc list
        :param name: Name or description of the npc
        :param classification: String of the NPC type, Enemy or Healer
        :param health: Enemy's health points
        :param damage: Enemy's amount of dealt damage per attack
        :param heal_amount: Healer's amount of heal points per interaction
        """
        if classification == "Enemy":
            self._npc_list.append(Enemy(name, classification, health,
                                        max_health, damage, reward))
        else:
            self._npc_list.append(Healer(name, heal_amount=heal_amount))

    def toJSON(self) -> dict:
        """
        Serializing the class, turning it into JSON format
        :return: dictionary in JSON format
        """
        return {"description": self.description,
                "doors": [door.toJSON() for door in self.doors],
                "npc_list": [npc.toJSON() for npc in self.npc_list],
                "goal": self.goal}

    def fromJSON(data: dict) -> "Room":
        """
        Deserializing from JSON format to python objects
        :param data: JSON string that needs to be converted
        :return: Room class using all attributes stored in the JSON string
        """
        return Room(description=data['description'],
                    doors=[Door.fromJSON(door_data)
                           for door_data in data['doors']],
                    npc_list=[NPC.fromJSON(npc_data)
                              for npc_data in data['npc_list']],
                    goal=data['goal'])
