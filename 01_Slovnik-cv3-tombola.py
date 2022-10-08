tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
cisloListku = int(input("Jaké je tvé číslo lístku?: "))

if cisloListku in tombola:
    print(f"Vyhráváš: {tombola[cisloListku]}")
    # print("Vyhráváš: " + tombola[cisloListku])
    tombola.pop(cisloListku)
else:
    print("Bohužel nevyhráváš nic.")

print(tombola) #pro kontrolu, že se opravdu záznam vymazal


