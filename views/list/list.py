from textual.app import App, ComposeResult
from textual.events import Key
from textual.reactive import reactive
from textual.containers import Vertical
from textual.widgets import Static
from textual.binding import Binding
from views.list.list_item import StockListItem
from theme import theme
from math import ceil

class StockListView(App):
    CSS_PATH = "css/list.tcss"
    ENABLE_COMMAND_PALETTE = False

    page = reactive(0)

    def __init__(self, tickers: list[str]):
        super().__init__()
        self.tickers = tickers
        self.selected = 0
        self.page_size = 1
        self.stock_items = []

    def compose(self) -> ComposeResult:
        with Vertical():
            for i, ticker in enumerate(self.tickers):
                item = StockListItem(ticker, i)
                item.display = False
                self.stock_items.append(item)
                yield item
        yield Static(id="page-count")

    def on_mount(self):
        self.screen.styles.background = theme["bg"]
        self.page_size = max(self.size.height // 10, 1)
        self.update_pagination()

    def on_resize(self):
        self.page_size = max(self.size.height // 10, 1)
        self.update_pagination()

    def update_pagination(self):
        start = self.page * self.page_size
        end = start + self.page_size

        for i, item in enumerate(self.stock_items):
            item.display = start <= i < end

        self.query_one("#page-count").update(f"[{theme["text"].hex}]{self.page+1}[/] [{theme["ter"].hex}]/ {ceil(len(self.tickers)/self.page_size)}")

        self.selected = 0
        self.update_selection()

    def update_selection(self):
        start = self.page * self.page_size
        end = start + self.page_size
        visible_items = [item for item in self.stock_items[start:end]]

        for i, item in enumerate(visible_items):
            item.styles.background = theme["selected_bg"] if i == self.selected else theme["bg"]

    def __change_select(self, to: int):
        start = self.page * self.page_size
        end = start + self.page_size
        visible_items = [item for item in self.stock_items[start:end]]

        if 0 <= to < len(visible_items):
            visible_items[self.selected].styles.background = theme["bg"]
            self.selected = to
            visible_items[self.selected].styles.background = theme["selected_bg"]

    def on_key(self, event: Key):
        if event.key in ["up", "k"]:
            self.__change_select(max(self.selected - 1, 0))
        elif event.key in ["down", "j"]:
            self.__change_select(min(self.selected + 1, self.page_size - 1))
        elif event.key in ["left", "h"] and self.page > 0:
            self.page -= 1
            self.update_pagination()
        elif event.key in ["right", "l"] and self.page < (len(self.tickers) / self.page_size)-1:
            self.page += 1
            self.update_pagination()
        elif event.key == "q":
            self.exit()
