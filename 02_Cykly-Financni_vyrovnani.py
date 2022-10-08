# finančnímu vyrovnání spolubydlících.

purchase_list = [                                                   # nákupní seznam
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]
# Pokud spolubydlící v našem novém slovníku ještě částku nemá, vložíme tam hodnotu aktuálního nákupu. Pokud tam nějakou částku už má, přičteme k této částce hodnotu aktuálního nákupu.
sum_per_person = {}     # vytvoření prázdného slovníku
for item in purchase_list:
    person = item["person"]
    value = item["value"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

# Vypíšeme si nyní útraty jednotlivých spolubydlících a spočteme celkovou útratu. K tomu můžeme využít cyklus for. Zde je pouze jeden malý rozdíl.
total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

# Jako poslední krok zbývá určení průměrné hodnoty na osobu. Zde opět využijeme funkci len, která umí pracovat i se slovníky.
average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

# Dopiš cyklus, který projde slovník sum_per_person a pro každého ze spolubydlících vypíše, kolik by měl doplatit (pokud utratil(a) méně než průměr), 
# případně kolik by měl obdržet (pokud utratil(a) více než průměr).

"""rozdil = 0
for person, utrata in sum_per_person.items():
    if utrata > average_value:
        rozdil = utrata - average_value
        print(f"{person} by měla obdržet {rozdil} Kč.") 
    else:
        rozdil = average_value - utrata
        print(f"{person} by měla vrátit {rozdil} Kč.") """

rozdil = 0
for person, value in sum_per_person.items():
    if value > average_value:
        rozdil = round((value - average_value),2)
        print(f"{person} by měla obdržet {rozdil} Kč.") 
    elif average_value > value:
        rozdil = round((average_value - value),2)
        print(f"{person} by měla vrátit {rozdil} Kč.") 
    else:
        print("Jsi na 0, nemusíš nic doplácet ani nic nedostaneš.")

# správně má být, aby ten výpočet se udělal jednou a jen pak použil, ale funguje mi to i viz výše.
for person, utrata in sum_per_person.items():
    rozdil = round(average_value - utrata, 2)
    if rozdil > 0:
        print(f'{person} by mel obdrzet {rozdil} Kc.')
    elif rozdil < 0:
        print(f'{person} by mel doplatit {rozdil} Kc.')
        # Pripadne bez minuska
        # print(f'{person} by mel doplatit {rozdil * -1} Kc.')
    else:
        print('Jsi na 0 nemusis nic doplacet a ani nic nedostanes.')