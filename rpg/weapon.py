from .base_models import Inspectable
from .base_models import JsonSerializable


class Weapon(Inspectable, JsonSerializable):
    def __init__(self, description: str, offensive: bool = True,
                 success: int = 100, damage: int = 20) -> None:
        """
        Initializes the Fight class
        :param description: name or description of the move
        :param offensive: Boolean if the move is offensive or not
        :param success: Integer representing the success percentage
        :param damage: Damage the weapon deals
        """
        self.description = description
        self.offensive = offensive
        self.success = success
        self.damage = damage

    @property
    def description(self) -> str:
        """
        Getter for description
        :return: string description of the weapon
        """
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """
        Setter for description
        :param value: string of the new description
        """
        self._description = value

    @property
    def offensive(self) -> bool:
        """
        Getter for offensive or not
        :return: boolean that indicates if the weapon is offensive
        """
        return self._offensive

    @offensive.setter
    def offensive(self, value: bool) -> None:
        """
        Setter for offensive or not
        :param value: boolean of the new offensive status
        """
        self._offensive = value

    @property
    def success(self) -> int:
        """
        Getter for success percentage
        :return: integer of success percentage
        """
        return self._success

    @success.setter
    def success(self, value: int) -> None:
        """
        Setter for success percentage
        :param value: integer of new success percentage
        """
        self._success = value

    @property
    def damage(self) -> int:
        """
        Getter for damage
        :return: Damage value
        """
        return self._damage

    @damage.setter
    def damage(self, value: int) -> None:
        """
        Setter for damage
        :param value: New damage value
        """
        self._damage = value

    def inspect(self) -> str:
        """
        When weapon is inspected, return its description
        :return: The description
        """
        return self.description

    def toJSON(self) -> dict:
        """
        Serializing the class, turning it into JSON format
        :return: dictionary in JSON format
        """
        return {"description": self.description,
                "offensive": self.offensive,
                "success": self.success,
                "damage": self.damage}

    def fromJSON(data: dict) -> "Weapon":
        """
        Deserializing from dictionary to python objects
        :param data: Dictionary off class attributes and values
        :return: Player class using all attributes stored in the dictionary
        """
        if data is None:
            return None
        else:
            return Weapon(description=data['description'],
                          offensive=data['offensive'],
                          success=data['success'],
                          damage=data['damage'])
