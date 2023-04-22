import random


class SelectWeapon:
    @staticmethod
    def weapon_list():
        """here is our weapons"""

        weapons = {
            1: "Kinfe",
            2: "Pistol",
            3: "Uzi",
            4: "Ump",
            5: "Akm",
        }

        return weapons


class DoorKey:
    def __init__(self):
        self.rand_num = random.randint(1, 3)

    def get_door_key(self):
        """get the door key"""

        return self.rand_num
