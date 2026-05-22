def version1():
    celsius = float(input("Skriv in en temperatur i grader Celsius: "))

    fahrenheit = 1.8 * celsius + 32

    print(f"Det blir {fahrenheit} grader Fahrenheit.")


def version2():
    choice = input("Vill du ange temperaturen i Celsius eller Fahrenheit? Skriv C eller F: ")
    temperature = float(input("Skriv in temperaturen: "))

    if choice == "C":
        fahrenheit = 1.8 * temperature + 32
        print(f"Det blir {fahrenheit} grader Fahrenheit.")
    else:
        celsius = (temperature - 32) / 1.8
        print(f"Det blir {celsius} grader Celsius.")


def version3():
    choice = input("Vill du ange temperaturen i Celsius eller Fahrenheit? Skriv C eller F: ")
    temperature = float(input("Skriv in temperaturen: "))

    if choice == "C":
        celsius = temperature
        fahrenheit = 1.8 * celsius + 32

        print(f"Det blir {fahrenheit} grader Fahrenheit.")

    else:
        fahrenheit = temperature
        celsius = (fahrenheit - 32) / 1.8

        print(f"Det blir {celsius} grader Celsius.")

    if celsius < 10:
        print("Det är kallt. Ta på dig vinterkläder.")

    elif celsius >= 20:
        print("Det är varmt. Packa badkläder.")


def uppgift4():
    version1()
    # version2()
    # version3()