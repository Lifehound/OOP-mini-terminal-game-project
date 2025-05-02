import unittest
from unittest.mock import MagicMock, patch
from rpg.enemy import Enemy
from rpg.weapon import Weapon
from rpg.player import Player


class TestEnemy(unittest.TestCase):
    """
    Unit test class for testing the functionality of the Enemy class.
    """
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.player = MagicMock(spec=Player)
        self.player.weapon = None
        self.player.health = 100
        self.player.in_fight = False

        self.weapon = MagicMock(spec=Weapon)
        self.weapon.description = "Stick"
        self.weapon.damage = 10

        self.enemy = Enemy("Test enemy", health=50, reward=self.weapon)

    def test_initialization(self) -> None:
        """
        Test to check whether the initialization of the Healer
        instance is done correctly.
        """
        self.assertEqual(self.enemy.description, "Test enemy")
        self.assertEqual(self.enemy.classification, "Enemy")
        self.assertEqual(self.enemy.health, 50)
        self.assertEqual(self.enemy.max_health, 50)
        self.assertEqual(self.enemy.damage, 5)
        self.assertEqual(self.enemy.reward, self.weapon)

    def test_interact(self) -> None:
        """
        Test to check if player is set to fight after interacting with enemy
        """
        self.enemy.interact(self.player)
        self.assertTrue(self.player.in_fight)

    @patch('random.randint')
    def test_attack_normal(self, mock_randint) -> None:
        """
        Test to check if the enemy takes correct damage on a normal attack
        """
        chosen_attack = self.weapon
        mock_randint.return_value = 8
        self.enemy.attack(self.player, self.enemy,
                          chosen_attack, critical_hit=False)
        self.assertEqual(self.enemy.health, 50 - 8)

    @patch('random.randint')
    def test_attack_critical_hit(self, mock_randint) -> None:
        """
        Test to check if the enemy takes correct damage on a critical hit
        """
        chosen_attack = self.weapon
        mock_randint.return_value = 12
        self.enemy.attack(self.player, self.enemy,
                          chosen_attack, critical_hit=True)
        total_damage = int(12 * 1.5)
        self.assertEqual(self.enemy.health, 50 - total_damage)

    def test_killed_equip_weapon(self) -> None:
        """
        Test to check if the player eqiops the reward of the enemy
        """
        self.player.equip = MagicMock()
        self.enemy.killed(self.player, self.enemy)
        self.player.equip.assert_called_once_with(self.weapon)

    def test_killed_remove_from_room(self):
        """
        Test to check if the enemy is removed from npc list after dying
        """
        self.player.current_room._npc_list = [self.enemy]
        self.enemy.killed(self.player, self.enemy)
        self.assertNotIn(self.enemy, self.player.current_room._npc_list)


if __name__ == '__main__':
    unittest.main()
