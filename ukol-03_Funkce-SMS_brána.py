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
