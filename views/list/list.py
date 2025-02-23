from rich.console import Console
from views.list.list_item import list_item_view
from utils.get_key import get_key


def list_view(tickers: list[str]) -> None:

    c = Console()
    c.set_alt_screen()

    select = 0
    running = True

    while running:

        for i, t in enumerate(tickers):
            list_item_view(t, select == i)

        key = get_key()
        if key == "q":
            running = False
            break
        elif key == "up":
            select = (select-1)%len(tickers)
        elif key == "down":
            select = (select+1)%len(tickers)

        c.clear()

    c.set_alt_screen(False)
