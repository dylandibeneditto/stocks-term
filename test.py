from stock import Stock

if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    stock = Stock(ticker)
    print(stock.get_name())
    print(stock.get_price())
    print(stock.get_perc())
    print(stock.get_change())
