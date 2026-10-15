def faktorial(x):
    # 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
    # 4! = 4 * 3 * 2 * 1
    if x == 1:
        return 1
    else:
        return x * faktorial(x - 1)



if __name__ == "__main__":

    print(faktorial(5))

    vek = 62
    pohlavi = "zena"

    # if pohlavi not in ("muz", "zena"):
    #     print("Nezname pohlavi")
    # elif pohlavi == "muz" and vek >= 65 or pohlavi == "zena" and vek >= 63:
    #     print("Jsi v duchodovem veku")
    # else:
    #     print("Nejsi duchodce")

    # while vek < 65:
    #     print(vek)
    #     vek += 1

    # for i in [1, 2, 3, "ctyri", 5]:
    #     if not isinstance(i, int):
    #         continue
    #     print(i + 1)