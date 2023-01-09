from bs4 import BeautifulSoup
import time
import requests
import webbrowser
from datetime import datetime


class Bot:

    def __init__(self, url, nom):
        self.url = url
        self.nom = nom

    def getParser(self, url):
        page = requests.get(url)
        self.parser = BeautifulSoup(page.content, 'html.parser')
        return self.parser

    def getListPrix(self, parser):

        self.listPrix = []
        self.prix = parser.find_all(class_="etiprix")

        for i in range(24):
            chainei = str(self.prix[i])
            soupi = BeautifulSoup(chainei, 'html.parser')
            #creer un parser de la valeur de rand i de la liste self.prix

            prix = soupi.find(class_="etiprix").text
            # enleve les balises

            prix = prix.replace(',', '.')
            prix = prix.replace('€', '')
            # enleve exep

            prix = prix.strip()
            # enleve espaces

            prixFinal = float(prix)
            self.listPrix.append(prixFinal)

        return self.listPrix



    def getListUrl(self, parser):
        self.listUrl = []
        self.url = parser.find_all(class_="neeed-cercle")
        for i in range(24):
            chainei = str(self.url[i])
            soupi = BeautifulSoup(chainei, 'html.parser')
            url = soupi.find().attrs['href']
            url = str(url)
            url = "https://neeed.comptoir.co/" + url
            self.listUrl.append(url)

        return self.listUrl


    def getListStock(self, parser):
        self.listStock = []
        self.url = parser.find_all(class_="btn btn-sp")
        for i in range(24):
            chainei = str(self.url[i])
            soupi = BeautifulSoup(chainei, 'html.parser')
            stock = soupi.find().attrs['data-text']
            stock = str(stock)

            self.listStock.append(stock)

        return self.listStock


    def verif(self, parser):

        if self.nom == "rtx-3060":
            valeurMin = 1000


        elif self.nom == "rtx-3060-ti":
            valeurMin = 600


        indice = 0

        v = self.getListPrix(parser)
        u = 0
        for i in self.getListStock(parser):
            if i == "EN STOCK!":
                if v[u] < valeurMin:
                    indice = u
                    return indice


            u = u + 1
            indice = 666

        return indice

    def ouvrir(self, parser, indice):
        listurl = self.getListUrl(parser)
        url = listurl[indice]

        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)




Bot1 = Bot("https://neeed.comptoir.co/filtrationnage/rtx-3060/stockasc", "rtx-3060")

Bot2 = Bot("https://neeed.comptoir.co/filtrationnage/rtx-3060-ti/stockasc", "rtx-3060-ti")

parserBot1 = Bot1.getParser(url="https://neeed.comptoir.co/filtrationnage/rtx-3060/stockasc")
parserBot2 = Bot2.getParser(url="https://neeed.comptoir.co/filtrationnage/rtx-3060-ti/stockasc")


a = Bot1.verif(parserBot1)
b = Bot2.verif(parserBot2)



while a == 666 and b == 666:
    time.sleep(60)

    parserBot1 = Bot1.getParser(url="https://neeed.comptoir.co/filtrationnage/rtx-3060/stockasc")
    parserBot2 = Bot2.getParser(url="https://neeed.comptoir.co/filtrationnage/rtx-3060-ti/stockasc")
    a = Bot1.verif(parserBot1)
    b = Bot1.verif(parserBot1)


if b < 600:
    Bot2.ouvrir(parserBot2, b)



else:
    Bot1.ouvrir(parserBot1, a)

print(datetime.now())































