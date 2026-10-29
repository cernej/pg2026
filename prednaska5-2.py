if __name__ == "__main__":

    radky = ["Prvni radek", "Druhy radek"]

    with open("novy-soubor.txt", "w") as fp:
        for radek in radky:
            fp.write(radek + "\n")

    with open("novy-soubor.txt", "r") as fp:
        line = fp.readline()
        while line:
            print(line)
            print("+++")
            line = fp.readline()

    with open("novy-soubor.txt", "a") as fp:
        fp.write("Treti radek")

    with open("novy-soubor.txt", "r") as fp:
        for line in fp:
            print(line)
            print("---")