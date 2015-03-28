# File:        hw6.py
# Written by:  Kyle Fritz
# Date:        10/23/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: This program creates a gameboard and you have to try to reach 
#     the key
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


# Greets the user.
def printgreeting():
    print("Welcome to the Navigation Game!")

# input: Where the player and the key are
# output: Tell the user that he/she wins
def reachedKey(playerX, playerY, keyX, keyY):
    win = False
    if playerX == keyX and playerY == keyY:
        win = True
        print("Nicely Done! You Win! You Found the Key!")

# input: Player's position
# output: Gets player back on the board
def offBoard(pX, pY):
    border = False
    # Determines if the player is on border or not
    if pX == 0 or pX == 9 or pY == 0 or pY == 9:
        border = True
    else:
        border = False
    # Gets player back on board    
    if border == True:
        print("That is an invalid move.")
        if pX == 0:
            pX += 1
        if pX == 9:
            pX -= 1
        if pY == 0:
            pY += 1
        if pY == 9:
            pY -= 1
        #printBoard(pX, pY, 4, 7)    
    return(pX, pY)
# input: Direction and player's original coordinates
# output: Player's new coordinates
def updatePosition(direction, playerX, playerY):
    # Determines which way the player will move
    if direction == "north":
        playerY -= 1
    elif direction == "south":
        playerY += 1
    elif direction == "west":
        playerX -= 1
    elif direction == "east":
        playerX += 1
    # Checks to see if the player is off the board
    playerX, playerY = offBoard(playerX, playerY)
    return(playerX, playerY)

# input: Player's and Key's coordinates
# output: The board with correct player and key positions
def printBoard(playerX, playerY, keyX, keyY):
    if playerX == keyX and playerY == keyY:
        print()
    # Creates a portrait of the board    
    else:
        for i in range(10):
            print("\n")
            for j in range(10):
                if i == 0 or i == 9:
                    print("--", end = "")
                elif i == playerY and j == playerX:
                    print("P", end = " ")
                elif i == keyY and j == keyX:
                    print("K", end = " ")
                elif j == 0 or j == 9:
                    print("|", end = " ")
                else:
                    print(".", end = " ")
    print()            
def main():
    printgreeting()
    # This shows the board
    printBoard(3, 5, 4, 7)
    direction = 0
    # This sets the player up
    playerX = 3
    playerY = 5
    # If the player isn't at the key, he/she will choose a direction
    while playerX != 4 or playerY != 7:
        direction = 0
        while direction != "north" and direction != "south" and direction != "east" and direction != "west":
            direction = input("What direction would you like to go (North, South, East, or West)?: ")
            direction = direction.lower()
        # This updates the player's position    
        playerX, playerY = updatePosition(direction, playerX, playerY)
        # This makes sure the player isn't at the key
        reachedKey(playerX, playerY, 4, 7)
        # This prints the board
        printBoard(playerX, playerY, 4, 7)
main()
