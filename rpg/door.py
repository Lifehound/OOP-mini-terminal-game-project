from .base_models import Inspectable
from .base_models import Interactable
from .base_models import JsonSerializable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player
    from .room import Room


class Door(Inspectable, Interactable, JsonSerializable):
    def __init__(self, description: str, connected_room: "Room") -> None:
        """
        Initializes the Door class with its description and connected room
        :param description: Door name or description
        :param connected_room: Room class of the room behind the door
        """
        self._description = description
        self._connected_room = connected_room

    @property
    def description(self) -> str:
        """
        Getter for description
        :return: The description
        """
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        """
        Setter for description
        :param new_description: New description
        """
        self._description = new_description

    @property
    def connected_room(self) -> "Room":
        """
        Getter for connected room
        :return: The connected room
        """
        return self._connected_room

    @connected_room.setter
    def connected_room(self, new_room: "Room") -> None:
        """
        Setter for connected room
        :param new_room: Room class of the new connected room
        """
        self._connected_room = new_room

    def inspect(self) -> str:
        """
        When door is inspected, return its description
        :return: The description
        """
        return self.description

    def interact(self, player: "Player") -> None:
        """
        When player interacts with door, it moves to the door's connected room
        :param player: Player class
        """
        player.move_to_room(self.connected_room)

    def toJSON(self) -> dict:
        """
        Serializing class into a dictionary
        :return: dictionary of class attributes
        """
        return {"description": self.description,
                "connected_room": self.connected_room.toJSON()}

    def fromJSON(data: dict) -> "Door":
        """
        Deserializing from dictionary to python objects
        :param data: Dictionary with class attributes
        :return: Door class using all attributes stored in the dictionary
        """
        from .room import Room
        return Door(description=data['description'],
                    connected_room=Room.fromJSON(data['connected_room']))
