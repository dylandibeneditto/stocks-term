import yfinance as yf

def get_stock_delta(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period='2d')  # Fetch last 2 days of data
    
    if len(data) < 2:
        print("Not enough data to calculate delta.")
        return None
    
    prev_close = data.iloc[-2]['Close']  # Previous day's close
    last_price = data.iloc[-1]['Close']  # Most recent close
    
    delta = last_price - prev_close
    percent_change = (delta / prev_close) * 100
    
    return last_price, delta, percent_change

def display_stock_info(ticker: str):
    result = get_stock_delta(ticker)
    if result:
        last_price, delta, percent_change = result
        delta_sign = "▲" if delta > 0 else "▼"
        print(f"{ticker.upper()} - ${last_price:.2f} ({delta_sign}{abs(delta):.2f}, {delta_sign}{abs(percent_change):.2f}%)")

if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    display_stock_info(ticker)
