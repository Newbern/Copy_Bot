# Copy Bot
## Modules
* pyautogui
* mouse
* keyboard
* os
* time

## Setup and Source page upload
```bash
# Creating text data to insert new Copy bot program into
with open("source.txt", "r") as file:
    source = file.read()

# Setup
cls = lambda: os.system("cls")
time = 0
sec = .3

# Getting name for the file
name = input("File Name:>>>")
cls()
```

Just loading in the source code page in as `source` for later and also naming the file to be created later.

## Mouse Setup
```bash
# Setting up Mouse clicks and functions
Mouse_lst = []
click = lambda: Mouse_lst.append(((mouse.get_position()), 0, time))
right_click = lambda: Mouse_lst.append((mouse.get_position(), 2, time))
double_click = lambda: Mouse_lst.append((mouse.get_position(), 00, time))

# Recording when mouse button is pressed
mouse.on_click(click)
mouse.on_right_click(right_click)
mouse.on_double_click(double_click)
```
so this mouse setup we create those lambda functions that will get the mouse position of x and y, and every time a mouse button is clicked it will record the position and the time when it was pressed.

## Keyboard Setup
```bash
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
```

so this and the mouse pretty much do the same thing it basically waits until a keyboard button is pressed, and then it
records it and individually places the character with the respected time it is pressed

## Countdown
```bash
# Recording
loop = True
while loop:
    # Counting
    time += 1
    print(time)
    Mouse_lst.append((pink.position(), None, time))
    sleep(sec)
```
all this does is print out every second and sleeps and adds the position of the mouse in the `Mouse_lst`.

## New file
```bash
# Inserts this line of code to fix the error
open(f"{name}.py", "w").write("Point = lambda x, y: (x, y)\n")
```
So this creates a new file and fix the error on the new page it places the position correctly, but it shows Point i solved
this by adding this function just returning the same values.
```bash
# Adding data to file to be run on file
with open(f"{name}.py", 'a') as file:
    # Fixing mouse x and y format
    file.write(f"Mouse_lst = {Mouse_lst}\n")
    file.write(f"keys = {keys}\n")
    file.write(source)
    file.close()
sleep(1)
cls()
```
next it will append the data list `Mouse_lst` & `keys` then of course it will then append the source from the data we collected earlier.

## Calling File
```bash
# Input to run new file
cho = input("Run Program?\n[y/n]\n>>>")
if cho == "y":
    cls()
    # Running file
    os.system(f"python {name}.py")
```
Then we ask for the input if they want to call this file I could have used `subprocess` but I was already using the `os` module

## Source code
```bash
import pyautogui as pink

# Playing Recording
for item in Mouse_lst:
    # Moving to position
    pink.moveTo(item[0])

    # Mouse Button being pressed
    if item[1] == 0:
        pink.click()

    elif item[1] == 00:
        pink.doubleClick()

    elif item[1] == 2:
        pink.rightClick()

```
last but not least we will talk about the source code and how it does everything in the right order.
First it every mouse movement will go in its place and click if that button was pressed.
```bash
# Going through the same time as the mouse position to see when to press a key
for key in keys:
    words = key[0]
    times = key[1]

    if item[2] == times:
        if words == "backspace":
            pink.press(words)
        else:
            pink.write(words)
```
as the mouse goes in the position and be pressed if it needs to it will then read the keys. and if the `Time` of the mouse Matches the `Time` a key was pressed it would then write that one character.
how it checks to see when to press it goes through the list of keys and will only do anything if the time is exact with the mouse time there times when the mouse has no action, but it will still use this time to make sure they are linked to each other 