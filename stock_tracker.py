# Stock Portfolio Tracker
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}
total_investment = 0
print("===== Stock Portfolio Tracker =====")
number_of_stocks = int(input("How many stocks do you want to enter? "))
for i in range(number_of_stocks):
    stock_name = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        print("Stock:", stock_name)
        print("Price: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)
        print()
    else:
        print("Sorry, this stock is not available.")
        print()
print("==============================")
print("Total Investment: $", total_investment)
print("==============================")
