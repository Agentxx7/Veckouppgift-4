def calculate_discount(price):
    level1 = 100
    level2 = 300

# Vi kollar level2 först, annars blir även level1 true när priset är över 300.
# Då kunde kunden få både 10% och 25% rabatt.
# Med if/elif får kunden bara en rabattnivå.

    if price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
        return 25

    elif price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
        return 10

    else:
        return 0


def uppgift1():
    price = input("Välkommen, köp något dyrt: ")
    price = float(price)

    discount = calculate_discount(price)

    final_price = price * (100 - discount) / 100

    print("Efter rabatter blir priset.... " + str(final_price))