import yfinance as yf

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.yTicker = yf.Ticker(ticker)
        self.today = None

    def __update_today(self):
        self.today = self.yTicker.history(period="2d")

    def get_name(self) -> str:
        return self.yTicker.info.get("longName", "Unknown")

    def get_price(self) -> str:
        self.__update_today()
        if self.today is not None and not self.today.empty:
            latest_price = self.today["Close"].iloc[-1]
            return "{:.2f}".format(latest_price)
        return "N/A"

    def get_change(self) -> str:
        self.__update_today()
        if self.today is not None and len(self.today) > 1:
            market_open_price = self.today["Close"].iloc[-2]
            latest_price = self.today["Close"].iloc[-1]
            return "{:.2f}".format(latest_price - market_open_price)
        return "N/A"

    def get_perc(self) -> str:
        self.__update_today()
        if self.today is not None and len(self.today) > 1:
            market_open_price = self.today["Close"].iloc[-2]
            latest_price = self.today["Close"].iloc[-1]
            percent_change = 100 * (latest_price / market_open_price - 1)
            return "{:.2f}%".format(percent_change)
        return "N/A"

    def get_todays_prices(self) -> list:
        return list(self.yTicker.history(period="1d", interval="15m")['Close'])
