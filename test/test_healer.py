import unittest
from unittest.mock import MagicMock
from rpg.healer import Healer
from rpg.player import Player


class TestHealer(unittest.TestCase):
    """
    Unit test class for testing the functionality of the Healer class.
    """
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.player = MagicMock(spec=Player)
        self.player.health = 30
        self.player.max_health = 100

        self.healer = Healer(description="Test healer", heal_amount=30)

    def test_initialization(self) -> None:
        """
        Test to check whether the initialization of the Healer
        instance is done correctly.
        """
        self.assertEqual(self.healer.description, "Test healer")
        # Testen of het de juiste class is?
        self.assertEqual(self.healer.heal_amount, 30)

    def test_interact_heal(self) -> None:
        """
        Test to check if the healer actually manages to change the health
        of the player the correct amount.
        """
        self.healer.interact(self.player)
        self.assertEqual(self.player.health, 60)

    def test_interact_heal_to_max(self) -> None:
        """
        Test to check if the healing amount of the healer does not make
        the player's health go above max_health
        """
        self.player.health = 90
        self.healer.interact(self.player)
        self.assertEqual(self.player.health, 100)

    def test_interact_heal_capped(self) -> None:
        """
        Test to check if the interaction does not change the player's health
        when it is at max_health.
        """
        self.player.health = 100
        self.healer.interact(self.player)
        self.assertEqual(self.player.health, 100)


if __name__ == '_main_':
    unittest.main()
