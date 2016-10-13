from yahoo_finance import Share
import matplotlib.pyplot as plt
import pandas as pd
import os.path
import datetime


class Stock:
    def __init__(self):
        self.historical = pd.DataFrame()

    def get_quote(self, symbol, start_date='2000-01-01', end_date=datetime.datetime.now().strftime("%Y-%m-%d")):
        if not os.path.exists("../stockdata/"+symbol+".csv"):
            my_share = Share(symbol)
            temp = pd.DataFrame(my_share.get_historical(start_date, end_date))
            if temp.size == 0:
                return False
            else:
                temp.to_csv("../stockdata/"+symbol+".csv")

        temp = pd.read_csv("../stockdata/"+symbol+".csv", parse_dates=True,
                                      index_col="Date", usecols=["Date","Adj_Close"])
        temp.rename(columns={"Adj_Close": symbol}, inplace=True)

        if self.historical.size == 0:
            self.historical = temp
        else:
            self.historical = self.historical.join(other=temp, how='outer')
            self.historical.fillna(method="ffill", inplace=True)
            self.historical.fillna(method="bfill", inplace=True)
        return True

    def plot(self, symbols=[]):
        if not symbols:
            self.historical.plot()
        else:
            self.historical[symbols].plot()
        plt.show()


def test_run():
    myStock = Stock()
    myStock.get_quote(symbol='FB')
    myStock.get_quote(symbol='QCOM')
    myStock.get_quote(symbol='GOOGL')
    myStock.get_quote(symbol='VMRI')
    symbols = ['VMRI']
    myStock.plot(symbols)

if __name__ == "__main__":
    test_run()