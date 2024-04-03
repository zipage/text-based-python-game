import pygame

# Starts up the game. Going to make a main menu
def game():
    gameStartChoice = input(">> Are you ready to move in to your first apartment on campus? (yes / no):")

    # PLAYER CHOICE
    if(gameStartChoice == "yes"):
        print(">> You hope off the bus as you arrive at your new apartment on campus.")
        print("*** You are a freshman staying on campus getting ready to start your first semester at Capital University.")
        start = True  

    else:
        print("Hmm, that doesn't seem to be an option right now.")
        start = False

        