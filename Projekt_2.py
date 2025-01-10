"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Slámová
email: petja24@seznam.cz
"""
import random
import time

separator = "-" * 40
print(
    "Ahoj!\n"
    + separator
    + "\n"
    + "Vygenerovala jsem náhodné čtyřciferné číslo.\n"
    + "Pojďme si zahrát hru bulls & cows.\n"
    + separator
)

import random


def vygeneruj_cislo():  # Generuje náhodné čtyřciferné číslo
    prvni_cislo = random.choice("123456789")  # první číslice nesmí být nula
    ostatni_cisla = random.sample(
        "0123456789".replace(prvni_cislo, ""), 3
    )  # zbývající 3 číslice
    cislo = prvni_cislo + "".join(ostatni_cisla)  # složíme číslo
    return cislo


def vysledek_tipu(hadane, uhodnute):  # Vrátí počet bulls a cows
    bulls = sum(1 for i in range(4) if hadane[i] == uhodnute[i])
    cows = sum(
        1 for i in range(4) if hadane[i] != uhodnute[i] and uhodnute[i] in hadane
    )
    return bulls, cows


uhodnute = vygeneruj_cislo()  # generování náhodného čtyřciferného čísla
odpocet = time.time()  # začínám počítat čas

pokusy = 0

print(f"Napiš své číslo:\n{separator}")
while True:
    hadane = input(">>> ")

    # kontrola, jestli hráč zadal číslo správně

    if (
        len(hadane) != 4
        or not hadane.isdigit()
        or len(set(hadane)) != 4
        or hadane[0] == "0"
    ):
        print(
            "Neplatný pokus! Zadej čtyřmístné číslo, nezačínající nulou, složené z různých číslic."
        )
        continue
    pokusy += 1

    bulls, cows = vysledek_tipu(hadane, uhodnute)  # vyhodnocení

    print(f"Bulls: {bulls}, Cows: {cows}")

    print(separator)

     if bulls == 4:  # Pokud hráč uhodl číslo
        celkovy_cas = time.time() - odpocet
        print(f"Blahopřeji! Uhodl/a jsi číslo {uhodnute} v {pokusy} pokusech.")
        print(f"Celkový čas: {celkovy_cas:.2f} sekund.") # Vytiskne čas se dvěma desetinnými místy
        print(separator + "\n" + "Výborně!")
        break
