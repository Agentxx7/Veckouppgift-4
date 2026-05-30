import random


def uppgift5_version1():
    secret = random.randint(1, 100)
    guesses = 0

    print("Välkommen till gissa talet!")
    print("Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

    while True:
        guess = int(input("Gissa: "))
        guesses += 1

        if guess < secret:
            print("Nej, det är för lågt!")
        elif guess > secret:
            print("Nej, det är för högt!")
        else:
            print("Det är rätt!! Du gjorde det på " + str(guesses) + " gissningar.")
            break


def uppgift5_version2():
    secret = random.randint(1, 100)
    guesses = 0

    print("Välkommen till gissa talet!")
    print("Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

    while True:
        guess = int(input("Gissa: "))
        guesses += 1

        difference = abs(secret - guess)

        if guess < secret:
            print("Nej, det är för lågt!")

            if difference <= 5:
                print("Nu börjar det brännas!")

        elif guess > secret:
            print("Nej, det är för högt!")

            if difference <= 5:
                print("Nu börjar det brännas!")

        else:
            print("Det är rätt!! Du gjorde det på " + str(guesses) + " gissningar.")
            break