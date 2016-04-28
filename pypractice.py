from sys import exit
import time

def gold_room():
    print("the room is full of gold. How much do you want to take?")
    choice = input("How many pounds?: ").lower()
    try:
        choice = int(choice)
    except ValueError as e:
        print(str(e))
        print("invalid entry. try typing in a number.")
        time.sleep(3)
        gold_room()
    else:
        if choice < 50:
            dead("nice, you're not greedy, you win!")
        else:
            dead("you greedy bastard!")

def bear_room():
    print("there's a bear here!")
    print("the bear has a bunch of honey!")
    print("the fat bear is front of another door")
    print("how are you going to move the bear?")
    choice = input("(taunt bear, take honey, open door?: ").lower()
    bear = input("Do you think the bear moved?(yes/no): ").lower()

    if bear == "yes":
        bear_moved = True
    else:
        bear_moved = False

    if choice == "take honey":
        dead("the bear looks at you then slaps your face off")
    elif choice == "taunt bear" and bear_moved: #true and true makes the argument true
        dead("the bear has moved from the door. You can leave.")
    elif choice == "taunt bear" and not bear_moved: #true and false makes the arugment true
        dead("the bear gets angry and chews your leg off")
    elif choice == "open door":
        gold_room()
    else:
        print("Invalid Entry")
        time.sleep(3)
        bear_room()

def cthulhu_room():
    print("here you see the great evil cthulhu")
    print("he, it, whatever stares at you and you go insane")
    print("do you flee for your life or let it eat your head?")
    choice = input("flee or head?: ").lower()

    if choice == "flee":
        start()
    elif choice == "head":
        print("well that was tasty")
    else:
        print("invalid entry")
        time.sleep(3)
        cthulhu_room()

def dead(string):
    print(string, "good job!")
    exit(0)
# by stating a argument (place holder) inside the definition it allows this to be a template
# for other functions to use.

def start():
    print("you are in a dark room.")
    print("there is a door to your right and left")
    print("which one do you take?")
    choice = input("left or right?: ").lower()

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("invalid entry. lets try again")
        start()

start()
