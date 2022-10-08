# 1.  Zkusíme si nejprve vypsat všechna čísla od 0 do nějaké hodnoty.
"""stop = int(input("Zadej konec: "))
for i in range(stop):
    print(i)"""

# 2. 
"""start = int(input("Zadej začátek: "))
stop = int(input5("Zadej konec: "))
for i in range(start, stop):
    print(i)"""

# 3. Opět platí, že dovnitř cyklu můžeme vložit podmínku. Zkusme si například vypsat pouze ta čísla z daného rozsahu, která jsou dělitelná třemi.
"""start = int(input("Zadej začátek: "))
stop = int(input("Zadej konec: "))
for i in range(start, stop):
    if i % 3 == 0:    # tedy zbytek po celočíselném dělení = 0
        print(i)
"""
# 4. Seznam hostů nemusíme zapisovat přímo do programu, ale můžeme požádat uživatele, aby nám jména hostů postupně zadával. Jména pak připojujeme k seznamu stávajícímu hostů 
# pomocí funkce append.

"""number_of_guests = int(input("Zadej počet hostů: "))
guest_list = []
for i in range(number_of_guests):
    new_guest = input("Zadej jméno hosta: ")
    guest_list.append(new_guest)
print(guest_list)"""

# 5. Uvažujme třeba prekérní situaci, kdy na poslední chvíli potřebujeme objednat dárek na oslavu narozenin. Máme seznam zboží v e-shopu a u každého zboží máme jeho název, 
# cenu a počet kusů skladem. Vzhledem k situaci potřebujeme, aby bylo zboží skladem a současně chceme dárek s cenou od 500 do 1000 Kč. Protože nemáme čas, spokojíme se 
# s prvním nalezeným dárkem.

list_of_items = [
    {"title": "Modrá kravata", "price": 239, "in_stock": True},
    {"title": "Luxusní psací pero", "price": 1599, "in_stock": True},
    {"title": "Degustační balíček kávy", "price": 599, "in_stock": True},
    {"title": "Parfém", "price": 559, "in_stock": False},
    {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True},
    {"title": "Sklenice na víno", "price": 799, "in_stock": True},
    {"title": "Fitness náramek", "price": 2399, "in_stock": False},
]

for item in list_of_items:
    if 500 <= item["price"] <= 1000 and item["in_stock"]:
        print(f"Vybraný dárek je {item['title']}")
        break
