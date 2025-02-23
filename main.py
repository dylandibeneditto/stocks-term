import sys
from data_handler import *

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        # MARK: PORTFOLIO LISTING
        print("[display all portfolio stocks]")
    elif "-edit" in args:
        # MARK: EDIT LIST VIEW
        next = None
        try:
            next = args[args.index("-edit")+1]
            if next not in get_lists():
                add_list(next)
        except:
            pass

        if next:
            print(get_list(next))
        else:
            print(get_portfolio())
    elif "-graph" in args:
        # MARK: GRAPH VIEW
        print("[display graph of the first stock]")

        if len(args) == 1:
            # arg warning : not supplying ticker
            print("[you didnt supply a ticker, defaulting to top portfolio stock]")
        elif len(args) > 2:
            # arg warning : supplying too many tickers
            print("[graphing only supports one stock input]")
    elif "-list" in args:
        # MARK: STOCK WATCHLIST VIEW
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
    else:
        # MARK: CUSTOM ARG TICKERS LIST
        print("[display list of tickers]")


