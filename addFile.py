from bs4 import BeautifulSoup
import requests




url3060 = "https://neeed.comptoir.co/filtrationnage/rtx-3060/stockasc"
url3060ti = "https://neeed.comptoir.co/filtrationnage/rtx-3060-ti/stockasc"


def getParser(url):
    page = requests.get(url)
    parser = BeautifulSoup(page.content, 'html.parser')
    conv = str(parser)

    return conv


fichier = open('3060.txt','w')
fichier.write(getParser(url3060))
fichier.close()

fichier = open('3060ti.txt','w')
fichier.write(getParser(url3060ti))
fichier.close()



