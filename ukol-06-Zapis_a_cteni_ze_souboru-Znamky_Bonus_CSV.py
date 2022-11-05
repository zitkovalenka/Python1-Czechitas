import csv

with open("ukol-06-znamky_za_semestr.csv","r", newline="", encoding="utf-8") as vstup:
    radky = vstup.readlines()     # readlines() vytvoří seznam stringů a rozděluje soubor na řádky pomocí \n. Není tedy potřeba radek = [radek.split() for radek in radky]   

radek_1 = radky[0]
znamky_replace = [radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","F") for radek in radky[1:]]

k_zapsani = [radek_1] + znamky_replace

with open("ukol-06-znamky_za_semestr-opraveno.csv","w", newline="", encoding="utf-8") as vystup:
    vystup.writelines(k_zapsani) 