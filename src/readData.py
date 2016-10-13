from yahoo_finance import Share
import matplotlib.pyplot as plt
import pandas as pd
import os.path


class Stock:
    def __init__(self):
        self.historical = []

    def get_quote(self, symbol):
        if not os.path.exists("../stockdata/"+symbol+".csv"):
            my_share = Share(symbol)
            pd.DataFrame(my_share.get_historical('1993-10-02','2016-10-12')).to_csv("../stockdata/"+symbol+".csv")

        self.historical = pd.read_csv("../stockdata/"+symbol+".csv")

    def plot(self):
        self.historical['Adj_Close'].plot(grid=True)
        plt.show()

myStock = Stock()
myStock.get_quote('AAPL')
myStock.plot()