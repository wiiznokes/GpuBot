from bs4 import BeautifulSoup
import time
import requests
import webbrowser
from datetime import datetime


class Bot:

    def __init__(self, url, prixVoulu):
        self.url = url
        self.prixVoulu = prixVoulu

    def getParser(self):
        page = requests.get(self.url)
        self.parser = BeautifulSoup(page.content, 'html.parser')
        return self.parser

    def getPrix(self):
        self.parser = Bot.getParser(self)
        cartePrice = self.parser.find(class_="font-weight-bold text-secondary w-100 d-block h1 mb-2").text
        cartePrice1 = cartePrice.rstrip(cartePrice[-1])
        self.prix = int(cartePrice1)

        return self.prix

    def getNom(self):
        self.parser = Bot.getParser(self)
        self.Nom = self.parser.find(class_="font-weight-bold h4 item-name").text
        return self.Nom

    def getUrlProduit(self):
        self.parser = Bot.getParser(self)
        self.urlProduit = self.parser.find("a", {"class": "no-link-style tracked-product-click"}).attrs['href']

        return self.urlProduit

    def ouvrir(self):
        self.urlProduit = Bot.getUrlProduit(self)
        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(self.urlProduit)



Bot1 = Bot("https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?onlyInStock=true&fv_gpu.chip=AMD%20RX%205700%20XT&fv_gpu.chip=AMD%20RX%206700%20XT&fv_gpu.chip=AMD%20RX%206800&fv_gpu.chip=AMD%20RX%206800%20XT&fv_gpu.chip=AMD%20RX%206900%20XT&fv_gpu.chip=NVIDIA%20RTX%202070%20SUPER&fv_gpu.chip=NVIDIA%20RTX%202080&fv_gpu.chip=NVIDIA%20RTX%202080%20SUPER&fv_gpu.chip=NVIDIA%20RTX%202080%20TI&fv_gpu.chip=NVIDIA%20RTX%203060%20TI&fv_gpu.chip=NVIDIA%20RTX%203070&fv_gpu.chip=NVIDIA%20RTX%203070%20TI&fv_gpu.chip=NVIDIA%20RTX%203080&fv_gpu.chip=NVIDIA%20RTX%203080%20TI&fv_gpu.chip=NVIDIA%20RTX%203090",
           50)

Bot2 = Bot("https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?onlyInStock=true&fv_gpu.chip=AMD%20RX%205600%20XT&fv_gpu.chip=AMD%20RX%205700&fv_gpu.chip=NVIDIA%20GTX%201060&fv_gpu.chip=NVIDIA%20GTX%201660&fv_gpu.chip=NVIDIA%20GTX%201660%20SUPER&fv_gpu.chip=NVIDIA%20GTX%201660%20TI&fv_gpu.chip=NVIDIA%20RTX%202060&fv_gpu.chip=NVIDIA%20RTX%202060%20SUPER&fv_gpu.chip=NVIDIA%20RTX%202070",
           150)
def bool(a, b):
    if a == 1 and b == 1:
        return 1
    elif a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 1
    elif a == 0 and b == 0:
        return 0

a = Bot1.getPrix() < Bot1.prixVoulu
b = Bot2.getPrix() < Bot2.prixVoulu
c = bool(a, b)


while c == 0:
    a = Bot1.getPrix() < Bot1.prixVoulu
    b = Bot2.getPrix() < Bot2.prixVoulu
    c = bool(a, b)

    time.sleep(10)

if a == 1:
    Bot1.ouvrir()
else:
    Bot2.ouvrir()


print(str(datetime.now()))