def pricti_jednicku(a):
    return a / 0

def vem_desaty_prvek_a_pricti_jednicku(seznam):
    seznam[9] = pricti_jednicku(seznam[9])
    return seznam

def nacti_cisla_ze_souboru_a_zpracuj(jmeno_souboru):
    fp = open(jmeno_souboru, "r")
    obsah = fp.read()
    fp.close()
    text_seznam = obsah.split(",")
    ciselny_seznam = []
    for prvek in text_seznam:
        try:
            ciselny_seznam.append(int(prvek))
        except ValueError:
            continue
    try:
        ciselny_seznam = vem_desaty_prvek_a_pricti_jednicku(ciselny_seznam)
    except ZeroDivisionError:
        print("chyba pri deleni nulou")
    return ciselny_seznam

if __name__ == "__main__":
    try:
        jmeno = input("Zadej jmeno souboru ke zpracovani: ")
        vysledek = nacti_cisla_ze_souboru_a_zpracuj(jmeno)
        print(vysledek)
    except Exception as e:
        fp = open("exceptions.log", "a")
        fp.write(str(e) + "\n")
        fp.close()