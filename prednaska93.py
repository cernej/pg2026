from unittest.mock import MagicMock


class Server:
    def __init__(self):
        pass
    
    def send(self, zprava):
        print(f"Odesilam zpravu '{zprava}' pomoci metody send()")
    
    def log(self, text):
        pass


def posli_email(server, zprava):
    server.send(zprava)
    server.log("neco se stalo")


def test_posli_email():
    server = MagicMock()
    posli_email(server, "Ahoj!")
    server.send.assert_called_once_with("Ahoj!")
    server.log.assert_called_once_with("neco se stalo")


if __name__ == "__main__":
    server = Server()
    posli_email(server, "Ahoj!")