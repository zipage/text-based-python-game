# import pygame

# List of arrays for the different choices Players can make
yes_noChoice = ["yes", "no"]
activityChoice = ["bed", "laptop", "kitchen"]
# major = input("> ");
# > + major +


# Give Player the option to type "Next Day" to sleep and move to the next day.
# ON Game end: You are not ready to start your Student life. You cancel your lease and move back home with your parents for another semester.


while True:
    game()
    restart = input('Play Again: yes / no?')
    if restart == 'N'
        break
    elif restart == 'Y':
        continue

# INTRODUCTION:
print(">> You hop off the bus as you arrive at your new apartment on campus.")

print(" ")
print(
    "*** You are a freshman staying on campus getting ready to start your first semester at Capital University."
)
print(" ")

print(
    "*** You are 18 years-old and this is the first time you moved away from your family to a different country."
)
print(" ")


print(">> Are you ready to start your first semester?")

print(" ")
print("* Choose if you want to begin your Student Life: yes / no *")
print(" ")

startGameChoice = input("> ")

if startGameChoice == "yes":
    print(">> You sign the rental papers for your apartment.")
    print(" ")
    print("* What is your name? *")
    # Ask Player what their name is:
    name = input("> ")
    print(">> Congratulations on your new apartment, " + name + "! ")

    print(" ")
    print("* You are now offically living on campus.")
    print(" ")

    print(
        ">> You don't have orientation until after the weekend, so you walk towards your door."
    )

    print(" ")
    print("*** You read 307 on the apartment door. This was your place.")
    print(" ")


elif startGameChoice == "no":
    print(
        ">> You are not ready to start your Student life. You cancel your lease and move back home with your parents for another semester."
    )
    print(">> The game is now over...")


# Player now enters their new apartment:
print(
    ">> You step inside of your bachelor apartment. You are lucky enough to not need a roommate, as you prefer the space from people anyways."
)
print(
    ">> It was pouring rain when you finally managed to bring the last of your bags in. You are relived to finally be inside."
)
print(">> You hang up your soaked jacket and leave your shoes at the door.")

print(" ")
print("*** You are exhausted from moving and you haven't eaten since lunch.")
print(" ")
print("* You check your watch. It's 8:48pm *")
print(" ")

# Note on the table:
print(">> You find a note on the table. Do you want to read the note? (yes / no)")

readNoteChoice = input("> ")

if readNoteChoice == "yes":
    print(
        ">> You pick up the note and it reads: Welcome to your new place, "
        + name
        + ". Here's the spare key."
    )

elif readNoteChoice == "no":
    print(">> You'll read that note later.")

    print(" ")
else:
    print("* Hmm, that didn't work. Choose an option. *")


# Make Player choose their Major:
print(" ")
print(
    ">> You unpack your LAPTOP from your backpack. You already choose your classes so its time to officially choose your Major. "
)

print(" ")
print("*** You login to the Capital Universities student portal.")

# Prompt to declare their Major:
print(
    ">> Congradulations on enrolling at Capital University! Please declare your Major:"
)

major = input("> ")

print(
    ">> You officially choose your Major. You are now enrolled as a freshman student in "
    + major
    + ", at Capital University!"
)

print(" ")
print("* YAWN *")
print(" ")

print(">> You are starting to feel the tiredness and hunger set in. ")
print(" ")


print("What activity would you like to do right now?")

print(" ")
print("* You look around your small apartment. What should you choose to do? *")
print(" ")
print("*** You can interact with your BED, LAPTOP, and a KITCHEN.*")
print(" ")
activityChoice = input("> ")

if activityChoice == "bed":
    print(
        ">> You walk to your BED. You watch YouTube on your phone until midnight. You fall asleep."
    )

elif activityChoice == "laptop":
    print(">> You go on your LAPTOP and browse social media for a while.")

elif activityChoice == "kitchen":
    print(
        ">> You walk to the KITCHEN. You make dinner. You head to bed and you fall asleep."
    )
    quit()

    print(" ")
else:
    ("* Hmm, that didn't work. Choose an option. *")
    print(" ")
