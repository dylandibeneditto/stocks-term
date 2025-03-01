import sys
from data_handler import *
from views.list.list import StockListView
from rich.console import Console
from rich.panel import Panel
import yfinance as yf
from theme import theme, themes

c = Console()

def next_arg(args, short: str, long: str):
    next = None
    try:
        next = args[args.index(short if short in args else long)+1]
    except:
        pass
    return next

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:

        # NOTE: PORTFOLIO LISTING
        StockListView(get_portfolio()).run()

    elif "-e" in args or "-edit" in args:

        # NOTE: EDIT LIST VIEW
        next = next_arg(args, "-e", "-edit")

        if next and next in get_lists():

            # edit list
            print(get_list(next))

        else:

            # edit portfolio
            print(get_portfolio())


    elif "-g" in args or "-graph" in args:

        # NOTE: GRAPH VIEW
        print("[display graph of the first stock]")

        if len(args) == 1:
            # arg warning : not supplying ticker
            print("[you didnt supply a ticker, defaulting to top portfolio stock]")
        elif len(args) > 2:
            # arg warning : supplying too many tickers
            print("[graphing only supports one stock input]")

    elif "-l" in args or "-list" in args:

        # NOTE: STOCK WATCHLIST VIEW
        next = next_arg(args, "-l", "-list")

        if next and next in get_lists():

            # list view of stocks
            StockListView(get_list(next)).run()

        else:

            # list of all watchlists
            # TODO: refactor this mess
            c.print("\n".join([f"[{theme["text"]} on {theme["selected_bg"] if j % 2 == 0 else theme["bg"]}]{i}{' ' * (c.width-len(i)-len(str(t))-7)}{len(t)} stocks" for j, (i, t) in enumerate(get_lists().items())]))

    elif "-h" in args or "-help" in args:

        # NOTE: HELP VIEW
        c.print(Panel(f"""
 [b]displaying your portfolio:[/b]
 \tstock\t\t\t\t[{theme["sec"].hex}]displays your portfolio watchlist[/{theme["sec"].hex}]
 
 [b]commands for showing stocks by ticker:[/b]
 \tstock (ticker)\t\t\t[{theme["sec"].hex}]will display a detail view of a single stock[/{theme["sec"].hex}]
 \tstock (ticker) (ticker) ...\t[{theme["sec"].hex}]will display a list view of each stock provided[/{theme["sec"].hex}]
 
 [i {theme["ter"].hex}]example of one stock\t\t\t'stock aapl'[/i {theme["ter"].hex}]
 [i {theme["ter"].hex}]example of multiple stocks\t\t'stock aapl msft ^dji'[/i {theme["ter"].hex}]
 
 [b]editing watchlists:[/b]
 \tstock (-e | -edit) (watchlist)\t[{theme["sec"].hex}]will create watchlist if it doesn't exist, and allow for adding a removing stocks from it[/{theme["sec"].hex}]
 
 [i {theme["ter"].hex}]example of editing a watchlist:\t'stock -e tech'[/i {theme["ter"].hex}]
 
 [b]opening watchlists:[/b]
 \tstock (-l | -list)\t\t[{theme["sec"].hex}]will display the name of every watchlist[/{theme["sec"].hex}]
 \tstock (-l | -list) (watchlist)\t[{theme["sec"].hex}]will open a list view of the watchlist[/{theme["sec"].hex}]
 
 [i {theme["ter"].hex}]example of opening a watchlist\t'stock tech'[/i {theme["ter"].hex}]
 
 [b]getting the graph view of a ticker:[/b]
 \tstock (-g | -graph) (ticker)\t[{theme["sec"].hex}]will open the provided ticker name, defaults to top portfolio stock if (ticker) argument is incorrect[/{theme["sec"].hex}]
 
 [i {theme["ter"].hex}]example of getting the graph view\t'stock -g aapl'[/i {theme["ter"].hex}]
        """, title="stock -help", title_align="left", style=f"{theme["text"].hex} on {theme["bg"].hex}"))

    elif "-s" in args or "-settings" in args:

        # NOTE: THEME SET VIEW
        next = next_arg(args, "-s", "-settings")

        if next and next in themes:
            set_theme(next)
            c.print(f"set theme to {next}")
        else:
            c.print(f"unknown theme {next}")
    else:

        # NOTE: CUSTOM ARG TICKERS LIST
        print("[Loading...]")

        stocks = []
        for i in args:
            try:
                t = yf.Ticker(i)
                info = t.info
                if info and isinstance(info, dict) and "longName" in info:
                    stocks.append(i.upper())
            except Exception as e:
                print(f"Error fetching data for {i}: {e}")

        if stocks:
            StockListView(stocks).run()
        else:
            print("No tickers provided were valid. Type \"stock -help\" for help.")


