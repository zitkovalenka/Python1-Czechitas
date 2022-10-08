# Hotel 
# Napiš funkci total_price, která vypočte cenu noci v hotelu.
# Funkce bude mít dva parametry - persons a breakfast.
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč.
# Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price(persons, breakfast=False):
    cenaOsoba = 850
    cenaSnidane = 125
    if breakfast:    #breakfast == True
        return persons*cenaOsoba + persons*cenaSnidane
    else:
        return persons*cenaOsoba
print(total_price(3))
print(total_price(3, True))


# nebo
def total_price(persons, breakfast=False):
  price_per_person = 850
  if breakfast:
    price_per_person += 125   # k ceně za osobu přičti 125, protože má snídani
  return price_per_person * persons

print(total_price(3))
print(total_price(3, True))
