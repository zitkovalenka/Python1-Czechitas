# Pokud si nejsem jistá, jestli je výsledkem True nebo False (výsledke Je 4>5?), tak se na to zeptám tímto programem.
# Tzn. mohu nějaký řetězec převést na pravdivostní hodnotu pomcí bool("nejaky string") stejně jako int(), str() apod.

what = bool(4>5)
print(what)

# Klicove slovo oznacujici prazdny objekt: 
#   []  (prazdny list), {} (prazdny slovnik), "" (prázdný řetězec), None (Klicove slovo oznacujici prazdny objekt)
# Jinými slovy se zde ptám, jestli "" má nebo nemá znak.

if '':
   print('Prazdny string je True')
else:
   print('Prazdny string je False')