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
    def __init__(self, nazev, autor, recepty=[]):
        self.nazev = nazev
        self.autor = autor
        self.recepty = recepty
    def __str__(self):
        return f"{self.nazev} od {self.autor} ({self.pocet_receptu})"
    def pocet_receptu(self):
        self.pocet_receptu = 0
        for i in self.recepty: #self.pocet_receptu:  Kucharka:
            self.pocet_receptu = self.pocet_receptu + 1    # for cyklus?
        return self.pocet_receptu
    def pridej_recept(self, Recept):
        self.recept = Recept
 
recept_1 = Recept("Štrůdl", 3, "https://www.nejrecept.cz/recept/fantasticky-stavnaty-jablecny-zavin-r5687")
recept_1.zmen_narocnost(5)
print(recept_1)
recept_2 = Recept("Bábovka", 2, "https://www.toprecepty.cz/recept/1673-hrnickova-babovka/")
recept_2.zkusit()
print(recept_2)   


kucharka=Kucharka("Dobrůdky", "Lentilka")
print(kucharka) 
kucharka.pridej_recept(recept_1)
print(kucharka.pocet_receptu)


"""class Kucharka:
    def __init__(self, k_nazev, strana):
        self.k_nazev = k_nazev
        self.strana = strana
    def __str__(self):
        return f"{self.k_nazev}                 str {self.strana}"
    def pocet_receptu(self):
        self.pocet = 0
        self.pocet = self.pocet + 1"""

"""class Kucharka:
    def __init__(self, nazev_kucharky, pocet_receptu=0):
        self.nazev_kucharky = nazev_kucharky
        self.pocet_receptu = pocet_receptu
    def __str__(self):
        return f"{self.nazev_kucharky}: {self.pocet_receptu} receptů."
    def pocet_receptu(self):
        self.pocet_receptu = 0
        for i in Kucharka: #self.pocet_receptu:
            self.pocet_receptu = self.pocet_receptu + 1    # for cyklus?
        return self.pocet_receptu
    def pridej_recept(self, Recept):
        self.recept = Recept
"""

"""def get_sleva(self, procento):
        self.cena = self.cena*(1-procento/100)

kniha1 = Kniha("Pokemon",495,279)
kniha1.get_sleva(20)
kniha2 = Kniha("Lolita",252,249)"""




"""
kucharka_1 = Kucharka("Štrůdl",5)
kucharka_2 = Kucharka("Bábovka",7) 
print(kucharka_1)
print(kucharka_2)
"""




#-------------------------------------------------------------------------------------------------------------
"""class Recept:
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


class Kucharka



recept_1 = Recept("Štrůdl", 3, "https://www.nejrecept.cz/recept/fantasticky-stavnaty-jablecny-zavin-r5687")
recept_1.zmen_narocnost(5)
print(recept_1)
recept_2 = Recept("Bábovka", 2, "https://www.toprecepty.cz/recept/1673-hrnickova-babovka/")
recept_2.zkusit()
print(recept_2)
"""

