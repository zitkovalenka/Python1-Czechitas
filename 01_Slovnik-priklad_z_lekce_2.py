baliky = {
    "B541X": 111,
    "B547X": 222,
    "B251X": 333,
    "B501X": 444,
    "B947X": 555
}

if 222 in baliky.values(): #vyhledá v hodnotě 222 a najde ho tam. Vypíše "Je"
    print("Je")
else:
    print("Neni")

if "B541B" in baliky.keys(): #vyhledá v klíči B541B a nenajde ho tam. Vypíše "Není". Pokud by hledal B541X, najde ho tam a vypíše "Je". 
    print("Je")              #může být zapsané jako: if "B5415" in baliky: a vyhledávalo by to stále v klíčích. Protože defaultní nastavení slovníků ve IN fci je hledání v klíčích.
else:
    print("Neni")