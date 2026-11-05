import requests
import json


url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'



if __name__ == "__main__":
    responce = requests.get(url)
    if responce.status_code == 200:
        print(responce.content)
