import unittest
from unittest.mock import MagicMock
from rpg.player import Player
from rpg.room import Room


class TestPlayer(unittest.TestCase):
    """
    Unit test class for testing the functionality of the Player class.
    """
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.room1 = MagicMock(spec=Room)
        self.room2 = MagicMock(spec=Room)
        self.room1.name = "Room 1"
        self.room2.name = "Room 2"
        self.room1.inspect.return_value = "This is Room 1."
        self.room2.inspect.return_value = "This is Room 2."

        self.player = Player(description="You", current_room=None,
                             health=100, max_health=100)
        self.player.move_to_room(self.room1)

    def test_initialization(self) -> None:
        """
        Test to check whether the initialization of the Player
        instance is done correctly.
        """
        self.assertEqual(self.player.description, "You")
        self.assertEqual(self.player.current_room, self.room1)
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.max_health, 100)
        self.assertFalse(self.player.in_fight)

    def test_move_to_room(self) -> None:
        """
        Test to check if the player is correctly moved to
        a new room and attributes are updated accordingly.
        """
        self.player.move_to_room(self.room2)
        self.assertEqual(self.player.current_room, self.room2)

    def test_check_room(self) -> None:
        """
        Test whether the player can inspect the current room
        and receive the correct description.
        """
        self.assertEqual(self.player.check_room(), "This is Room 1.")
        self.player.move_to_room(self.room2)
        self.assertEqual(self.player.check_room(), "This is Room 2.")

    def test_to_json(self) -> None:
        """
        Test to check whether the player's attributes are correctly
        serialized into JSON format.
        """
        # Mock the toJSON method of the room and test Player's toJSON
        self.room1.toJSON.return_value = {"name": "Room 1"}
        expected_output = {
            "description": "You",
            "current_room": {"name": "Room 1"},
            "health": 100,
            "max_health": 100,
            "weapon": None
        }
        self.assertEqual(self.player.toJSON(), expected_output)

    def test_from_json(self) -> None:
        """
        Test to check whether the player's attributes are correctly
        deserialized from JSON format.
        """
        self.room1 = MagicMock(spec=Room)
        self.player.move_to_room(self.room1)

        player_data = {
            "description": "You",
            "current_room": {"name": "Room 1"},
            "health": 90,
            "max_health": 100,
            "weapon": None
        }
        new_player = Player.fromJSON(player_data)
        self.assertEqual(new_player.description, "You")
        self.assertEqual(new_player.current_room, self.room1)
        self.assertEqual(new_player.health, 90)
        self.assertEqual(new_player.max_health, 100)
        self.assertEqual(new_player.weapon, None)


if __name__ == '_main_':
    unittest.main()
