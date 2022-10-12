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