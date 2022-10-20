# BONUS 
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
        return self.vyzkouseno

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return f"V kuchařce {self.nazev} od {self.autor} je {self.pocet_receptu()} receptů." 

    def pocet_receptu(self):
        pocet_receptu_prom = 0
        for i in self.recepty:
            pocet_receptu_prom = pocet_receptu_prom + 1
        return pocet_receptu_prom

    """def pocet_receptu(self):
        pocet_receptu = len(self.recepty)
        #print(f"V kucharce je {pocet_receptu} receptů.")  
        return pocet_receptu"""

    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)

    def vyzkousene_recepty(self):
        vyzkousene_recepty = []
        for recept in self.recepty:  # tady nemuze byt i ale recept kdyz ho pak pouzivas o radek niz (a v řádku níž ho mám, protože se snažím dostat do třídy recept na jeho obsah)
            if recept.vyzkouseno == True:  # male r urcite, nechces celou tridu ale ten konkretni objekt/obsah # nebo stačí jen: if recept.vyzkouseno:
                vyzkousene_recepty.append(recept)   # tady musis pridat jako argument te append tu promennou recept aby se do lsitu neco pridalo a nebyl prazdnej
        return f"{vyzkousene_recepty}"     
# může být klidně i takhle, co je níže a bude to fungovat správně. Trida je jen ta sablona pro to jak se ten objekt chova, je to stejny princip jako kdyz je nejaka promenna retezec, 
# ona je tridy String a ta ma nejake vlastnosti, tvoje promenna typu Recept a ta ma jine vlastnosti
"""def vyzkousene_recepty(self):
        vyzkousene_recepty = []
        for cokoli in self.recepty:
            if cokoli.vyzkouseno:
                vyzkousene_recepty.append(cokoli)
        return f" {vyzkousene_recepty}" """

recept_1 = Recept("Štrůdl", 3, "https://www.nejrecept.cz/recept/fantasticky-stavnaty-jablecny-zavin-r5687")
print(recept_1)
recept_1.zmen_narocnost(5)
print(recept_1)
recept_2 = Recept("Bábovka", 2, "https://www.toprecepty.cz/recept/1673-hrnickova-babovka/")
print(recept_2)
# recept_2.zkusit()
# print(recept_2)  
recept_3 = Recept("Croissant", 5, "https://www.toprecepty.cz/recept/5541-croissanty/")
print(recept_3)

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
kucharka.pridej_recept(recept_3) 
kucharka.pocet_receptu()     
print(kucharka)
"""
print(kucharka.vyzkousene_recepty())
recept_2.zkusit()
print(recept_2)  
print(kucharka.vyzkousene_recepty())
"""
recept_2.zkusit()
print(recept_2)
recept_3.zkusit()
print(recept_3)

kucharka.vyzkousene_recepty()


