class Recept:
    def __init__(self, nazev, narocnost, url_adresa,vyzkouseno=False):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = vyzkouseno

    def __str__(self):
        if self.vyzkouseno == True:
            return f"Recept {self.nazev} (náročnost {self.narocnost}) vyzkoušeno: {self.url_adresa}"
        else:
            return f"Recept {self.nazev} (náročnost {self.narocnost}) nevyzkoušeno: {self.url_adresa}"

    def zmen_narocnost(self, nova_narocnost):
        self.narocnost = nova_narocnost

    def zkusit(self):
        self.vyzkouseno = True

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    def __str__(self):
        return f"V kuchařce {self.nazev} od {self.autor} je {self.pocet_receptu()} receptů." 
    def pocet_receptu(self):
        self.pocet_receptu_prom = 0
        for i in self.recepty: 
            self.pocet_receptu_prom = self.pocet_receptu_prom + 1
        return self.pocet_receptu_prom
    """def pocet_receptu(self):
        pocet_receptu = len(self.recepty)
        #print(f"V kucharce je {pocet_receptu} receptů.")  
        return pocet_receptu"""
    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)

 
recept_1 = Recept("Štrůdl", 3, "https://www.nejrecept.cz/recept/fantasticky-stavnaty-jablecny-zavin-r5687")
recept_1.zmen_narocnost(5)
print(recept_1)
recept_2 = Recept("Bábovka", 2, "https://www.toprecepty.cz/recept/1673-hrnickova-babovka/")
recept_2.zkusit()
print(recept_2)   


kucharka=Kucharka("Dobrůdky", "Lentilka")
print(kucharka)
kucharka.pocet_receptu()            # musím nejprve fci zavolat, abych mohla vypsat výsledek
#print(kucharka.pocet_receptu)
kucharka.pridej_recept(recept_1)    # musím nejprve fci zavolat, abych mohla vypsat výsledek
kucharka.pocet_receptu()            # musím nejprve fci zavolat, abych mohla vypsat výsledek
# print(kucharka.pocet_receptu())
print(kucharka)
kucharka.pridej_recept(recept_2) 
kucharka.pocet_receptu()     
print(kucharka)


