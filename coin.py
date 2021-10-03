from function import minimum_coins_required

def obtain_integer_input(maxValue=50000, minValue=1):
    while True:
        try:
            amount = int(input('Please enter an amount in pence '))
            if (amount < minValue or amount > maxValue):
                print('You must enter a value between', minValue, 'and', maxValue)
                continue
            return amount
        except ValueError as e:
            print('Please enter a whole number of pence')

      
amount = obtain_integer_input()
numberOfCoins = minimum_coins_required(amount)
print('The minimum number of coins required is', numberOfCoins)