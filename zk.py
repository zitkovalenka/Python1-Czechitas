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
number = int(input("Zadejte číslo lístku: "))
if number in tombola:
  # Funkce pop odstraní hodnotu ze slovníku a tuto odstraňovanou hodnotu vrací. 
  # Můžeme ji tedy uložit do proměnné a nemusíme načítat výhru pomocí hranatých závorek.
  win = tombola.pop(number)
  win = win.lower()
  print(f"Vyhráváš: {win}.")
else:
  print("Bohužel nevyhráváš nic.")