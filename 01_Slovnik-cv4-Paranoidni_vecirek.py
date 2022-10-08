passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
host = input("Ahoj, řekni mi své jméno: ")
if host in passwords:
    hostHeslo = input("Jaké je tvé heslo?: ")
    if hostHeslo in passwords[host]:  # lze i takto: if password == passwords[name]:
        print("Smíš vstoupit.")
    else:
        print("Špatné heslo.")
else:
    print("Nejsi na seznamu.")
