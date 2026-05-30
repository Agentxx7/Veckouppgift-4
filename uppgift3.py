def uppgift3_version1():
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")

    total = 0

    while True:
        value = input("Skriv in ett belopp: ")

        if value == "quit" or value == "avsluta":
            break

        total += int(value)

    print("Det blir " + str(total) + " kr totalt. Välkommen åter!")


def uppgift3_version2():
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")

    total = 0

    while True:
        value = input("Skriv in ett belopp: ")

        if value == "quit" or value == "avsluta":
            break

        total += int(value)

    people = int(input("Hur många är ni? "))
    per_person = total / people

    print("Det blir " + str(total) + " kr totalt, alltså " + str(per_person) + " kr per person. Välkommen åter!")


def uppgift3_version3():
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")

    total = 0

    while True:
        value = input("Skriv in ett belopp: ")

        if value == "quit" or value == "avsluta":
            break

        total += int(value)

    people = int(input("Hur många är ni? "))

    tip_input = input("Hur många procent dricks vill ni lägga på? ")

    if tip_input == "":
        tip_percent = 10
    else:
        tip_percent = int(tip_input)

    total_with_tip = total + total * tip_percent / 100
    per_person = total_with_tip / people

    print("Det blir " + str(total_with_tip) + " kr totalt, alltså " + str(per_person) + " kr per person. Välkommen åter!")