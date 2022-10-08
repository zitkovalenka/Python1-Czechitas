# V tombole bylo prodáno celkem 1000 lístků. Naším úkolem je vylosovat náhodně tři výherce. Napište program, který vygeneruje a vypíše tři čísla mezi 1 a 1000. 
# Využijte funkci randint, nezapomeňte ale, že si ji musíte importovat z modulu random.
# Neřešte, že jedno číslo může být vygenerováno dvakrát.

# mé řešení
import random
for i in range(1,4):
    print(random.randint(1,1000))


# dle lektorů
import random
for i in range(3):
    print(random.randint(1, 1000))


# Slo by i pridat cisla do listu a pak vypsat list
import random
vyherci = []
for i in range(3):
    vyherci.append(random.randint(1, 1000))
print(vyherci)