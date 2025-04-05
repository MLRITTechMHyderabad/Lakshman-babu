import numpy as np

# random stock prices (30 days, 5 companies)
np.random.seed(42)  
stock_prices = np.random.uniform(100, 500, size=(30, 5)).round(2)

#average stock price for each company
average_prices = np.mean(stock_prices, axis=0)

#highest stock price and its location (day, company)
max_price = np.max(stock_prices)
max_index = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)  #np.argmax() -> Finds the index of that max price, but as a flat index.
max_day = max_index[0]  # row                                              #np.unravel_index( , shape) -> Converts that flat index into:(day, company) format using array's shape (30, 5).
max_company = max_index[1]  # column

# Normalize prices to [0, 1]
min_val = np.min(stock_prices)
max_val = np.max(stock_prices)
normalized_prices = (stock_prices - min_val) / (max_val - min_val)

#Flag risky investment days (any price < 200)
risky_days_mask = np.any(stock_prices < 200, axis=1)
risky_days = np.where(risky_days_mask)[0]  # Get indices of risky days

print("Average stock prices per company over 30 days:")
print(average_prices.round(2))

print(f"\nHighest price recorded: ₹{max_price} on Day {max_day}, Company {max_company}")

print("\nNormalized Stock Prices (0 to 1):")
print(np.round(normalized_prices, 2))

print("\nRisky Investment Days (price < ₹200 in any company):")
print(risky_days)
