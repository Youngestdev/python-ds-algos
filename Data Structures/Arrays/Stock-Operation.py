def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit
