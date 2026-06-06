# Uppgift 1
# Funktionen tar emot en sträng som parameter.
# När funktionen anropas skriver den ut namnet tillsammans med texten.
def uppgift1(name):
    print(name + " är en fena på programmering")


# Uppgift 2a och 2b
# Funktionen eko tar emot en sträng och upprepar den.
# count har standardvärdet 2, så eko("hej") skriver ut "hejhej".
# Om man skickar in count, till exempel eko("hej", 3), skrivs "hejhejhej" ut.
def eko(text, count=2):
    print(text * count)


# Uppgift 3
# Koden är flyttad in i en funktion.
# Loopen ska avslutas efter 5 varv.
def loopa_fem_varv():
    end = 5
    y = 1

    for x in range(1, 100):
        y *= 2

        # Här avslutar vi loopen när x har blivit samma som end.
        # Eftersom end är 5 kommer loopen bara gå 5 varv.
        if x == end:
            break

    print(y)


# Uppgift 4
# Funktionen tar emot en lista och returnerar sista elementet.
def last(items):
    return items[-1]


# Uppgift 5
# Funktionen tar emot en lista och returnerar en ny lista
# utan första och sista elementet.
def cut_edges(items):
    return items[1:-1]


# Uppgift 6
# Ursprunglig kod:
#
# def increase(x):
#     return x
#     x += 1
#
# Felet var att return x låg före x += 1.
# När Python kommer till return avslutas funktionen direkt.
# Därför kördes aldrig x += 1.
#
# Rätt lösning är att först öka x med 1 och sedan returnera värdet.
def increase(x):
    x += 1
    return x


# Uppgift 7
# Funktionen tar emot två tal och returnerar medelvärdet.
# Formeln är: (x + y) / 2
def average(x, y):
    result = (x + y) / 2
    return result


# Uppgift 8
# Funktionen skriver ut innehållet i en lista på ett snyggare sätt.
# Först kontrollerar den om listan är tom.
# Annars skriver den ut hur många element listan har
# och sedan varje element som en punktlista.
def pretty_print(items):
    if len(items) == 0:
        print("Listan är tom.")
        return

    print(f"Listan har {len(items)} element:")

    counter = 1
    for item in items:
        print(f"{counter}. {item}")
        counter += 1