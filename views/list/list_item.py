from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Vertical
from textual.widget import Widget

from views.list.graph import StockListGraph
from theme import theme

import yfinance as yf

class StockListItem(Widget):
    def __init__(self, ticker: str, index: int):
        super().__init__()
        self.ticker = ticker
        self.index = index
        self.data = yf.Ticker(self.ticker)
        self.today = self.data.history(period="2d")
        self.id = f"t{self.index}"

    def compose(self) -> ComposeResult:
        with Vertical(id="name"):
            yield Label(self.ticker)
            yield Label(self.data.info["longName"], id="long-name")
        yield Label("", id="spacer")
        yield StockListGraph(self.today)
        with Vertical(id="info"):
            yield Label(self.get_price(), id="price")
            yield Label(self.get_delta(), id="delta")
            yield Label(self.get_perc(), id="perc")

    def on_mount(self):
        pos = float(self.get_delta()) > 0
        col = theme["good" if pos else "bad"]
        self.query_one("#delta").styles.background = col
        self.query_one("#perc").styles.background = col
        self.query_one("#long-name").styles.color = theme["ter"]

    def get_price(self) -> str:
        latest_price = self.today["Close"].iloc[-1]
        return "{:.2f}".format(latest_price)

    def get_delta(self) -> str:
        market_open_price = self.today["Close"].iloc[-2]
        latest_price = self.today["Close"].iloc[-1]
        
        return "{:.2f}".format(latest_price - market_open_price)

    def get_perc(self) -> str:
        market_open_price = self.today["Close"].iloc[-2]
        latest_price = self.today["Close"].iloc[-1]
        
        percent_change = 100 * (latest_price / market_open_price - 1)
        return "{:.2f}%".format(percent_change)
