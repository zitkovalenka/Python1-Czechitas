baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kodBaliku = input("Dobrý den. Jaký je Váš kód balíčku? ")
if kodBaliku in baliky:
    # print("Tento balíček máme.")
    # print(baliky[kodBaliku])
    if baliky[kodBaliku] == True:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík zatím nebyl předán kurýrovi.")
else:
    print("Tento balíček neevidujeme.")