
with open("ukol-06-znamky_za_semestr.txt","r", encoding="utf-8") as vstup:
    prvni_radek = vstup.readline()
    radky = vstup.readlines()

radek = [radek.split() for radek in radky]    

if radky != prvni_radek:
    znamky_replace = [radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","F") for radek in radky]

with open("ukol-06-znamky_za_semestr-opraveno.txt","w", encoding="utf-8") as vystup:
    vystup.writelines(prvni_radek)

with open("ukol-06-znamky_za_semestr-opraveno.txt","a", encoding="utf-8") as vystup:
    vystup.writelines(znamky_replace)

#=====================================================================================================================================
# jak se to dá udělat přes radek[0] a pro kazdy radek v radky[1:] zapiš řádek s replacenutými hodnotami? Tak, jak psala Andy?
# radky = nejaky list
# zapisu radky[0] do souboru / ulozi msi do modifikovanych radku
# pro kazdy radek v radky[1:] zapisu radek s replacnutymi hodnotami / ulozi msi h odo seznamu k zapsani

# dle koučky

with open("ukol-06-znamky_za_semestr.txt","r", encoding="utf-8") as vstup:
    radky = vstup.readlines()     # readlines() vytvoří seznam stringů a rozděluje soubor na řádky pomocí \n. Není tedy potřeba radek = [radek.split() for radek in radky]   

radek_1 = radky[0]
znamky_replace = [radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","F") for radek in radky[1:]]

k_zapsani = [radek_1] + znamky_replace

with open("ukol-06-znamky_za_semestr-opraveno.txt","w", encoding="utf-8") as vystup:
    vystup.writelines(k_zapsani)   # write zapíše jen jeden řádek, writelines() píše víc řádku v listu najednou.

    # a nebo
    # vystup.write(radek_1)
    # for radek in znamky_replace:
    #     vystup.write(radek)
