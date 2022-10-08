
# 3 Měsíc narození (zapni hlavu)
# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

# 1. možnost:

def month_of_birth(rodneCislo): 
    mesic = rodneCislo[2] + rodneCislo[3]
    mesic = int(mesic)
    if mesic > 50:
      mesic = mesic - 50
    else:
      mesic = mesic
    print(mesic)
    return mesic
#month_of_birth("8252273986")   # zkouším ženské RČ
month_of_birth("8005063836")    # zkouším mužské RČ


# 2. možnost:
def month_of_birth(rodneCislo): 
    mesic = rodneCislo[2] + rodneCislo[3]
    mesic = int(mesic)
    if mesic > 50:
      mesic = mesic - 50
    else:
      mesic = mesic
    print(mesic)
    return mesic
month_of_birth(input("Zadej své rodné číslo bez lomítka: "))


# 3. možnost dle lektorky:


def month_of_birth(birth_number):
  month = birth_number[2] + birth_number[3]
  month = int(month)
  month = month % 50    # hint trochu na tu ruletu, podobné řešení s tím děleno. 60/50=1 a zbytek je 10 (tedy 60%50 = 10, takže se jedná o 10.měsíc u ženy)
                        # Ale zde se to dá obejít tak, že dám if > 50 atd. (kvůli té ženě)
  return month

print(month_of_birth("9555125899"))

# 4. možnost dle lektorky:

def month_of_birth(number):
    month = int(str(number)[2:4])     # rozpětí, je to 3. a 4. znak
    if month > 12:
        month -= 50
    return month
print(month_of_birth("8252273986"))   