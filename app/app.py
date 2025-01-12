from app.fetch_stocks.fetch_stocks import fetch_filtered_stocks
from app.indicators.moving_averages import get_moving_average
import yfinance as yf
def run():
    # """Main entry point for the paper trading app."""
    # print("Running the Paper Trading App...")
    # filtered_stocks = fetch_filtered_stocks()
    
    # if filtered_stocks:
    #     print(f"\nFiltered Stocks: {filtered_stocks}")
    # else:
    #     print("\nNo stocks matched the criteria today.")

    ticker = "AAPL"
    twenty_DMA = get_moving_average(ticker, 20)
    fifty_DMA = get_moving_average(ticker, 50)
    two_hundred_DMA = get_moving_average(ticker, 200)

    print(f"Twenty DMA: {twenty_DMA}")
    print(f"Fifty DMA: {fifty_DMA}")
    print(f"Two Hundred DMA: {two_hundred_DMA}")

   

if __name__ == "__main__":
    run()
