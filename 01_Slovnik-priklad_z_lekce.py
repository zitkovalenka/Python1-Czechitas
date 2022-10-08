item = {
    "title": "Čajová konvička s hrnky",
    "price": 899,
    "in_stock": True
}

print(item['price'])
print(item.get('aa', 'Neexistuje')) # item aa neexistuje
print(f"Vybraný předmět je {item['title']} a stojí {item['price']} Kč.")

item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
if '899' in item.values():
    print("Je")
else:
    print("Neni")

item['price'] = 455

item['cena'] = item['price']
item.pop('price')

print(len(item))