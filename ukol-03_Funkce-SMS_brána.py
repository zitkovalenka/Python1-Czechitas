import math

def overeni(phone_no):
    if len(phone_no) == 13:
        if phone_no[0:4] == "+420":
            platne_cislo = True
            #print(f"Zadal jsi platné 13 místné číslo. {platne_cislo}")
            print(f"Zadal jsi platné 13 místné číslo.")
            return platne_cislo
        else:
            platne_cislo = False
            #print(f"Zadal jsi číslo s předvolbou mimo ČR. {platne_cislo}")
            print(f"Zadal jsi číslo s předvolbou mimo ČR.")
            return platne_cislo
    elif len(phone_no) == 9:
        platne_cislo = True
        #print(f"Zadal jsi platné 9 místné číslo. {platne_cislo}")
        print(f"Zadal jsi platné 9 místné číslo.")
        return platne_cislo
    else:
        platne_cislo = False
        #print(f"Zadal jsi neplatné číslo. {platne_cislo}")
        print(f"Zadal jsi neplatné číslo.")
        return platne_cislo

def get_message_price(msg):
    length_mes=len(msg)
    price_message = math.ceil(length_mes/180)*price_per_unit
    print(f"Délka zprávy je {length_mes} znaků a stojí {price_message} Kč.")
    return price_message

price_per_unit=3
phone_no=str(input("Zadej telefonní číslo, kam chceš zaslat SMS: "))
phone_no=phone_no.replace(" ","")

je_cislo_platne = overeni(phone_no)
if je_cislo_platne:                   # if je_cislo_platne == True
    message = str(input("Zadej text své zprávy: "))
    get_message_price(message)
else: 
    print("Neznámé číslo.")

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