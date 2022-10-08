# Seznam hostů na party
# Vraťte se k příkladu se zadáváním seznamu hostu na párty a zkopírujte si kód k sobě do editoru. Upravte program tak, že pokud uživatel v průběhu zadávání jmen napíše "konec", 
# cyklus na zadávání jmen se ukončí.

"""number_of_guests = int(input("Zadej počet hostů: "))
guest_list = []
for i in range(number_of_guests):
    new_guest = input("Zadej jméno hosta: ")
    guest_list.append(new_guest)
print(guest_list)"""


number_of_guests = int(input("Zadej počet hostů: "))
guest_list = []
for i in range(number_of_guests):
    new_guest = input("Zadej jméno hosta nebo 'konec' pro ukonceni seznamu: ")
    if new_guest == "Konec" or new_guest == "konec":
        break
    guest_list.append(new_guest)
print(guest_list)