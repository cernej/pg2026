if __name__ == "__main__":
    seznam = ["aaa", "bbb", "ccc", "zzz"]
    print(seznam)
    seznam.append("xxx")
    print(seznam)
    seznam.insert(1, "zzz")
    print(seznam)
    seznam.remove("zzz")
    print(seznam)
    prvek = seznam.pop(2)
    print(prvek)
    print(seznam)

    seznam2 = {1, 2, 3, 4}
    seznam.extend(seznam2)
    print(seznam)

    seznam = seznam + [100, 200] * 2
    print(seznam)

    x = [1, 2, 2, 2, 2, 4, 5, 6, 7]
    print(x)
    x = sorted(list(set(x)))
    print(x)

    if 3 not in x:
        x.append(3)
    print(x)
    print(3 in x)

    _, _, p3, _, _, _, p7 = x
    print(p3)
    print(p7)

    slovnik = {
        "jmeno": "Vlada",
        "vek": 25,
        "znamky": [1,1,1,2,3,3,3]
    }
    print(slovnik)
    slovnik["vek"] += 1
    print(slovnik)
    slovnik["prumer"] = sum(slovnik["znamky"]) / len(slovnik["znamky"]) if len(slovnik["znamky"]) > 0 else None
    # stejny zapis predchozi podminky
    # if len(slovnik["znamky"]) > 0:
    #     slovnik["prumer"] = sum(slovnik["znamky"]) / len(slovnik["znamky"])
    # else:
    #     slovnik["prumer"] = None
    print(slovnik)
    j = slovnik.pop("jmeno")
    print(j)
    print(slovnik)

    for klic, hodnota in slovnik.items():
        print(klic)
        print(hodnota)

    obor = {
        "nazev_oboru": "Informatika",
        "zamereni": "Systemove inzenyrstvi",
        "vek": 30
    }
    slovnik.update(obor)
    print(slovnik)