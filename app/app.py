from app.fetch_stocks.fetch_stocks import fetch_filtered_stocks

def run():
    """Main entry point for the paper trading app."""
    print("Running the Paper Trading App...")
    filtered_stocks = fetch_filtered_stocks()
    
    if filtered_stocks:
        print(f"\nFiltered Stocks: {filtered_stocks}")
    else:
        print("\nNo stocks matched the criteria today.")

if __name__ == "__main__":
    run()
