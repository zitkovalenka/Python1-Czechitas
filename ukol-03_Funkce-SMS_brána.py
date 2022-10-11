


phoneNo=str(input("Zadej telefonní číslo, kam chceš zaslat SMS: "))
phoneNo=phoneNo.replace(" ","")
platneCislo=False
def overeni(phoneNo,platneCislo:bool=False):
    if len(phoneNo) == 13:
        if phoneNo[0:4] == "+420":
            platneCislo = True
            print(f"Zadal jsi platné 13 místné číslo. {platneCislo}")
            return platneCislo
        else:
            platneCislo = False
            print(f"Zadal jsi číslo s předvolbou mimo ČR. {platneCislo}")
            return platneCislo
    elif len(phoneNo) == 9:
        platneCislo = True
        print(f"Zadal jsi platné 9 místné číslo. {platneCislo}")
        return platneCislo
    else:
        platneCislo = False
        print(f"Zadal jsi neplatné číslo. {platneCislo}")
        return platneCislo


import math
message = str(input("Zadej text své zprávy: "))
lengthMes=len(message)
pricePart=3
def priceMessage(lengthMes,pricePart):
    priceMessage = math.ceil(lengthMes/180)*pricePart
    print(f"Délka zprávy je {lengthMes} znaků a stojí {priceMessage} Kč.")
    return priceMessage


overeni(phoneNo,platneCislo)
if platneCislo==True:
    priceMessage(lengthMes,pricePart)
else: 
    platneCislo==False
    break

    




#----------------------------------------------------------------------------------------
"""
import math
phoneNo=str(input("Zadej telefonní číslo ve formátu +420xxx, kam chceš zaslat SMS: "))
phoneNo=phoneNo.replace(" ","")

def overeni(phoneNo):
    if len(phoneNo) == 13:
        predvolba = phoneNo[0:4]
        if predvolba != "+420":
            print("Zadal jsi předvolbu státu mimo ČR.")
        else:
            message = str(input("Zadej text své zprávy: "))
            lengthMes=len(message)
            pricePart=3
            def priceMessage(lengthMes,pricePart):
                priceMessage = math.ceil(lengthMes/180)*pricePart
                print(f"Délka zprávy je {lengthMes} znaků a stojí {priceMessage} Kč.")
                return priceMessage
            priceMessage(lengthMes,pricePart)
    else:
        print(f"Zadal jsi číslo ve špatném formátu.")
overeni(phoneNo)
"""