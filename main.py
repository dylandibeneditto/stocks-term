import sys
from data_handler import *
from views.list.list import StockListView
from rich.console import Console
from rich.panel import Panel
import yfinance as yf
from theme import theme

c = Console()

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:

        # NOTE: PORTFOLIO LISTING
        StockListView(get_portfolio()).run()

    elif "-e" in args or "-edit" in args:

        # NOTE: EDIT LIST VIEW
        next = None
        try:
            next = args[args.index("-edit")+1]
            if next not in get_lists():
                add_list(next)
        except:
            pass

        if next:

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
        next = None
        try:
            next = args[args.index("-l" if "-l" in args else "-list")+1]
            if next not in get_lists():
                next = None
        except:
            pass

        if next:

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
 \tstock\t\t\t\t[{theme["sec"]}]displays your portfolio watchlist[/{theme["sec"]}]
 
 [b]commands for showing stocks by ticker:[/b]
 \tstock (ticker)\t\t\t[{theme["sec"]}]will display a detail view of a single stock[/{theme["sec"]}]
 \tstock (ticker) (ticker) ...\t[{theme["sec"]}]will display a list view of each stock provided[/{theme["sec"]}]
 
 [i {theme["ter"]}]example of one stock\t\t\t'stock aapl'[/i {theme["ter"]}]
 [i {theme["ter"]}]example of multiple stocks\t\t'stock aapl msft ^dji'[/i {theme["ter"]}]
 
 [b]editing watchlists:[/b]
 \tstock (-e | -edit) (watchlist)\t[{theme["sec"]}]will create watchlist if it doesn't exist, and allow for adding a removing stocks from it[/{theme["sec"]}]
 
 [i {theme["ter"]}]example of editing a watchlist:\t'stock -e tech'[/i {theme["ter"]}]
 
 [b]opening watchlists:[/b]
 \tstock (-l | -list)\t\t[{theme["sec"]}]will display the name of every watchlist[/{theme["sec"]}]
 \tstock (-l | -list) (watchlist)\t[{theme["sec"]}]will open a list view of the watchlist[/{theme["sec"]}]
 
 [i {theme["ter"]}]example of opening a watchlist\t'stock tech'[/i {theme["ter"]}]
 
 [b]getting the graph view of a ticker:[/b]
 \tstock (-g | -graph) (ticker)\t[{theme["sec"]}]will open the provided ticker name, defaults to top portfolio stock if (ticker) argument is incorrect[/{theme["sec"]}]
 
 [i {theme["ter"]}]example of getting the graph view\t'stock -g aapl'[/i {theme["ter"]}]
        """, title="stock -help", title_align="left", style=f"{theme["text"]} on {theme["bg"]}"))

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


