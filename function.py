def minimum_coins_required(amountInPence, limitIndex=0, coinCount=0):
    amountInPence = int(amountInPence)
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    if (amountInPence < 1):
        return coinCount
    if (amountInPence < coins[limitIndex]):
        limitIndex += 1
        return minimum_coins_required(amountInPence, limitIndex, coinCount)
    amountInPence = amountInPence - coins[limitIndex]
    coinCount += 1
    return minimum_coins_required(amountInPence, limitIndex, coinCount)

