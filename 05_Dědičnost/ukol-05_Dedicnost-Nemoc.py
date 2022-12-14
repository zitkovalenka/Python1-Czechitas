class Nemoc:
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    # def __init__(self, jmeno, pocet_obeti, sireni):
    def __init__(self, jmeno):
        # super().__init__(jmeno, 12, pocet_obeti, sireni)
        super().__init__(jmeno, 12, 0, "vzduchem")
        self.varianty = []

    def pridej_variantu(self,varianta):
        self.varianty.append(varianta)

# V zádání bylo, že mám převzít metodu zmen_pocet_obeti ze třídy Nemoc? Nemusím dělat nic, vůbec nevpisuji níže uvedenou definici metody/funkce.
# Pokud správně dědím z třídy Nemoc, tak se toto samo dědí/převezme.
# Naopak, když jsem vložila níže uvedenou část, tak při volání funkce/změně počtu obětí mi to pak házelo chybu, že mám 2 atributy na místo jednoho.
    """def zmen_pocet_obeti(pocet_obeti):                  
        super().zmen_pocet_obeti(pocet_obeti)"""

    def __str__(self):
        # return super().__str__() + f" (varianty: {self.varianty})"     # vypíše se celý seznam/list v hranatých závorkách, což je sice ok, ale chceme to vypsat jinak
        return super().__str__() + f" (varianty: {', '.join(self.varianty)})"

corona = Koronavirus("Coronavirus")
# corona = Koronavirus("Coronavirus", 0, "vzduchem")
# corona = Koronavirus('Coronavirus', ['omikron'])  # proč mám volat takhle? Pak tam není počet obětí, ale omikron??
print(corona) 

print(corona.pocet_obeti) # nejake cislo ktere se da menit pomoci metody zmen_pocet_obeti() - muze byt nacatku nula nebo cislo ktere si zvolite pri vytvoreni objektu
print(corona.sireni) # 'vzduchem' -- muzete reprezentovat i cislem
print(corona.inkubacni_doba) # 12 -- je mi jedno jake cislo - pevne dane ve volani super().__init__(...)
corona.pridej_variantu('omikron')
print(corona)
corona.pridej_variantu('delta')
print(corona)
corona.pridej_variantu('alpha')
print(corona)

corona.zmen_pocet_obeti(5)
print(corona.pocet_obeti)