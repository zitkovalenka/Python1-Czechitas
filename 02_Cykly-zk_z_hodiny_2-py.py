#-------------------------------------------------------------------------
# Př. č. 2
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

sales = 0
for item in books:
    sales += item["sold"]
print(f"Celkem bylo prodáno {sales} knih.")

sales = 0
for item in books:
    sales += item["sold"] * item["price"]
print(f"Celkové tržby jsou {sales} Kč.")


# Nakladatele zajímá, jaké jsou peněžní tržby za knihy vydané v roce 2019. U každé knihy tedy musíme zkontrolovat, zda vyšla v roce 2019.
sales = 0
for item in books:
    if item["year"] == 2019:
        sales += item["sold"] * item["price"]
print(f"Celkové tržby za knihy prodané v roce 2019 jsou {sales} Kč.")

# K výběru určitých hodnot ze slovníku můžeme použít i funkci filter(). tzv. lambda funkce
# to stejné jako níže, ale vypíše to za sebe do jednoho řádku
books_2019 = list(filter(lambda item: item["year"] == 2019, books))
print(books_2019)

# to stejné jako filter, ale vypíše to pod sebe
for item in books:
    if item["year"] == 2019:
        print(item)