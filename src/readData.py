from yahoo_finance import Share
import json

class Quotes:
    def main(self, symbol):
        myShare = Share(symbol)
        historical = myShare.get_historical('1993-10-02','2016-10-12')
        for i in range (len(historical)):
            print (historical[i],"\n")

Quotes().main('AAPL')