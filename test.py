from stock import Stock

if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    stock = Stock(ticker)
    print(stock.get_todays_prices())
