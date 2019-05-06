def maxProfit(prices) -> int:
    cooling, resting, holding = 0, 0, 0
    for i in range(1, len(prices)):
        print(resting, holding, cooling)
        delta = prices[i] - prices[i - 1]
        new_cooling = holding + delta
        new_resting = max(cooling, resting)
        new_holding = max(resting, holding + delta)
        cooling, resting, holding = new_cooling, new_resting, new_holding
    print(resting, holding, cooling)
    return max(cooling, resting)

print(maxProfit([4, 5, 3, 1, 5]))