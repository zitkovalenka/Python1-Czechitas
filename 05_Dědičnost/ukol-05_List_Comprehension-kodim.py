# 1 Seznamy čísel (pohodička)
# Mějme zadaný následující seznam

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]

# Vytvořte seznam, který obsahuje:
# každé z čísel ze seznamu cisla vynásobené dvěma:

print([nasobeni*2 for nasobeni in cisla])

# každé z čísel ze seznamu cisla s opačným znaménkem:
print([nasobeni*-1 for nasobeni in cisla])

# každé z čísel ze seznamu cisla umocněné na druhou:
print([cislo*cislo for cislo in cisla])

# každé z čísel ze seznamu cisla jako řetězec.
print([str(cislo) for cislo in cisla])   #asi toto má být výsledek. Těžko říct


#-----------------------------------------------------------------------------------------------
# 2 Seznamy řetězců (to dáš)
# Mějme zadaný následující seznam

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

# Vytvořte seznam, který obsahuje:

# počty písmen ve všech jménech:
print([len(jmeno) for jmeno in jmena])

# všechna jména napsaná velkými písmeny:
print([jmeno.upper() for jmeno in jmena])

# všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména):
print([jmeno+"a" for jmeno in jmena])

# všechna jména převedená na malá písmena s koncovkou '@email.cz':
print([jmeno.lower()+"@email.cz" for jmeno in jmena])

#-----------------------------------------------------------------------------------------------
# 3 Seznam teplot (zapni hlavu)
# Mějme zadaný následující seznam naměřených teplot.
# Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

# seznam v seznamu (tuším říkala, rozhodně to není slovník v seznamu, to by tam byli skládané závorky)

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# sečíst teploty v řádcích:
soucty = [sum(teplota) for teplota in teploty]
print(soucty)

# Vytvořte seznam průměrných teplot pro každý den
prumer = [sum(teplota)/len(teplota) for teplota in teploty]
print(prumer)

# Vytvořte seznam ranních teplot.
print([teplota[0] for teplota in teploty])

# Vytvořte seznam nočních teplot.
print([teplota[3] for teplota in teploty])

# Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
dvojice ={str(teplota[1]) + "," + str(teplota[2]) for teplota in teploty}
print(dvojice)

# Spočítejte celkovou průměrnou teplotu za celý týden.
soucet = [sum(teplota) for teplota in teploty]
print(soucet)
soucet_cely_tyden = [sum(soucet)]
print(soucet_cely_tyden)

soucet_cely_tyden = [sum([sum(teplota) for teplota in teploty])]
print(soucet_cely_tyden)