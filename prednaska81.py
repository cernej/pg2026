def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


class Math:
    @staticmethod
    def add(*numbers):
        result = 0
        for number in numbers:
            result += number
        return result


if __name__ == "__main__":
    vysledek = Math.add(1, 2, 3, 4, 5, 6)
    print(vysledek)