class OutOfRange(Exception):
    pass

if __name__ == "__main__":

    print("Deleni")
    print("------")

    counter = 3
    while counter > 0:

        counter -= 1

        try:
            citatel = int(input("Zadej citatel: "))
            jmenovatel = int(input("Zadej jmenovatel: "))

            if citatel < 0 or citatel > 100:
                raise OutOfRange(f"Citatel mimo rozsah <0, 100>")

            if  jmenovatel < 0 or jmenovatel > 100:
                raise OutOfRange(f"Jmenovate mimo rozsah <0, 100>")

            vysledek = citatel / jmenovatel

            print(f"Vysledek deleni je: {vysledek}")

            break
        except ValueError:
            print("Nelze zkonvertovat hodnotu, zadej znovu...")
        except ZeroDivisionError:
            print("Nelze delit nulou, zadej znovu...")
        except OutOfRange as e:
            print(str(e) + ", zadej znovu...")

    print("Konec")

