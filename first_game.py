import random 
import time
from data import *
from helpers import *

name = input("введи своё имя путник.")
player["name"] = name
current_enemy = 0

while True:
    action = input("веберите действие: \n1 - атака\n2 - тренировка\n3 - инфо об игроке\n4 - инфо о текущем противнике\n5 - инвентарь\n6 - магазин\n7 - иди работай бездарь ")
    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == len(enemies):
            print("вы всех победили!!!")
            break
    elif action == "2":
        training()
        print()
    elif action == "3":
        display_player()
        print()
    elif action == "4":
        display_enemy(current_enemy)      
        print() 
    elif action == "5":
        display_inventory()
        print()
    elif action == "6":
        shop()
        print()
    elif action == "7":
        earn()
        print()
    print()



