
# Need Dynamic programming for non-cononical coin set (we can make any set)

''' Below implementation is NOT mine. It is following an overview
  at https://www.youtube.com/watch?v=m2Elp9ubY3w for learning purposes.'''


def coin_matrix(coin_values, cents):
    mat = [[0 for m in range(cents + 1)] for m in range(len(coin_values)+1)]
    for i in range(cents+1):
        mat[0][i] = i
    return mat
    
def dynamic_change(coin_values, cents):
    matrix = coin_matrix(coin_values,cents)
    for c in range(1, len(coin_values)+1):
        for r in range(1, cents+1):
            if (coin_values[c-1] == r):
                matrix[c][r] = 1
            elif coin_values[c-1] > r:
                matrix[c][r] = matrix[c-1][r]
            else:
                matrix[c][r] = min(matrix[c-1][r], 1+matrix[c][r-coin_values[c-1]])
    # print(matrix)
    return matrix[-1][-1]
    
print("Coins needed for 30 cents: ", dynamic_change([1, 10, 25], 30))
print("Coins needed for 32 cents: ", dynamic_change([1, 10, 25], 32))
print("Coins needed for 25 cents: ", dynamic_change([1, 10, 25], 25))

