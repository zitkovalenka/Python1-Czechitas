# list(range(1,11,2))
# print(list(range(1,11,2)))

""" for item in range(3):
    print("Knock")
print("Penny") """

#-------------------------------------------------------------------------
# Př. č.1
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

"""for key in sales:
    print(key)"""

for key, value in sales.items():
    print(f"Knihy", key, "bylo prodáno", value, "výtisků.")
    # Použití f-stringu
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
# Zkusme si nyní spočítat celkový počet prodaných kusů. Vytvoříme si tedy proměnnou total_sales a pro každou knihu do ní přičteme počet prodaných kusů.

total_sales = 0
for key, value in sales.items():
    print(f"Knihy", key, "bylo prodáno", value, "výtisků.")
    # Použití f-stringu
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
    total_sales += value
print(f"Celkem bylo prodáno {total_sales} výtisků.")