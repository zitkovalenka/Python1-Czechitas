#Balík
"""Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
Připoj ke třídě funkci doruc, která změní hodnotu parametru doruceno na True.
Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.
"""


class Balik:
    def __init__(self, adresa, hmotnost, doruceno = False):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = doruceno

    def doruc(self):
        self.doruceno = True
    
    def __str__(self):
        return f"Balík {self.adresa} o hmotnosti {self.hmotnost} byl doručen {self.doruceno}"

BX123456 = Balik("U Lavičky 15", "15kg")
BX987654 = Balik("Trafika 177", "3kg")
print(BX123456)


#-----------------------------------------------------------------------
# dle lektorky

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.dorucen = False

    def dorucit(self):
        self.dorucen = True

    def __str__(self):
        return (
            f"Balik na adresu {self.adresa}, hmotnost {self.hmotnost}"
            f' - {"doručen" if self.dorucen else "nedoručen"}'
        )

BX123456 = Balik("U Lavičky 15", "15kg")
BX987654 = Balik("Trafika 177", "3kg")

print(BX123456)
BX123456.dorucit()     # až zde se změní defaultně nastavené "nedoručeno"  na doručeno. Protože jsem zavolala funkci, že bylo doručeno.
print(BX123456)

#------------------------------------------------------------------------------
class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def doruc(self):
        self.doruceno = True

    def __str__(self):
        vypis = f'{self.adresa}({self.hmostnos} kg) - {self.doruceno}'
        return vypis
