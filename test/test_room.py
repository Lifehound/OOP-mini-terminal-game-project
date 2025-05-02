import unittest
from unittest.mock import MagicMock
from rpg.room import Room
from rpg.door import Door
from rpg.npc import NPC
from rpg.enemy import Enemy
from rpg.healer import Healer
from rpg.weapon import Weapon


class TestRoom(unittest.TestCase):
    """
    Unit test class for testing the functionality of the Room class.
    """
    def setUp(self) -> None:
        """
        Set up method that is executed before each test.
        """
        self.door = MagicMock(spec=Door)
        self.npc = MagicMock(spec=NPC)
        self.enemy = MagicMock(spec=Enemy)
        self.healer = MagicMock(spec=Healer)
        self.weapon = MagicMock(spec=Weapon)

        self.room1 = Room("Test room")

    def test_initialization(self) -> None:
        """
        Test to check whether the initialization of the Room
        instance is done correctly.
        """
        self.assertEqual(self.room1.description, "Test room")
        self.assertEqual(len(self.room1.doors), 0)
        self.assertEqual(self.room1.npc_list, [])
        self.assertFalse(self.room1.goal)

    def test_add_door(self) -> None:
        """
        Test whether the add_door method actually adds a door correctly.
        """
        self.room1.add_door("Test door")
        self.assertEqual(len(self.room1.doors), 1)
        self.assertIsInstance(self.room1.doors[0], Door)

    def test_add_npc_enemy(self) -> None:
        """
        Test to check whether an enempy npc gets added to the room
        in the correct format.
        """
        self.room1.add_npc(name="Test enemy", classification="Enemy",
                           health=30, max_health=30, damage=10, reward=None)
        self.assertEqual(len(self.room1.npc_list), 1)
        self.assertIsInstance(self.room1.npc_list[-1], Enemy)
        self.assertEqual(self.room1.npc_list[-1].description, "Test enemy")

    def test_add_npc_healer(self) -> None:
        """
        Test to check whether an healer npc gets added to the room
        in the correct format.
        """
        self.room1.add_npc(name="Test healer", classification="Healer",
                           health=20,
                           max_health=20, damage=5, heal_amount=20,
                           reward=None)
        self.assertEqual(len(self.room1.npc_list), 1)
        self.assertIsInstance(self.room1.npc_list[-1], Healer)
        self.assertEqual(self.room1.npc_list[-1].description, "Test healer")

    def test_inspect(self) -> None:
        """
        Test to check whether the inspect method returns
        the correct information.
        """
        self.assertEqual(self.room1.inspect(),
                         "Test room The room has 0 doors")

    def test_to_json(self) -> None:
        """
        Test to check whether the room's attributes are correctly
        serialized into JSON format.
        """
        expected_output = {
            "description": "Test room",
            "doors": [],
            "goal": False,
            "npc_list": []
        }
        self.assertEqual(self.room1.toJSON(), expected_output)

    def test_from_json(self) -> None:
        """
        Test to check whether the room's attributes are correctly
        deserialized from JSON format.
        """
        Door.fromJSON = MagicMock(return_value=self.door)
        NPC.fromJSON = MagicMock(return_value=self.npc)

        room_data = {
            "description": "Test room",
            "doors": [{"description": "Test door 1"}],
            "npc_list": [{"name": "Friendly NPC"}],
            "goal": True
        }

        new_room = Room.fromJSON(room_data)
        self.assertEqual(new_room.description, "Test room")
        self.assertEqual(len(new_room.doors), 1)
        self.assertEqual(new_room.npc_list, [self.npc])
        self.assertTrue(new_room.goal)


if __name__ == '__main__':
    unittest.main()
