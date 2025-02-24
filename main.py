import sys
from data_handler import *
from views.list.list import StockListView

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
            next = args[args.index("-edit")+1]
            if next not in get_lists():
                next = None
        except:
            pass

        if next:

            # list view of stocks
            print(f"[list view of {next} list]")

        else:

            # list of all watchlists
            print("[list of watchlists]")

    elif "-h" in args or "-help" in args:

        # NOTE: HELP VIEW
        print("[help]")

    else:

        # NOTE: CUSTOM ARG TICKERS LIST
        print("[display list of tickers]")


