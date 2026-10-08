if __name__ == "__main__":

    seznam = [1, 2, 3, 4]

    #x = input("Pridej prvek: ")
    #seznam.append(x)

    a = seznam.pop(1)
    print("Odstraneny druhy prvek", a)

    print("Cely seznam", seznam)
    print("Prvni prvek", seznam[0])
    seznam[0] = 10
    print("Prvni prvek", seznam[0])

    n_tice = (1, 2, 3, 4)
    print("Cela Ntice", n_tice)
    print("Prvni prvek", n_tice[0])

    slovnik = {"jmeno": "Vlada"}
    print("Cely slovnik", slovnik)
    print("Jmeno", slovnik["jmeno"])
    slovnik["jmeno"] = "Petr"
    slovnik["vek"] = 20
    slovnik[0] = 1
    print("Cely slovnik", slovnik)


    uzivatele = [{"jmeno": "Vlada", "vek": 25}, {"jmeno": "Petr", "vek": 20}]
    print(uzivatele[1]["jmeno"])

    {"jmeno":"Vlada", "data": [1,2,3,4]}

    mnozina = {1, 2, 3, 4}
    print("Mnozina", mnozina)
    print("Mnozina obsahuje 5", 5 in mnozina)
    mnozina.add(5)
    mnozina.add(5)
    mnozina.add(5)
    print("Mnozina obsahuje 5", 5 in mnozina)
    print("Mnozina", mnozina)

    a = [1, 2, 3]
    print("Seznam A", a)
    b = a
    print("Seznam B", b)
    b.append(4)
    print("Seznam A", a)
    print("Seznam B", b)

    print("Promenne odkazuji na stejny seznam", a is b)
