import unittest
from unittest.mock import MagicMock
from rpg.room import Room
from rpg.door import Door
from rpg.player import Player


class TestDoor(unittest.TestCase):
    """
    Unit test class for testing the functionality of the Door class.
    """
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.room1 = MagicMock(spec=Room)
        self.room2 = MagicMock(spec=Room)
        self.room1 = Room("Test room 1")
        self.room2 = Room("Test room 2")
        self.player = MagicMock(spec=Player)

        self.door = Door("Test door", self.room1)

    def test_initialization(self) -> None:
        """
        Test to check whether the initialization of the Door
        instance is done correctly.
        """
        self.assertEqual(self.door.description, "Test door")
        self.assertEqual(self.door.connected_room, self.room1)

    def test_interact(self) -> None:
        """
        Test to check whether the interaction between
        the Door and Player class goes correctly.
        """
        self.door.interact(self.player)
        self.player.move_to_room(self.room1)
        self.assertEqual(self.room1.inspect(),
                         "Test room 1 The room has 0 doors.")

    def test_to_json(self) -> None:
        """
        Test to check whether the Door's attributes are correctly
        serialized into JSON format.
        """
        expected_output = {
            "description": "Test door",
            "connected_room": {"description": "Test room 1",
                               "doors": [], "npc_list": [],
                               "goal": False}
        }
        self.assertEqual(self.door.toJSON(), expected_output)

    def test_from_json(self) -> None:
        """
        Test to check whether the Door's attributes are correctly
        serialized into JSON format.
        """
        Room.fromJSON = MagicMock(return_value=self.room1)
        door_data = {
            "description": "Test door",
            "connected_room": {"description": "Test room 1",
                               "doors": [], "npc_list": [],
                               "goal": False}
        }
        new_door = Door.fromJSON(door_data)
        self.assertEqual(new_door.description, "Test door")
        self.assertEqual(new_door.connected_room, self.room1)


if __name__ == 'main':
    unittest.main()
