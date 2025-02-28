import yfinance as yf

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.yTicker = yf.Ticker(ticker)
        self.today = None

    def __update_today(self):
        self.today = self.yTicker.history(period="2d")

    def yest_close(self):
        self.__update_today()
        open_price = None
        if self.today is not None and not self.today.empty:
            open_price = self.today["Close"].iloc[-2]
        return open_price

    def today_close(self):
        self.__update_today()
        latest_price = None
        if self.today is not None and not self.today.empty:
            latest_price = self.today["Close"].iloc[-1]
        return latest_price

    def get_name(self) -> str:
        return self.yTicker.info.get("longName", "Unknown")

    def get_price(self) -> str:
        return "{:.2f}".format(self.today_close())

    def get_change(self) -> str:
        today = self.today_close()
        yes = self.yest_close()
        if today and yes:
            return "{:.2f}".format(today - yes)
        return "N/A"

    def get_perc(self) -> str:
        today = self.today_close()
        yes = self.yest_close()
        if today and yes:
            percent_change = 100 * (today / yes - 1)
            return "{:.2f}%".format(percent_change)
        return "N/A"

    def get_todays_prices(self) -> list:
        day = list(self.yTicker.history(period="1d", interval="1m")['Close'])
        return day
        
