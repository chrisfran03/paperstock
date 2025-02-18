import requests
import yfinance as yf

# Filtering criteria constants
MIN_PRICE = 15
MIN_VOLUME = 500_000
MIN_AVG_VOLUME = 500_000
MIN_MARKET_CAP = 1_000_000_000

NASDAQ_URL = "https://api.nasdaq.com/api/quote/list-type/FIFTYTWOWEEKHILOW?&queryString=exchange%3Dq%7Cstatus%3DHi&limit=99999&sortColumn=symbol&sortOrder=ASC"


def get_json_data(url):
    """Fetches JSON data from a provided URL."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def filter_by_price(json_data):
    """Filters tickers based on the minimum price."""
    rows = json_data.get("data", {}).get("table", {}).get("rows", [])
    return [
        stock['symbol']
        for stock in rows
        if float(stock['lastsale'].replace('$', '').replace(',', '')) >= MIN_PRICE
    ]


def filter_by_volume_and_market_cap(tickers):
    """Filters stocks based on volume and market cap using yfinance."""
    filtered_tickers = []
    for ticker in tickers:
        try:
            stock_info = yf.Ticker(ticker).info
            share_volume = stock_info.get("regularMarketVolume", 0)
            avg_volume = stock_info.get("averageVolume", 0)
            market_cap = stock_info.get("marketCap", 0)

            if (
                share_volume >= MIN_VOLUME and
                avg_volume >= MIN_AVG_VOLUME and
                market_cap >= MIN_MARKET_CAP
            ):
                filtered_tickers.append(ticker)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return filtered_tickers


def fetch_filtered_stocks():
    """Main function to fetch and filter stocks."""
    json_data = get_json_data(NASDAQ_URL)
    price_filtered_tickers = filter_by_price(json_data)
    return filter_by_volume_and_market_cap(price_filtered_tickers)
