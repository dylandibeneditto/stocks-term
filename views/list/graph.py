from textual.widget import Widget
from textual.widgets import Static
from textual.app import ComposeResult

from theme import theme

class StockListGraph(Widget):
    def __init__(self, stock):
        super().__init__()
        self.stock = stock
        self.id = "list-graph"

    def compose(self) -> ComposeResult:
        yield Static(self.get_graph())

    def get_graph(self) -> str:
        result = """"""
        for y in range(8):
            (r,g,b) = theme["good"].rgb if float(self.stock.get_change()) > 0 else theme["bad"].rgb
            text_color = f"rgb({r+100}, {g+100}, {b+100})"
            color = f"rgba({r}, {g}, {b}, {(7-y)/8})"
            for x in range(20):
                char = " "
                if x % 2 == 0 and y == 0:
                    char = "-"
                result += f"[{text_color} on {color}]{char}[/]"
            result += "\n"

        return result
