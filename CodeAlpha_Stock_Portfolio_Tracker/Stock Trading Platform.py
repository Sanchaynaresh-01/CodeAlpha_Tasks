import yfinance as yf
import datetime

class StockPortfolioTracker:
    def init(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity, purchase_date):
        """Adds a stock to the portfolio."""
        if ticker not in self.portfolio:
            self.portfolio[ticker] = {
                "quantity": quantity,
                "purchase_date": purchase_date,
                "purchase_price": self.get_stock_price(ticker, purchase_date)
            }
            print(f"Added {quantity} shares of {ticker} to your portfolio.")
        else:
            print(f"You already have {ticker} in your portfolio.")

    def remove_stock(self, ticker):
        """Removes a stock from the portfolio."""
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from your portfolio.")
        else:
            print(f"You don't have {ticker} in your portfolio.")

    def track_performance(self):
        """Tracks and displays the performance of each stock in the portfolio."""
        today = datetime.date.today()
        print("\nPortfolio Performance:")
        for ticker, data in self.portfolio.items():
            current_price = self.get_stock_price(ticker, today)
            total_cost = int(data["quantity"]) * int(data["purchase_price"])
            current_value = data["quantity"] * current_price
            gain_loss = current_value - total_cost
            gain_loss_percentage = (gain_loss / total_cost) * 100
            print(f"{ticker}:")
            print(f"  Purchase Date: {data['purchase_date'].strftime('%Y-%m-%d')}")
            print(f"  Purchase Price: ${data['purchase_price']:.2f}")
            print(f"  Current Price: ${current_price:.2f}")
            print(f"  Total Cost: ${total_cost:.2f}")
            print(f"  Current Value: ${current_value:.2f}")
            print(f"  Gain/Loss: ${gain_loss:.2f} ({gain_loss_percentage:.2f}%)")

    def get_stock_price(self, ticker, date):
        """Fetches the stock price for a given ticker and date."""
        try:
            stock = yf.Ticker(ticker)
            history = stock.history(start=date, end=date)
            return history["Close"][0]
        except Exception as e:
            print(f"Error fetching stock price for {ticker}: {e}")
            return None

def main():
    portfolio_tracker = StockPortfolioTracker()

    while True:
        print("\nStock Portfolio Tracker:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter ticker symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_date_str = input("Enter purchase date (YYYY-MM-DD): ")
            purchase_date = datetime.datetime.strptime(purchase_date_str, "%Y-%m-%d").date()
            portfolio_tracker.add_stock(ticker, quantity, purchase_date)
        elif choice == "2":
            ticker = input("Enter ticker symbol to remove: ").upper()
            portfolio_tracker.remove_stock(ticker)
        elif choice == "3":
            portfolio_tracker.track_performance()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if name == "main":
    main()