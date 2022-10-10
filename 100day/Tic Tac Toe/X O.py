import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


user = "X"
computer = "O"


def ckeck():
    result = all(element == user for element in game_list1)
    result1 = all(element == computer for element in game_list1)
    if result:
        print("You won!!")
        quit()
    else:
        pass
    if result1:
        print("You lost!!")
        quit()
    else:
        pass
    result3 = all(element == user for element in game_list2)
    result4 = all(element == computer for element in game_list2)
    if result3:
        print("You won!!")
        quit()
    else:
        pass
    if result4:
        print("You lost!!")
        quit()
    else:
        pass
    result5 = all(element == user for element in game_list3)
    result6 = all(element == computer for element in game_list3)
    if result5:
        print("You won!!")
        quit()
    else:
        pass
    if result6:
        print("You lost!!")
        quit()
    else:
        pass
    if game_list1[0] == game_list2[1] == game_list3[2] == "X" or game_list1[2] == game_list2[1] == game_list3[0] == "X":
        print("You won")
        quit()
    if game_list1[0] == game_list2[1] == game_list3[2] == "O" or game_list1[2] == game_list2[1] == game_list3[0] == "O":
        print("You Lost")
        quit()
    if game_list1[0] == game_list2[0] == game_list3[0] == "X" or game_list1[1] == game_list2[1] == game_list3[
        1] == "X" or game_list1[2] == game_list2[2] == game_list3[2] == "X":
        print("You won")
        quit()
    if game_list1[0] == game_list2[0] == game_list3[0] == "O" or game_list1[1] == game_list2[1] == game_list3[
        1] == "O" or game_list1[2] == game_list2[2] == game_list3[2] == "O":
        print("You lost")
        quit()


game_list1 = ["-", "-", "-"]
game_list2 = ["-", "-", "-"]
game_list3 = ["-", "-", "-"]
table = [game_list1, game_list2, game_list3]

print(f"{game_list1}\n{game_list2}\n{game_list3}")
print("Welcome to TicTacToe..")
x_o = "You're 'X' and computer is 'O'"


def game():
    while True:
        position = input("Enter the position")
        a = int(position[0])
        b = int(position[1])
        while table[a - 1][b - 1] != "-":
            print("Position is busy go again")
            position = input("Enter the position")
            a = int(position[0])
            b = int(position[1])
        if table[a - 1][b - 1] == "-":
            table[a - 1][b - 1] = user

        com_post1 = random.randint(0, 3)
        com_post2 = random.randint(0, 3)
        while table[com_post1 - 1][com_post2 - 1] != "-":
            com_post1 = random.randint(0, 3)
            com_post2 = random.randint(0, 3)
        if table[com_post1 - 1][com_post2 - 1] == "-":
            table[com_post1 - 1][com_post2 - 1] = computer

        print(f"{game_list1}\n{game_list2}\n{game_list3}")
        ckeck()

game()