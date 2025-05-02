from .base_models import Inspectable
from .base_models import Interactable
from .base_models import JsonSerializable
from .weapon import Weapon
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .enemy import Enemy
    from .healer import Healer


class NPC(Inspectable, Interactable, JsonSerializable):
    def __init__(self, description: str, classification: str = "Enemy",
                 health: int = 50, max_health: int = 50, damage: int = 5,
                 heal_amount: int = 30, reward: "Weapon" = None,
                 active: bool = True) -> None:
        """
        Initializes the NPC class
        :param description: Name or description of the NPC
        :param classification: String of the NPC type, Enemy or Healer
        :param health: NPC's health points
        :param max_health: NPC's maximum health points
        :param damage: NPC's amount of dealt damage per attack
        :param heal_amount: NPC's amount of heal points per interaction
        :param reward: Weapon class of reward for killing NPC
        :param active: Boolean if NPC is active or not
        """
        self._description = description
        self._classification = classification
        self._health = health
        self._max_health = max_health
        self._damage = damage
        self._heal_amount = heal_amount
        self._reward = reward
        self._active = active

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
        :param description: The new description
        """
        self._description = new_description

    @property
    def classification(self) -> str:
        """
        Getter for classification
        :return: The classification
        """
        return self._classification

    @classification.setter
    def classification(self, new_classification: str) -> None:
        """
        Setter for classification
        :param classification: New classification
        """
        self._classification = new_classification

    @property
    def health(self) -> int:
        """
        Getter for health
        :return: NPC's health
        """
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        """
        Setter for health
        :param health: New health
        """
        self._health = new_health

    @property
    def max_health(self) -> int:
        """
        Getter for max_health
        :return: The maximum health
        """
        return self._max_health

    @max_health.setter
    def max_health(self, new_max_health: int) -> None:
        """
        Setter for max_health
        :param max_health: The new maximum health
        """
        self._max_health = new_max_health

    @property
    def damage(self) -> int:
        """
        Getter for damage
        :return: Its damage
        """
        return self._damage

    @damage.setter
    def damage(self, new_damage: int) -> None:
        """
        Setter for damage
        :param damage: Its new damage
        """
        self._damage = new_damage

    @property
    def heal_amount(self) -> int:
        """
        Getter for heal_amount
        :return: heal_amount
        """
        return self._heal_amount

    @heal_amount.setter
    def heal_amount(self, new_heal_amount: int) -> None:
        """
        Setter for heal_amount
        :param heal_amount: New heal amount
        """
        self._heal_amount = new_heal_amount

    @property
    def reward(self) -> "Weapon":
        """
        Getter for reward
        :return: Weapon class of the reward
        """
        return self._reward

    @reward.setter
    def reward(self, new_reward: "Weapon") -> None:
        """
        Setter for reward
        :param reward: Weapon class of the new reward
        """
        self._reward = new_reward

    @property
    def active(self) -> bool:
        """
        Getter for active
        :param active: active
        :return: Boolean if NPC is active or not
        """
        return self._active

    @active.setter
    def active(self, new_active: bool) -> None:
        """
        Setter for active
        :param new_active: Boolean if NPC is now active or not
        """
        self._active = new_active

    def inspect(self) -> str:
        """
        Inspects the NPC
        :return: string of the npc's name / description
        """
        return self.description

    def toJSON(self) -> dict:
        """
        Serializing the class, turning it into JSON format
        :return: dictionary in JSON format
        """
        if self.classification == "Enemy":
            return {"description": self.description,
                    "classification": self.classification,
                    "health": self.health,
                    "max_health": self.max_health,
                    "damage": self.damage,
                    "reward": self.reward.toJSON()
                    if self.reward is not None else None}
        elif self.classification == "Healer":
            return {"description": self.description,
                    "classification": self.classification,
                    "heal_amount": self.heal_amount,
                    "active": self.active}

    def fromJSON(data: dict) -> Union["Enemy", "Healer"]:
        """
        Deserializing from JSON format to python objects
        :param data: JSON string that needs to be converted
        :return: Enemy or Healer class using all
        attributes stored in the JSON string
        """
        from .enemy import Enemy
        from .healer import Healer
        if data['classification'] == "Enemy":
            return Enemy(description=data['description'],
                         classification=data['classification'],
                         health=data['health'],
                         max_health=data['max_health'],
                         damage=data['damage'],
                         reward=Weapon.fromJSON(data['reward']))
        elif data['classification'] == "Healer":
            return Healer(description=data['description'],
                          classification=data['classification'],
                          heal_amount=data['heal_amount'],
                          active=data['active'])
