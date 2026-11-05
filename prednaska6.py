from cviceni4_jaccard import jaccardova_vzdalenost_mnozin
import sys
import time
import datetime
import random

symboly = ['🍒', '🍋', '🍊', '🍇', '🔔', '💎', '7️⃣']

def hraci_automat():
    step = 0
    while True:
        step += 1
        vysledek = []
        for i in range(3):
            vysledek.append(random.choice(symboly))
        print(vysledek)
        if len(set(vysledek)) == 1:
            print(f"Vyhra v {step} kole")
            break



if __name__ == "__main__":
    # a = {1, 2, 3, 4}
    # b = {3, 4, 5, 6}
    # jd = jaccardova_vzdalenost_mnozin(a, b)
    # print(jd)

    # ts = time.time()
    # hraci_automat()
    # print(f"Cas behu funkce hraci_automat: {(time.time() - ts)*1000} ms")

    # d = datetime.date.today()
    # print(d)
    # d += datetime.timedelta(days=7)
    # print(d.strftime("%d. %m. %Y"))

    # n = datetime.datetime.now()
    # print(n)
    # n += datetime.timedelta(seconds=3600)
    # print(n.strftime("%H:%M:%S %d. %m. %Y"))

    if len(sys.argv) <= 1:
        print(f"Pouziti: {sys.argv[0]} nazev_souboru")
        sys.exit()
    print(f"Provadim operace se souborem {sys.argv[1]}")