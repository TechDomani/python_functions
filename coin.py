from function import minimum_coins_required

def obtain_integer_input():
    while True:
        try:
            amount = int(input("Amount in pence "))
            return amount
        except ValueError as e:
            print('Please enter a whole number of pence')

      
amount = obtain_integer_input()
numberOfCoins = minimum_coins_required(amount)
print("The minimum number of coins required is ", numberOfCoins)