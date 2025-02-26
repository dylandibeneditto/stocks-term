from textual.widget import Widget
from textual.widgets import Label
from textual.app import ComposeResult

class StockListGraph(Widget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.id = "list-graph"

    def compose(self) -> ComposeResult:
        yield Label(str(len(self.data)))
