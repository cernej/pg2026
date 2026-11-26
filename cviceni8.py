import json

class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.__telefon = telefon
        self.__email = email
    
    @property
    def jmeno(self):
        return self.__jmeno
    
    @property
    def telefon(self):
        return self.__telefon
    
    @property
    def email(self):
        return self.__email

    @staticmethod
    def test_jmeno(hodnota):
        return hodnota.replace(" ", "").isalpha()

    @jmeno.setter
    def jmeno(self, hodnota):
        if self.test_jmeno(hodnota):
            self.__jmeno = hodnota
        else:
            raise InvalidData("Jmeno muze obsahovat pouze pismena")

    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isnumeric():
            self.__telefon = hodnota
        else:
            raise InvalidData("Cislo muze obsahovat pouze cislice")

    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("Email musi obsahovat @")
        if "." not in hodnota:
            raise InvalidData("Email musi obsahovat tecku")
        if hodnota.replace("@", "").replace(".", "").isalnum():
            self.__email = hodnota
        else:
            raise InvalidData("Email musi obsahovat pouze pismena a cislice")

    def __str__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"
    
    def __repr__(self):
        return f"objekt Osoba({self.jmeno}, {self.telefon}, {self.email})"

    @classmethod
    def load_json_data(cls, data):
        if "jmeno" not in data or "telefon" not in data or "email" not in data:
            return None
        if not cls.test_jmeno(data["jmeno"]):
            return None
        return cls(data["jmeno"], data["telefon"], data["email"])

if __name__ == "__main__":
    # o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")
    # o.jmeno = "Tomas Novotny"  # kontrola, ze jmeno obsahuje pouze pismena
    # o.telefon = "00456887876"  # kontrola, ze telefon obsahuje jenom cisla
    # o.email = "xxx1@xxx.xx"  # kontrola, ze email obsahuje pouze pismena, cisla, zavinac a tecky
    # print(o)
    osoby = []
    with open("osoby.json") as f:
        data = json.loads(f.read())
        for record in data:
            osoby.append(Osoba.load_json_data(record))
    print(osoby)