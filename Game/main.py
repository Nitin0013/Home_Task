import random
from utils.answer import Questions
from utils.resource import SelectWeapon, DoorKey


Ques = Questions.task()
ques_lists = list(Ques.keys())


Sel_wep = SelectWeapon()
wep_list = Sel_wep.weapon_list()
enemy_weapon = random.randint(1, 5)


D_key = DoorKey()
door_key = D_key.get_door_key()


lives = 3

print("Welcome To the Game !!!")

while True:
    if lives > 0:
        print("Level 1")
        print("Please Give Coprrect Ans else You will Lose One Live")
        print(f"Total LIves Are {lives}")

        """ start the game we call qustions list if player loose then his live get reduce and if get correct ans then goes to next round """

        random_que = random.randint(0, 4)
        ask_ques = ques_lists[random_que]

        print(ask_ques)

        player_answer = input("Enter Correct Ans : ")

        if Ques[ask_ques] != player_answer.capitalize():
            print(f"Player Ans is {player_answer}")
            print("Please Try Again !!!")
            lives -= 1
        else:
            print("Success")
            print(wep_list)

            while True:
                try:
                    player_choice = int(input("Enter Select Weapon : "))
                    if player_choice >= 6 or player_choice <= 0:
                        print("Please Select val between (1-5)")
                        continue
                    print(f"Door Key is {door_key}")

                    while True:
                        pickup_key = int(input("Enter Key Num : "))
                        print(pickup_key)
                        if pickup_key >= 4 or pickup_key <= 0:
                            print("Please Select Val between (1-3)")
                            continue

                        if door_key != pickup_key:
                            print("Select Valid Key")
                            continue
                        else:
                            print("Succefully Unlock Door")
                            print("Successfully complted level 1")
                            print("Welcome to the level 2")
                            if lives < 3:
                                lives += 1
                                print(f"Total Lives are {lives}")

                        print("Fight With Boss")
                        print(f"enemy choose {enemy_weapon}")
                        while enemy_weapon != player_choice:
                            player_choice = int(input("Enter Weapon Choice : "))
                            print("PLease Select Same Weapon")
                        else:
                            print("Boss Defeat")
                            while True:
                                random_que = random.randint(0, 4)
                                ask_ques = ques_lists[random_que]
                                print(ask_ques)

                                player_answer = input("Enter Correct Ans : ")

                                if Ques[ask_ques] != player_answer.capitalize():
                                    print(f"Player Ans is {player_answer}")
                                    print("Please Try Again !!!")
                                    continue
                                else:
                                    print("Win Game")
                                    break
                        break
                except ValueError as v:
                    print(v)
                    print("Please Enter Integer Only")
                else:
                    break
            break
    else:
        print("You Lost Game Please Try Again")
        break
