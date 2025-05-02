from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .player import Player
    from .enemy import Enemy
    from .door import Door
    from .room import Room
    from .healer import Healer
    from .weapon import Weapon


class Inspectable(ABC):
    @abstractmethod
    def inspect(self) -> str:
        """
        Base function for object being inspected
        """
        pass


class Interactable(ABC):
    @abstractmethod
    def interact(player: "Player") -> None:
        """
        Abstract method for player interacting with interactable object.
        :param player: Player class
        """
        pass


class Attackable(ABC):
    @abstractmethod
    def attack(self, attacker: Union["Player", "Enemy"],
               defender: Union["Player", "Enemy"]) -> None:
        """
        Abstract method for class to be attacked (Player or Enemy)
        :param attacker: Class of the attacker.
        :param defender: Class of the defender.
        """
        pass

    @abstractmethod
    def killed(self, attacker: Union["Player", "Enemy"],
               defender: Union["Player", "Enemy"]) -> None:
        """
        Abstract method for the attacker killing the defender.
        :param attacker: Class of the attacker.
        :param defender: Class of the defender.
        """
        pass


class JsonSerializable(ABC):
    @abstractmethod
    def toJSON(self) -> dict:
        """
        Abstract method of serializing data to JSON format.
        :return: Dictionary of class attributes.
        """
        pass

    @abstractmethod
    def fromJSON(data: dict) -> Union["Player", "Enemy", "Healer",
                                      "Room", "Door", "Weapon"]:
        """
        Abstract method for deserializing from JSON to class attributes.
        :param data: Dictionary of class attributes
        :return: Corresponding class this function is implemented in.
        """
        pass
