# Napište interaktivní hru, ve které počítač vygeneruje tajné číslo v rozsahu 1 až 100 (použijte funkci random.randint()). Následně se v cyklu ptejte uživatele, aby zadal číslo 
# a vypisujte vždy jestli je zadané číslo nižší nebo vyšší než tajné číslo. Ukončete cyklus v momentě, kdy uživatel trefí tajné číslo.

import random
zadane_cislo=int(input("Zadej číslo: "))
tajne_cislo=random.randint(0,100)       # nemůžu dát tajne_cislo=print(random.randint(0,100)), protože se do proměnné uloží jen výstup printu, což je None. 
                                        # pokud chci vypsat číslo a ještě ho uložit, musím udělat 2 kroky. Uložit ho a teprve pak vypsat.
print(tajne_cislo)

while zadane_cislo != tajne_cislo:
    print("Netrefil jsi.")
    zadane_cislo=int(input("Zadej číslo: "))
print("Trefil ses!")