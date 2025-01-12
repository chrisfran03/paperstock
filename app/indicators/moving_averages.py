import yfinance as yf
import datetime as dt

def get_date_x_days_before(date_string, num_days_before):
    date_object = dt.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date_object - dt.timedelta(days=num_days_before)
    new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string

def get_moving_average(stock, period):
    """Fetches the Simple Moving Average (SMA) for a given stock and period."""
    end_date = dt.date.today().strftime("%Y-%m-%d")
    
    start_date = get_date_x_days_before(end_date, period*2)

    # Get a few days before the start date to accommodate the period size
    stock_data = yf.download(stock, start=start_date, end=end_date, progress=False)
    
    # Calculate the SMA
    stock_data["SMA"] = stock_data["Close"].rolling(window=period).mean()

    # Return the latest SMA value
    return stock_data["SMA"].iloc[-1]