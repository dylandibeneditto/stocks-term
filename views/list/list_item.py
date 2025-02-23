from rich.console import Console

c = Console()

def list_item_view(ticker: str, selected: bool) -> None:
    bg = "[#808080]" if selected else ""
    c.print(f"{bg}{ticker}")
