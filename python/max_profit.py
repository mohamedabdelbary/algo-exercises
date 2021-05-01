def max_profit(a):
    """
    write a function that takes a list of prices a and returns the max profit possible by buying at a given
    price then selling at a future price, for e.g.

    [2, 5, 1, 3, 10] should return 9 (10 - 1)
    [4, 3, 2, 1] should return 0 (prices are always decreasing)
    """
    if len(a) == 1:
        return 0

    min_price, max_ = float("inf"), 0
    for price in a:
        profit = price - min_price
        max_ = max(profit, max_)
        min_price = min(price, min_price)
    return max_


if __name__ == "__main__":
    assert max_profit([2, 5, 1, 3, 10]) == 9
    assert max_profit([4, 3, 2, 1]) == 0
    assert max_profit([1]) == 0
    assert max_profit([1, 3, 10, 43]) == 42
