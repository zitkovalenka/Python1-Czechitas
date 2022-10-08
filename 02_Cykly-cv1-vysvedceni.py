# 1 Vysvědčení (to dáš)
# Uvažujme vysvědčení, které máme zapsané jako slovník.

# Napiš program, který spočte průměrnou známku ze všech předmětů.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

suma = 0
pocet = 0
for znamka in school_report.values():
    suma += znamka
    pocet += 1
# print(suma)
# print(pocet)
# prumer = suma/pocet
print(f"Průměrná známka z předmětů na vysvědčení je: {suma/pocet}")
print(f"Průměrna znamka je {sum(school_report.values())/len(school_report)}.")

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
for key, value in school_report.items():
    if value == 1:
        print(key)