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
        prices: list = self.stock.get_todays_prices()
        (max_price, min_price) = (max(prices), min(prices))
        (width, height) = (36, 8)

        def compress_prices() -> list[float]:
            if width >= len(prices) or width <= 0:
                return prices

            bucket_size = len(prices) / width
            compressed = []

            for i in range(width):
                start = int(i * bucket_size)
                end = int((i + 1) * bucket_size)
                segment = prices[start:end]

                if segment:
                    compressed.append(sum(segment) / len(segment))

            return compressed

        def normalize_graph() -> list[int]:
            compressed = compress_prices()
            result = [0 for i in compressed]
            for (i, c) in enumerate(compressed):
                result[i] = round((c-min_price)/(max_price-min_price)*height)

            return result

        normalized = normalize_graph()
        open = round((self.stock.yest_close()-min_price)/(max_price-min_price)*height)
        (r,g,b) = theme["good"].rgb if float(self.stock.get_change()) > 0 else theme["bad"].rgb
        text_color = f"rgb({r+30}, {g+30}, {b+30})"
        for y in range(height):
            color = f"rgba({r}, {g}, {b}, {(height-y)/height})"
            for (n, x) in zip(normalized, range(width)):
                char = " "

                if x % 2 == 0 and y == open:
                    char = "-"
                if height - y == n:
                    if y == height:
                        char = "_"
                    else:
                        char = "▔"

                if height-y <= n:
                    result += f"[{text_color} on {color}]{char}[/]"
                else:
                    result += f"[{text_color}]{char}[/]"

            result += "\n"

        return result
