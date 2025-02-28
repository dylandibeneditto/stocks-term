from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Vertical, Horizontal
from textual.widget import Widget

from views.list.graph import StockListGraph
from stock import Stock
from theme import theme

class StockListItem(Widget):
    def __init__(self, ticker: str, index: int):
        super().__init__()
        self.ticker = ticker
        self.index = index
        self.id = f"t{self.index}"
        self.stock = Stock(ticker)

    def compose(self) -> ComposeResult:
        with Vertical(id="name"):
            with Horizontal():
                yield Label(self.ticker)
                yield Label(" ▲ " if float(self.stock.get_change()) > 0 else " ▼ ", id="indicator")
            yield Label(self.stock.get_name(), id="long-name")
        yield Label("", id="spacer")
        yield StockListGraph(self.stock)
        with Vertical(id="info"):
            yield Label(self.stock.get_price(), id="price")
            yield Label(self.stock.get_change(), id="delta")
            yield Label(self.stock.get_perc(), id="perc")

    def on_mount(self):
        pos = float(self.stock.get_change()) > 0
        col = theme["good" if pos else "bad"]
        self.query_one("#indicator").styles.color = col
        self.query_one("#delta").styles.background = col
        self.query_one("#perc").styles.background = col
        self.query_one("#long-name").styles.color = theme["ter"]

