import unittest
from unittest.mock import MagicMock, patch
from rpg.room import Room
from rpg.player import Player
from rpg.healer import Healer
from rpg.enemy import Enemy
from rpg.weapon import Weapon
from rpg.door import Door


class TestIntegration(unittest.TestCase):

    def setUp(self) -> None:
        """
        Integration test to check if the classes interact
        with eachother correctly.
        """
        # Mocking Player and Room
        self.mock_player = MagicMock(spec=Player)
        self.mock_player.health = 100
        self.mock_player.max_health = 100
        self.mock_player.in_fight = False
        self.mock_room_1 = MagicMock(spec=Room)
        self.mock_room_2 = MagicMock(spec=Room)
        self.mock_room_1 = Room("Mock Room 1")
        self.mock_room_2 = Room("Mock Room 2")
        self.mock_player.move_to_room = MagicMock(self.mock_room_1)
        # Creating Doors
        self.door_to_room_1 = Door("Mock Door", self.mock_room_1)
        self.door_to_room_2 = Door("Test Door", self.mock_room_2)
        # Creating Weapons
        self.basic_sword = Weapon(description="Basic Sword",
                                  success=80, damage=15)
        self.critical_sword = Weapon(description="Critical Sword",
                                     success=90, damage=30)

        # Creating NPCs (Enemy and Healer)
        self.enemy = Enemy(description="Mock Enemy", health=50,
                           damage=10, reward=self.critical_sword)
        self.healer = Healer(description="Mock Healer", heal_amount=25)
        # Adding the NPCs to mock room 2
        self.mock_room_2.add_npc(self.enemy)
        self.mock_room_2.add_npc(self.healer)

    def test_check_room(self) -> None:
        """
        Test to check whether the player gets moved to the first room.
        """
        self.assertEqual(self.mock_player.current_room, self.mock_room_1)

    def test_room_attributes(self) -> None:
        """
        Test to check whether all the attributes of the room
        moves apporiapetly.
        """
        self.assertEqual(len(self.mock_room_2.npc_list), 2)
        self.mock_player.move_to_room(self.mock_room_2)
        self.assertEqual(self.mock_player.check_room(), "This is Mock Room 2.")
        self.assertEqual(len(self.mock_room_2.doors), 1)

    def test_weapon_inspect(self) -> None:
        """
        Test to check if the weapons return the correct descriptions.
        """
        self.assertEqual(self.basic_sword.inspect(), "Basic Sword")
        self.assertEqual(self.critical_sword.inspect(), "Critical Sword")

    def test_door_interaction(self) -> None:
        """
        Test to check if the player can move through the doors correctly.
        """
        self.door_to_room_2.interact(self.mock_player)
        self.mock_player.move_to_room.assert_called_with(self.mock_room_2)
        self.door_to_room_1.interact(self.mock_player)
        self.mock_player.move_to_room.assert_called_with(self.mock_room_1)

    def test_healer_interaction(self) -> None:
        """
        Test to check if the healer interacts with the player correctly.
        """
        self.assertEqual(self.mock_player.health, 100)
        self.mock_player.health = 70
        self.healer.interact(self.mock_player)
        self.assertEqual(self.mock_player.health, 95)

    @patch('random.randint')
    def test_enemy_combat(self) -> None:
        """
        Test to see if the combat interact goes as it is intended.
        """
        self.assertEqual(self.mock_player.health, 100)
        self.assertFalse(self.mock_player.in_fight)
        self.enemy.interact(self.mock_player)
        self.assertTrue(self.mock_player.in_fight)
        # Critical hit = True
        mock_randint.return_value = 13
        self.enemy.attack(self.mock_player, self.enemy,
                          chosen_attack=self.basic_sword,
                          critical_hit=True)
        expected_damage = int(13 * 1.5)
        self.assertEqual(self.enemy.health, 50 - expected_damage)
        # Critical hit = False
        self.enemy.attack(self.mock_player, self.enemy, self.basic_sword,
                          critical_hit=False)
        self.enemy.health = 5
        mock_randint.return_value = 13
        self.enemy.killed(self.mock_player, self.enemy)
        self.mock_player.equip.assert_called_with(self.critical_sword)
        self.assertEqual(len(self.mock_room_2.npc_list), 1)


if __name__ == '__main__':
    unittest.main()
