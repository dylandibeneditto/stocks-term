from stock import Stock
from views.list.graph import StockListGraph

if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    stock = Stock(ticker)
    print(stock.get_sector())
    print(stock.get_industry())
    print(stock.get_description())
