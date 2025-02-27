import yfinance as yf

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.yTicker = yf.Ticker(ticker)
