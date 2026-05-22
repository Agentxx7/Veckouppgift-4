def uppgift2():
    lenght = input("Hur lång är du i cm? ")
    lenght = float(lenght)

    if lenght >= 130:
        print("Du får åka på attraktionen!")
    else:
        print("Tyvärr, du är inte tillräckligt lång för att åka på attraktionen.")