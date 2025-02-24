from textual.app import App, ComposeResult
from textual.events import Key
from views.list.list_item import StockListItem

from theme import theme

class StockListView(App):
    CSS_PATH = "css/list.tcss"
    def __init__(self, tickers: list[str]):
        super().__init__()
        self.tickers = tickers
        self.selected = 0

    def compose(self) -> ComposeResult:
        for (i,t) in enumerate(self.tickers):
            yield StockListItem(t, i)

    def on_mount(self):
        self.screen.styles.background = theme["bg"]
        self.query_one(f"#t0").styles.background = theme["selected_bg"]

    def on_key(self, event: Key):

        el1 = self.query_one(f"#t{self.selected}")
        el1.styles.background = theme["bg"]

        if event.key in ["up", "k"]:
            self.selected = max(self.selected-1, 0)
        elif event.key in ["down", "j"]:
            self.selected = min(self.selected+1, len(self.tickers)-1)
        elif event.key == "q":
            self.exit()

        el2 = self.query_one(f"#t{self.selected}")
        el2.styles.background = theme["selected_bg"]
