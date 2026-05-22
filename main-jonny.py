def task3():
    biljettpris = 100
    pengar_pa_fickan = 200

    pengar_over = pengar_pa_fickan - biljettpris
    varje_person_far = pengar_over / 2

    print("Det blir " + str(pengar_over) + " kronor över.")
    print("Varje person får " + str(varje_person_far) + " kronor.")

def task4a():
    nummer = input("Skriv in ett nummer: ")
    nummer = int(nummer)
    print(f"Du skrev in talet: {nummer}")
    
def task4b():
    nummer1 = input("Skriv in ett nummer: ")
    nummer2 = input("Skriv in ett nummer: ")
    summa = int(nummer1) + int(nummer2)
    print(f"Summan av {nummer1} och {nummer2} är {summa}")

def task4c():
    jacka_pris = 2000
    rea_procent = 75.0

    pris_att_betala = jacka_pris * rea_procent / 100

    print("Jackan kostar", pris_att_betala, "kr på rea.")

    
def task4d():
    jacka_pris = 1000

    rabatt_procent = input("Skriv rabatt i procent: ")
    rabatt_procent = float(rabatt_procent)

    rabatt_kronor = jacka_pris * rabatt_procent / 100
    nytt_pris = jacka_pris - rabatt_kronor

    print("Rabatten är", rabatt_kronor, "kr.")
    print("Jackan kostar", nytt_pris, "kr efter rabatt.")
    
def task5_1a():
    avstand_km = 470

    hastighet_kmh = float(input("Hur snabbt kör man i km/h? "))

    tid_timmar = avstand_km / hastighet_kmh

    print("Det tar", tid_timmar, "timmar att köra från Stockholm till Göteborg.")


def task5_1b():
    avstand_km = 470

    hastighet_kmh = float(input("Hur snabbt kör man i km/h? "))

    tid_timmar = avstand_km / hastighet_kmh
    tid_minuter = tid_timmar * 60

    print("Det tar", tid_minuter, "minuter att köra från Stockholm till Göteborg.")


def task5_1c():
    avstand_km = 470

    hastighet_kmh = float(input("Hur snabbt kör man i km/h? "))

    tid_timmar_decimal = avstand_km / hastighet_kmh
    total_minuter = round(tid_timmar_decimal * 60)

    timmar = total_minuter // 60
    minuter = total_minuter % 60

    print("Det tar", timmar, "timmar och", minuter, "minuter att köra från Stockholm till Göteborg.")


def task5_2():
    sida_a = float(input("Skriv längden på första sidan: "))
    sida_b = float(input("Skriv längden på andra sidan: "))

    hypotenusa = (sida_a ** 2 + sida_b ** 2) ** 0.5

    print("Hypotenusan är", hypotenusa)


def task5_3a():
    from datetime import date

    dagens_datum = date.today()

    print("Dagens datum är:", dagens_datum)


def task5_3b():
    from datetime import date, timedelta

    dagens_datum = date.today()
    datum_om_sju_dagar = dagens_datum + timedelta(days=7)

    print("Dagens datum är:", dagens_datum)
    print("Datumet om 7 dagar är:", datum_om_sju_dagar)

print("################################################################")
task3()
print("################################################################")
task4a()
print("################################################################")
task4b()
print("################################################################")
task4c()
print("################################################################")
task4d()
print("################################################################")
task5_1a()
print("################################################################")
task5_1b()
print("################################################################")
task5_1c()
print("################################################################")
task5_2()
print("################################################################")
task5_3a()
print("################################################################")
task5_3b()