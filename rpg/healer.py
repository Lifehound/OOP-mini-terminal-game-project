from .npc import NPC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player


class Healer(NPC):
    def __init__(self, description, classification: str = "Healer",
                 heal_amount: int = 30, active: bool = True) -> None:
        """
        Initializes the Healer class which inherits from NPC
        :param description: Name or description of the npc
        :param classification: String of the NPC type, Enemy or Healer
        :param heal_amount: Healer's amount of heal points per interaction
        """
        super().__init__(description=description,
                         classification=classification,
                         heal_amount=heal_amount, active=active)

    def interact(self, player: "Player") -> None:
        """
        Player's health is added by the Healer's heal amount
        :param: Player class
        """
        if self.active is True:
            player.health += self.heal_amount
            if player.health > player.max_health:
                player.health = player.max_health
            print(f"\n{self.description} healed you"
                  f" with {self.heal_amount} hp.")
            self.active = False
        else:
            print(f"You have already interacted with {self.description}, "
                  f"please try again later.")
