def max_profit(prices):
    if len(prices) == 0:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

prices = []
num_prices = int(input("Enter the number of prices: "))
for i in range(num_prices):
    price = int(input(f"Enter price {i + 1}: "))
    prices.append(price)

result = max_profit(prices)
print("Maximum profit:", result)