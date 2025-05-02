import unittest
from unittest.mock import MagicMock
from rpg.npc import NPC
from rpg.weapon import Weapon


class TestNPC(unittest.TestCase):
    """
    Unit test class for testing the functionality of the NPC class.
    """
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.weapon = MagicMock(spec=Weapon)
        self.weapon.description = "Gun"

        self.npc_enemy = NPC(description="Test NPC 1", classification="Enemy",
                             health=50, max_health=50, damage=5,
                             heal_amount=25, reward=None)

        self.npc_healer = NPC(description="Test NPC 2",
                              classification="Healer",
                              heal_amount=20, active=True)

    def test_initialization(self) -> None:
        self.assertEqual(self.npc_enemy.description, "Test NPC 1")
        self.assertEqual(self.npc_enemy.classification, "Enemy")
        self.assertEqual(self.npc_enemy.health, 50)
        self.assertEqual(self.npc_enemy.max_health, 50)
        self.assertEqual(self.npc_enemy.damage, 5)
        self.assertEqual(self.npc_enemy.heal_amount, 25)
        self.assertEqual(self.npc_enemy.reward, None)

    def test_inspect(self) -> None:
        self.assertEqual(self.npc_enemy.inspect(), "Test NPC 1")
        self.assertEqual(self.npc_healer.inspect(), "Test NPC 2")

    def test_to_json_enemy(self) -> None:
        """
        Test to check whether the enemy's attributes are correctly
        serialized into JSON format.
        """
        expected_output = {
            "description": "Test NPC 1",
            "classification": "Enemy",
            "health": 50,
            "max_health": 50,
            "damage": 5,
            "reward": None
        }
        self.assertEqual(self.npc_enemy.toJSON(), expected_output)

    def test_to_json_healer(self) -> None:
        """
        Test to check whether the healer's attributes are correctly
        serialized into JSON format.
        """
        expected_output = {
            "description": "Test NPC 2",
            "classification": "Healer",
            "heal_amount": 20,
            "active": True
        }
        self.assertEqual(self.npc_healer.toJSON(), expected_output)

    def test_from_json_enemy(self) -> None:
        """
        Test to check whether the player's attributes are correctly
        deserialized from JSON format.
        """
        weapon_data = {"description": "Gun"}
        NPC.weapon_class = Weapon
        Weapon.fromJSON = MagicMock(return_value=self.weapon)

        enemy_data = {
            "description": "Monster",
            "classification": "Enemy",
            "health": 40,
            "max_health": 50,
            "damage": 10,
            "reward": weapon_data
        }
        new_enemy = NPC.fromJSON(enemy_data)
        self.assertEqual(new_enemy.description, "Monster")
        self.assertEqual(new_enemy.classification, "Enemy")
        self.assertEqual(new_enemy.health, 40)
        self.assertEqual(new_enemy.max_health, 50)
        self.assertEqual(new_enemy.damage, 10)
        self.assertEqual(new_enemy.reward, self.weapon)

    def test_from_json_healer(self) -> None:
        """
        Test to check whether the player's attributes are correctly
        deserialized from JSON format.
        """
        healer_data = {
            "description": "Professor",
            "classification": "Healer",
            "heal_amount": 25,
            "active": True
        }
        new_healer = NPC.fromJSON(healer_data)
        self.assertEqual(new_healer.description, "Professor")
        self.assertEqual(new_healer.classification, "Healer")
        self.assertEqual(new_healer.heal_amount, 25)
        self.assertTrue(new_healer.active)


if __name__ == '__main__':
    unittest.main()