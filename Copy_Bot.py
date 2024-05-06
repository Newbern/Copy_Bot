import pyautogui as pink
import mouse
import keyboard
import os
from time import sleep

# Creating text data to insert new Copy bot program into
with open("source.txt", "r") as file:
    source = file.read()

# Setup
cls = lambda: os.system("cls")
time = 0
sec = .3

# Waiting for input
input("Copy Bot \nTO QUIT PRESS 'esc'... \nPress 'Enter' to Start:")
cls()

# Getting name for the file
name = input("File Name:>>>")
cls()

# Setting up Mouse clicks and functions
Mouse_lst = []
click = lambda: Mouse_lst.append(((mouse.get_position()), 0, time))
right_click = lambda: Mouse_lst.append((mouse.get_position(), 2, time))
double_click = lambda: Mouse_lst.append((mouse.get_position(), 00, time))

# Recording when mouse button is pressed
mouse.on_click(click)
mouse.on_right_click(right_click)
mouse.on_double_click(double_click)

# Getting Keyboard pressing
# Uses a callback function use the 'KeyboardEvent' in our code to get back characters
# keys[0] = Keywords
# keys[1] = Time
keys = []


def getting_keys(args):
    # This will break the while loop
    if keyboard.is_pressed("esc"):
        global loop
        loop = False

        # Stop Recording Mouse and Keyboard
        mouse.unhook_all()
        keyboard.unhook_all()

    # Storing the key that was pressed
    elif args.event_type == keyboard.KEY_DOWN:

        if args.name == "space":
            args.name = " "
        elif args.name == "enter":
            args.name = "\n"
        elif args.name == "shift":
            args.name = ""

        global time
        keys.append((args.name, time))


# Every time a key is pressed this will run until the loop is broke
keyboard.hook(getting_keys)

# Recording
loop = True
while loop:
    # Counting
    time += 1
    print(time)
    Mouse_lst.append((pink.position(), None, time))
    sleep(sec)

# Inserts this line of code to fix the error
open(f"{name}.py", "w").write("Point = lambda x, y: (x, y)\n")

# Adding data to file to be run on file
with open(f"{name}.py", 'a') as file:
    # Fixing mouse x and y format
    file.write(f"Mouse_lst = {Mouse_lst}\n")
    file.write(f"keys = {keys}\n")
    file.write(source)
    file.close()
sleep(1)
cls()

# Input to run new file
cho = input("Run Program?\n[y/n]\n>>>")
if cho == "y":
    cls()
    # Running file
    os.system(f"python {name}.py")
