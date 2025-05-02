import unittest
from unittest.mock import MagicMock
from rpg.weapon import Weapon
from rpg.player import Player


class TestDoor(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.player = MagicMock(spec=Player)
        self.weapon = Weapon("Test weapon")

    def test_initialization(self) -> None:
        """
        Test to check whether the initialization of the Weapon
        instance is done correctly.
        """
        self.assertEqual(self.weapon.description, "Test weapon")
        self.assertTrue(self.weapon.offensive)
        self.assertEqual(self.weapon.success, 100)
        self.assertEqual(self.weapon.damage, 20)

    def test_inspect(self):
        """
        Test to check if inspect method indeed returns description
        """
        self.assertEqual(self.weapon.inspect(), "Test weapon")

    def test_to_json(self) -> None:
        """
        Test to check whether the weapon's attributes are correctly
        serialized into JSON format.
        """
        expected_output = {
            "description": "Test weapon",
            "offensive": True,
            "success": 100,
            "damage": 5
        }
        self.assertEqual(self.weapon.toJSON(), expected_output)

    def test_from_json(self) -> None:
        """
        Test to check whether the weapons's attributes are correctly
        deserialized from JSON format.
        """
        Weapon.fromJSON = MagicMock(return_value=self.weapon)
        weapon_data = {
            "description": "Test weapon",
            "offensive": True,
            "success": 100,
            "damage": 5
        }
        new_weapon = Weapon.fromJSON(weapon_data)
        self.assertEqual(new_weapon.description, "Test weapon")
        self.assertTrue(new_weapon.offensive)
        self.assertEqual(new_weapon.success, 100)
        self.assertEqual(new_weapon.damage, 5)


if __name__ == '__main__':
    unittest.main()
