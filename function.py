def minimum_coins_required(amountInPence):
    coinCount = 0
    amountInPence = int(amountInPence)
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    if (amountInPence < 1):
        return coinCount
    for coin in coins:
        while amountInPence >= coin:
            amountInPence = amountInPence - coin
            coinCount += 1
    return coinCount


def capitalise_even_letters(val):
    ret = ""
    count = 1
    for ind, char in enumerate(val): 
        if char.isspace():
            count = count
            ret = ret + char
        elif (ind + count) % 2 == 0:
            ret = ret + char.upper()
        else:
            ret = ret + char.lower()
    return ret