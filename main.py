# Lucas Weakland
# Group Bowser
# SCS 341 01
# Group Project 3

#imports
from PIL import Image
import sys
from random import randrange

# Initialize item box
randomNumber = randrange(20)

#Create player inventory
userInv = [0]

# open and "ready" our images / maps
img1 = Image.open('Map Images/DinoJungle.png')
img2 = Image.open('Map Images/ZestyZippers.png')
img3 = Image.open('Map Images/AncientAlgorithms.png')
img4 = Image.open('Map Images/MessnerMountains.png')

# intro (prints)
print("-*-*-*-Welcome to Analysis Kart!-*-*-*-")
print()
print("Let's have a look at our maps!")

# main
def main():
    menuMapView()
    menuMapSelect()

# user menu / start screen
def menuMapView():

    # user input for choice
    choice = input("""
Which map would you like to view?
A: Map view of Dino Jungle
B: Map view of Zesty Zippers
C: Map view of Ancient Algorithms
D: Map view of Messner Mountains
S: Skip map previews.
R: Continue to map selection.

Please enter your choice: """)

    # user choices
    if choice == "A" or choice == "a":
        print("Here is the map of Dino Jungle..")
        img1.show()
        menuMapView()
    elif choice == "B" or choice == "b":
        print("Here is the map of Zesty Zippers..")
        img2.show()
        menuMapView()
    elif choice == "C" or choice == "c":
        print("Here is the map of Ancient Algorithms..")
        img3.show()
        menuMapView()
    elif choice == "D" or choice == "d":
        print("Here is the map of Messner Mountains..")
        img4.show()
        menuMapView()
    elif choice == "S" or choice == "s":
        sys.exit
    elif choice == "R" or choice == "r":
        print()
    else:
        print("You must only select from A-D or S to Skip, or R to Continue.")
        print("Please try again")
        menuMapView()

# Play game by selecting map
def menuMapSelect():

    # user input for choice of map to play on
    choice1 = input("""
Alrighty! Which map would you like to play?
A: Play: Dino Jungle
B: Play: Zesty Zippers
C: Play: Ancient Algorithms
D: Play: Messner Mountains
Q: Never mind I don't wanna play...

Please enter your choice: """)

    # user choices
    if choice1 == "A" or choice1 == "a":
        print("Loading Dino Jungle...")
        dinoJungle(userInv)
    elif choice1 == "B" or choice1 == "b":
        print("Loading Zesty Zippers...")
        zestyZippers(userInv)
    elif choice1 == "C" or choice1 == "c":
        print("Loading Ancient Algorithms...")
        ancientAlgorithms(userInv)
    elif choice1 == "D" or choice1 == "d":
        print("Loading Messner Mountains...")
        messnerMountains(userInv)
    elif choice1 == "Q" or choice1 == "q":
        sys.exit
    else:
        print("You must only select from A-D or Q for Quit.")
        print("Please try again")
        menuMapView()



# Dino Jungle map
def dinoJungle(userInv):
    print("Welcome to Dino Jungle!")
    print("""Starting game in...
3...
2...
1...
Start!""")
    pickupItemDino(userInv)

        # shortcut code
def dinoJungleShortcut(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have",userInv,"Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #2
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut2
            dinoJungleShortcut2(userInv)
            print()
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC2
            dinoJungleNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC2(userInv)


# non shortcut code (SC - shortcut)
def dinoJungleNonSC(userInv):
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    #ask about shortcut #purple
    # shortcut #2
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut3
            print("You continue to go towards shortcut red")
            dinoJungleShortcut3(userInv)
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC3
            dinoJungleNonSC3(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC3(userInv)
# second shortcut
def dinoJungleShortcut2(userInv): # took the purple line shortcut
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    #shortcut 3
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut2
            print("You take shortcut 3")
            dinoJungleShortcut3(userInv)
            print()
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC2
            dinoJungleNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC2(userInv)

def dinoJungleNonSC2(userInv): # dont take purple shortcut
    print("You did not take the shortcut")
    print("*You continue driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
        # ask about Shortcut 3 (RED LINE on map)
        # shortcut 3
        if userInv >= [1]:
            print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
            choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
            if choiceDino == 'A' or choiceDino == 'a':
                # if choice A or a then load into the dinoJungleShortcut3
                print("You take shortcut 3")
                dinoJungleShortcut3(userInv)
                print()
            elif choiceDino == 'B' or choiceDino == 'b':
                print("You do not take the shortcut, which means you did not use your mushroom.")
                # load into dinojungleNonSC2
                dinoJungleNonSC3(userInv)
        else:
            print(
                "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
            dinoJungleNonSC3(userInv)

def dinoJungleShortcut3(userInv): # finished red shortcut, now can maybe take purple shortcut
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # ask about Shortcut 4 (PURPLE LINE on map)
    # shortcut 4
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut2
            dinoJungleShortcut4(userInv)
            print()
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC2
            dinoJungleNonSC3(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC3(userInv)


def dinoJungleNonSC3(userInv): # asks about green shortcut line / could be red as well tho
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # ask about shortcut green / red
    # shortcut #3
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut3
            print("You continue to go towards shortcut green")
            dinoJungleShortcut4(userInv)
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC3
            dinoJungleNonSC4(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC4(userInv)


def dinoJungleShortcut4(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    print()
    dinoJungleLoop()

def dinoJungleNonSC4(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # ask about Shortcut 3 (RED LINE on map)
    # shortcut 3
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut2
            dinoJungleShortcut4(userInv)
            print()
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC2
            dinoJungleNonSC5(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC5(userInv)


def dinoJungleNonSC5(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # ask about Shortcut (yellow LINE on map)
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut2
            dinoJungleShortcut4(userInv)
            print()
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into dinojungleNonSC2
            dinoJungleNonSC6(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC6(userInv)

def dinoJungleNonSC6(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # ask about Shortcut (purple LINE on map)
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut2
            dinoJungleShortcut4(userInv)
            print()
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            dinoJungleNonSC7(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC7(userInv)

def dinoJungleNonSC7(userInv):
    print("*You keep driving*")
    print()
    dinoJungleLoop()

def dinoJungleLoop():
    print("finished race")
    # NOTES FOR GROUP MEMBERS
    # here is gonna be the loop / laps. So say lap 1/3 completed and so on.
    # next part does not have to be here in this block of code, just simply stating it
    # can also add in the time, like +1 time for each shortcut not taken and -1 time for each shortcut taken

# PICKING UP FIRST ITEM BOX
def pickupItemDino(userInv):
    # user picks up item box
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv , "Mushroom(s)")
        shortcutCodeDino(userInv)
    else:
        print("You came across an item box! You got... Nothing")
        shortcutCodeDino(userInv)

def shortcutCodeDino(userInv):
    #Shortcut 1
    # if the users inventory contains 1 mushroom then ask if user wants to take shortcut, if they don't, then do not ask
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceDino = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceDino == 'A' or choiceDino == 'a':
            # if choice A or a then load into the dinoJungleShortcut
            dinoJungleShortcut(userInv)
        elif choiceDino == 'B' or choiceDino == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            dinoJungleNonSC(userInv)
    else:
        print("You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        dinoJungleNonSC(userInv)

# END OF DINO JUNGLE ^

# Zesty Zippers map
def zestyZippers(userInv):
    print("Welcome to Zesty Zippers!")
    print("""Starting game in...
3...
2...
1...
Start!""")
    pickupItemZesty(userInv)

        # shortcut code
def zestyZipShortcut(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have",userInv,"Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #2
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            zestyZipShortcut2(userInv)
            print()
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            zestyZipNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC2(userInv)


# non shortcut code (SC - shortcut)
def zestyZipNonSC(userInv):
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            # if choice A or a then load into the dinoJungleShortcut3
            print("You continue to go towards shortcut red")
            zestyZipShortcut3(userInv)
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            zestyZipNonSC3(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC3(userInv)
# second shortcut
def zestyZipShortcut2(userInv): # took the purple line shortcut
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    #shortcut 3
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            zestyZipShortcut3(userInv)
            print()
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            zestyZipNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC2(userInv)

def zestyZipNonSC2(userInv):
    print("You did not take the shortcut")
    print("*You continue driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
        if userInv >= [1]:
            print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
            choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
            if choiceZesty == 'A' or choiceZesty == 'a':
                # if choice A or a then load into the dinoJungleShortcut3
                zestyZipShortcut3(userInv)
                print()
            elif choiceZesty == 'B' or choiceZesty == 'b':
                print("You do not take the shortcut, which means you did not use your mushroom.")
                # load into dinojungleNonSC2
                zestyZipNonSC3(userInv)
        else:
            print(
                "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
            zestyZipNonSC3(userInv)

def zestyZipShortcut3(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    zestyZipShortcutFinal(userInv)

def zestyZipShortCut4(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            print("You take shortcut 3")
            zestyZipShortcutFinal(userInv)
            print()
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            zestyZipNonSC6(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC6(userInv)

def zestyZipNonSC3(userInv):
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")

    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            print("You continue to go towards shortcut green")
            zestyZipShortCut4(userInv)
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            zestyZipNonSC4(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC4(userInv)

def zestyZipShortcutFinal(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    zestyZipLoop()

def zestyZipNonSC4(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            zestyZipShortcutFinal(userInv)
            print()
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into zestyZipNonSC5
            zestyZipNonSC5(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC5(userInv)

def zestyZipNonSC5(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            # if choice A or a then load into the zestyZipShortcut2
            zestyZipShortcutFinal(userInv)
            print()
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            # load into zestyZipNonSC2
            zestyZipNonSC6(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC6(userInv)

def zestyZipNonSC6(userInv):
    print()
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    zestyZipLoop()

def zestyZipLoop():
    print("finished race")
    # NOTES FOR GROUP MEMBERS
    # here is gonna be the loop / laps. So say lap 1/3 completed and so on.
    # next part does not have to be here in this block of code, just simply stating it
    # can also add in the time, like +1 time for each shortcut not taken and -1 time for each shortcut taken

# PICKING UP FIRST ITEM BOX
def pickupItemZesty(userInv):
    # user picks up item box
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv , "Mushroom(s)")
        shortcutCodeZesty(userInv)
    else:
        print("You came across an item box! You got... Nothing")
        shortcutCodeZesty(userInv)

def shortcutCodeZesty(userInv):
    #Shortcut 1
    # if the users inventory contains 1 mushroom then ask if user wants to take shortcut, if they don't, then do not ask
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceZesty = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceZesty == 'A' or choiceZesty == 'a':
            # if choice A or a then load into the zestyZipShortcut
            zestyZipShortcut(userInv)
        elif choiceZesty == 'B' or choiceZesty == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            zestyZipNonSC(userInv)
    else:
        print("You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        zestyZipNonSC(userInv)

# END OF ZESTY ZIPPERS

# Ancient Algorithms map
def ancientAlgorithms(userInv):
    print("Welcome to Ancient Algorithms!")
    print("""Starting game in...
3...
2...
1...
Start!""")
    pickupItemAncient(userInv)

# shortcut code
def ancientShortcut(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # go back to picking up item box #2
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #2
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceANC = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceANC == 'A' or choiceANC == 'a':
            ancientShortcutFinal(userInv)
            print()
        elif choiceANC == 'B' or choiceANC == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            ancientNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        ancientNonSC2(userInv)

def ancientShortcutFinal(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    ancientLoop()

# non shortcut code (SC - shortcut)
def ancientNonSC(userInv):
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceANC = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceANC == 'A' or choiceANC == 'a':
            ancientShortcut2(userInv)
        elif choiceANC == 'B' or choiceANC == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            ancientNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        ancientNonSC2(userInv)

def ancientShortcut2(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    ancientLoop()


def ancientNonSC2(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceANC = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceANC == 'A' or choiceANC == 'a':
            ancientShortcutFinal(userInv)
            print()
        elif choiceANC == 'B' or choiceANC == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            ancientNonSC3(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        ancientNonSC3(userInv)

def ancientNonSC3(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    print("*You keep driving*")
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    print()
    print("*You keep driving*")
    ancientLoop()

def ancientLoop():
    print("finished race")
    # NOTES FOR GROUP MEMBERS
    # here is gonna be the loop / laps. So say lap 1/3 completed and so on.
    # next part does not have to be here in this block of code, just simply stating it
    # can also add in the time, like +1 time for each shortcut not taken and -1 time for each shortcut taken


# PICKING UP FIRST ITEM BOX
def pickupItemAncient(userInv):
    # user picks up item box
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
        shortcutCodeAncient(userInv)
    else:
        print("You came across an item box! You got... Nothing")
        shortcutCodeAncient(userInv)


def shortcutCodeAncient(userInv):
    # Shortcut 1
    # if the users inventory contains 1 mushroom then ask if user wants to take shortcut, if they don't, then do not ask
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceANC = input("""
A: Take the shortcut
B: Do not take the shortcut""")
        if choiceANC == 'A' or choiceANC == 'a':
            ancientShortcut(userInv)
        elif choiceANC == 'B' or choiceANC == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            ancientNonSC(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        ancientNonSC(userInv)

# END OF ANCIENT ALGORITHMS

# Messner Mountains map
def messnerMountains(userInv):
    print("Welcome to Messner Mountains!")
    print("""Starting game in...
3...
2...
1...
Start!""")
    pickupItemMessner(userInv)

# shortcut code
def messnerShortcut(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have",userInv,"Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #2
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (lime line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut2(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC2(userInv)

def messnerNonSC2(userInv):
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
        # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
        if userInv >= [1]:
            print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
            choiceMess = input("""
A: Take the shortcut (cyan line)
B: Do not take the shortcut""")
            if choiceMess == 'A' or choiceMess == 'a':
                messnerShortcut3(userInv)
                print()
            elif choiceMess == 'B' or choiceMess == 'b':
                print("You do not take the shortcut, which means you did not use your mushroom.")
                messnerNonSC3(userInv)
        else:
            print(
                "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
            messnerNonSC3(userInv)

def messnerNonSC3(userInv):
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #3
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (yellow line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut3(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC4(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC4(userInv)

def messnerNonSC4(userInv):
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (red line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut3(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC5(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC5(userInv)

def messnerNonSC5(userInv):
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (pink line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut3(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSCFinal(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSCFinal(userInv)

def messnerShortcut2(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have",userInv,"Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #3
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (yellow line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut3(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC4(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC4(userInv)

def messnerShortcut3(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # shortcut #4
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (pink line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcutFinal(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSCFinal(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSCFinal(userInv)

def messnerShortcutFinal(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    messnerLoop()

def messnerLoop():
    print("finished race")
    # NOTES FOR GROUP MEMBERS
    # here is gonna be the loop / laps. So say lap 1/3 completed and so on.
    # next part does not have to be here in this block of code, just simply stating it
    # can also add in the time, like +1 time for each shortcut not taken and -1 time for each shortcut taken

# non shortcut code (SC - shortcut)
def messnerNonSC(userInv):
    print("*You keep driving*")
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (dark blue line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            # if choice A or a then load into the dinoJungleShortcut3
            print("You continue to go towards shortcut red")
            messnerShortcut4(userInv)
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC6(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC6(userInv)

def messnerNonSC6(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    # shortcut #2
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (lime line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut2(userInv)
            print()
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC2(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC2(userInv)

def messnerShortcut4(userInv):
    print()
    print("You take the shortcut by using 1 Mushroom")
    # minus 1 to existing inventory for using shortcut
    for i in range(len(userInv)):
        userInv[i] -= 1
    print("You now have", userInv, "Mushroom(s)")
    print("*You keep driving*")
    # go back to picking up item box
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
        if userInv >= [1]:
            print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
            choiceMess = input("""
A: Take the shortcut (cyan line)
B: Do not take the shortcut""")
            if choiceMess == 'A' or choiceMess == 'a':
                messnerShortcut3(userInv)
            elif choiceMess == 'B' or choiceMess == 'b':
                print("You do not take the shortcut, which means you did not use your mushroom.")
                messnerNonSCFinal(userInv)
        else:
            print(
                "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
            messnerNonSCFinal(userInv)

def messnerNonSCFinal(userInv):
    randomNumber = randrange(20)
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
    else:
        print("You came across an item box! You got... Nothing")
    messnerLoop()


# PICKING UP FIRST ITEM BOX
def pickupItemMessner(userInv):
    # user picks up item box
    if randomNumber <= 9:
        print("You came across an item box! You got... A Mushroom!")
        # adds plus 1 to existing inventory
        for i in range(len(userInv)):
            userInv[i] += 1
        print("You have", userInv, "Mushroom(s)")
        shortcutCodeMessner(userInv)
    else:
        print("You came across an item box! You got... Nothing")
        shortcutCodeMessner(userInv)


def shortcutCodeMessner(userInv):
    # Shortcut 1
    # if the users inventory contains 1 mushroom then ask if user wants to take shortcut, if they don't, then do not ask
    if userInv >= [1]:
        print("You came across a shortcut, would you like to take it by using 1 Mushroom?")
        choiceMess = input("""
A: Take the shortcut (purple line)
B: Do not take the shortcut""")
        if choiceMess == 'A' or choiceMess == 'a':
            messnerShortcut(userInv)
        elif choiceMess == 'B' or choiceMess == 'b':
            print("You do not take the shortcut, which means you did not use your mushroom.")
            messnerNonSC(userInv)
    else:
        print(
            "You came across a shortcut! However, you do not have the efficient amount of mushrooms to take this shortcut...")
        messnerNonSC(userInv)

# initiate
main()