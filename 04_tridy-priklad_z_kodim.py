"""
class Zamestnanec:
    def vypis_informace(self):
        return f"{self.jmeno} pracuje na pozici {self.pozice}."

frantisek = Zamestnanec()
frantisek.jmeno = "František Novák"
frantisek.pozice = "konstruktér"
print(frantisek.vypis_informace())

klara = Zamestnanec()
klara.jmeno = "Klára Nová"
klara.pozice = "konstruktérka"

print(frantisek.vypis_informace())
print(klara.vypis_informace())
"""
# -----------------------------------------------------------------

class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice

    def vypis_informace(self):
        return f"{self.jmeno} pracuje na pozici {self.pozice}."

frantisek = Zamestnanec("František Novák", "konstruktér")
klara = Zamestnanec("Klára Nová", "svářeč")

print(frantisek.vypis_informace())
print(klara.vypis_informace())

