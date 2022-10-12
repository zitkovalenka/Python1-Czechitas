class Jednorozec:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva

        self.existuje = False

    def __str__(self):
        return f'{self.jmeno} ({self.barva})'

    def __eq__(self, y):                    # učím tu třídu Jednorožec porovnávat. Srovnání že jednorožec se stejný
        return self.jmeno == y.jmeno

    def zmen_barvu(self, novaBarva):
        self.barva = novaBarva

    def vypis_informace(self):
        vypis = f'Jmenuji se {self.jmeno} a mam {self.barva} barvu'
        if self.existuje:
            vypis += ' a existuje.'
        else:
            vypis += ' a neexistuje.'
        print(vypis)

#karel1 = Jednorozec('Karel1', 'pruhovanej')                # u tét dvojice to hodí False (protože jmeno Karel1 není jméno Karel2)
#karel2 = Jednorozec('Karel2', 'puntikovanej')

karel1 = Jednorozec('Karel', 'pruhovanej')                  # u této dvojice to hodí True (protože jméno Karel se zde nachází 2x, tak se jedná o stejného jednorožce)
karel2 = Jednorozec('Karel', 'puntikovanej')

print(karel1 == karel2)