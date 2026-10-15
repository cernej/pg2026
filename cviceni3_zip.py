def my_zip(*iterables):
    """
    Nase vlastni implementace zip()

    iterables = [
        ["Alice", "Bob", "Karel", "Eva", "Martin"], -> len() -> 5
        [  30,     20,     24,     18,     27    ],
        [  50,     80,     90,     55,     67    ]
    ]

    results = [
        ('Alice', 30, 50),
        ('Bob',   20, 80),
        ('Karel', 24, 90),
        ('Eva',   18, 55),
        ('Martin',27, 67)
    ]
    """
    pass


if __name__ == "__main__":

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [  30,     20,     24,     18,     27    ]
    vaha =  [  50,     80,     90,     55,     67    ]

    vysledek = list( zip(jmena, vek, vaha) )
    print(vysledek)
    # for jmeno, vek, vaha in vysledek:
    #     print(f'{jmeno} je {vek} let a vazi {vaha} kg')

    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)