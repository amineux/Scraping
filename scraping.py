
# Obtiens les prix des bourses de google finance
# Author: Amine Atar

import urllib
from bs4 import BeautifulSoup

tickerFile = open("ticker.txt")
tickerList = tickerFile.read()
tickerArr = tickerList.split("\n")
BASE_URL = "https://www.google.com/finance?q=NASDAQ%3A"

def get_stock_price():
    try:
        print "Tenter de rassembler les données de prix pour les sumbols ticker \n"
        for ticker in tickerArr:
            try:
                htmlfile = urllib.urlopen(BASE_URL + ticker)
                htmltext = htmlfile.read()
                
                soup = BeautifulSoup(htmltext, 'html.parser')
                market_data = soup.find('span', attrs={'class' : 'pr'})
                price_fluctuation = soup.find('span', attrs={'class' : 'chg'})
                stock_price = market_data.text.strip()
                if price_fluctuation is None:
                    print ticker, ": $", stock_price
                else:
                    print ticker, ": $", stock_price, "Osillation du prix: $", price_fluctuation.text.strip()
            except:
                print("Prix de Stock non trouvé " + ticker)
except Exception, e:
    print str(e)
    print 'Erreur trouvé pour otenir le prix de stock . Vérifier que le symbol ticker  est bon svp'

get_stock_price()
