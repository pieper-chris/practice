
# Basic Greedy Algorithm Examples
# Optimization problems

'''From discrete mathematics course notes: "Algorithms that make what seems to be the “best” choice at each step are called greedy algorithms"'''

# Change Return - find right change (USD) that takes least amount of coins (greedy choice)
# IS NOT optimal for all coin sets given

def make_change(coin_values, cents):
    num_coins = len(coin_values)
    d = [0]*num_coins
    for i in range(num_coins):
        while (cents >= coin_values[i]):
            d[i] += 1
            cents = cents - coin_values[i]
    return d


print("\nTest Cases...\n")
print("\nCoin Values take form: [Half-Dollar, Quarter, Dime, Nickel, Penny]\n")
print("56 cents: ", make_change([50,25,10,5,1], 56))
print("10 cents: ", make_change([50,25,10,5,1], 10))
print("0 cents: ", make_change([50,25,10,5,1], 0))
print("1 cent: ", make_change([50,25,10,5,1], 1))
print("90 cents: ", make_change([50,25,10,5,1], 90))
print("129 cents: ", make_change([50,25,10,5,1], 129))
print("800 cents: ", make_change([50,25,10,5,1], 800))
print("-2 cents: ", make_change([50,25,10,5,1], -2))
print("15 cents: ", make_change([50,25,10,5,1], 15))
print("17 cents: ", make_change([50,25,10,5,1], 17))
