from .npc import NPC
from .base_models import Attackable
from .weapon import Weapon
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player


class Enemy(NPC, Attackable):
    def __init__(self, description: str, classification: str = "Enemy",
                 health: int = 50, max_health: int = 50, damage: int = 5,
                 reward: "Weapon" = None) -> None:
        """
        Initializes Enemy class which inherits from NPC
        :param description: Enemy dname or description
        :param classification: String of the NPC type, Enemy or Healer
        :param health: Current amount of health points
        :param damage: Amount of dealt damage per attack
        """
        super().__init__(description=description,
                         classification=classification,
                         health=health, max_health=max_health,
                         damage=damage, reward=reward)

    def interact(self, player: "Player") -> None:
        """
        Player starts fight with Enemy
        :param player: Player class
        """
        player.in_fight = True
        print("\nStarting fight")

    def attack(self, player: "Player", enemy: "Enemy",
               chosen_attack: "Weapon", critical_hit: bool) -> None:
        """
        Enemy is being successfully being attacked by player.
        :param player: Player class
        :param enemy: Enemy class of enemy being attacked
        :param chosen_attack: Chosen attack of the player
        :return: amount of damage
        """
        min_damage = max(1, int(chosen_attack.damage * 0.8))
        max_damage = int(chosen_attack.damage * 1.2)
        damage = random.randint(min_damage, max_damage)
        if critical_hit is True:
            damage = int(damage * 1.5)
            print("Critical hit!")
        else:
            print("Missed timing.")
        self.health -= damage
        if self.health <= 0:
            self.killed(player, enemy)
        else:
            print(f"\nYou dealt {damage} damage"
                  f" to the {enemy.description}.")

    def killed(self, player: "Player", enemy: "Enemy") -> None:
        """
        Enemy is killed by the player
        :param player: Player class
        :param enemy: Enemy class
        """
        print(f"\nYou killed {enemy.description} with "
              f"{player.health}/{player.max_health} hp.")
        if enemy.reward is not None:
            print(f"\nYou found: {enemy.reward.description}")
            player.equip(enemy.reward)
        player.current_room._npc_list.remove(enemy)
