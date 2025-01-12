import yfinance as yf
import pandas as pd

def get_keltner_channel(stock, period=20, multiplier=2):
    """Calculate the Keltner Channel (Upper and Lower Bands) for a stock."""
    
    # Fetch stock data for the last 60 days (to account for ATR calculation)
    stock_data = yf.download(stock, period="6mo", interval="1d",progress=False)
    
    if stock_data.empty:
        raise ValueError(f"No data available for {stock}")

    # Calculate EMA (Middle Line)
    stock_data['EMA'] = stock_data['Close'].ewm(span=period, adjust=False).mean()

    # Calculate True Range components
    stock_data['High-Low'] = stock_data['High'] - stock_data['Low']
    stock_data['High-Close'] = (stock_data['High'] - stock_data['Close'].shift(1)).abs()
    stock_data['Low-Close'] = (stock_data['Low'] - stock_data['Close'].shift(1)).abs()

    # Calculate True Range (TR) and ATR
    stock_data['TR'] = stock_data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    stock_data['ATR'] = stock_data['TR'].rolling(window=period).mean()

    # Calculate Upper and Lower Bands
    stock_data['Upper Band'] = stock_data['EMA'] + (multiplier * stock_data['ATR'])
    stock_data['Lower Band'] = stock_data['EMA'] - (multiplier * stock_data['ATR'])

    # Get the latest bands
    latest_upper_band = float(stock_data['Upper Band'].iloc[-1])
    latest_lower_band = float(stock_data['Lower Band'].iloc[-1])

    return {
        "Upper Band": latest_upper_band,
        "Lower Band": latest_lower_band
    }