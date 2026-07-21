STOCK_PRICES = {
    "AAPL": 180,
    "AMZN": 185,
    "MSFT": 320,
    "GOOGL": 140,
}


def show_available_stocks():
    """Display all available stocks and their prices."""
    print("\n Available Stocks:")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price:.2f}")
    print("-" * 30)


def get_portfolio():
    """Collect stock names and quantities from the user."""
    portfolio = {}

    print("\nEnter your stocks (type 'done' when finished):")

    while True:
        symbol = input("  Stock symbol: ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            quantity = int(input(f"  Quantity of {symbol}: "))
            if quantity <= 0:
                print("  Quantity must be a positive number.")
                continue
        except ValueError:
            print("  Please enter a valid whole number.")
            continue

        # Add to portfolio (accumulate if same stock entered twice)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"  Added: {quantity} x {symbol} @ ${STOCK_PRICES[symbol]}")

    return portfolio


def calculate_investment(portfolio):
    """Calculate total investment value for each stock and overall."""
    results = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        results.append((symbol, quantity, price, value))

    return results, total


def display_results(results, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 50)
    print("         PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<8} {'Qty':>5} {'Price':>10} {'Value':>12}")
    print("-" * 50)

    for symbol, quantity, price, value in results:
        print(f"{symbol:<8} {quantity:>5} ${price:>9.2f} ${value:>11.2f}")

    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':>35} ${total:>11.2f}")
    print("=" * 50)


def run_tracker():
    """Main function to run the stock portfolio tracker."""
    print("=" * 50)
    print("     STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    results, total = calculate_investment(portfolio)
    display_results(results, total)

    print("\nThank you for using Stock Portfolio Tracker!")


# Entry point
run_tracker()