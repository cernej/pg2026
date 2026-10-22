if __name__ == "__main__":

    # Dvě množiny
    set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    set_b = {3, 4, 5, 6, 1, 2, 11, 12, 13}
    # Výpočet průniku a sjednocení
    prunik = set_a.intersection(set_b)
    sjednoceni = set_a.union(set_b)
    # Výpočet Jaccardova indexu
    jaccard_index = len(prunik) / len(sjednoceni)
    # Výpočet Jaccardovy vzdálenosti
    jaccard_distance = 1 - jaccard_index
    print(f"Jaccardův index: {jaccard_index}")
    print(f"Jaccardova vzdálenost: {jaccard_distance}")
