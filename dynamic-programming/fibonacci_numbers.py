
# Exponential runtime complexity
def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


# Top-down approach, O(N) runtime complexity
def fibonacci_memoization(n, table):
    if n not in table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)

    # O(1) runtime complexity
    return table[n]


# Bottom-up approach, O(N) runtime complexity
def fibonacci_tabulation(n, table):
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]


print("With DP/Memoization : ", fibonacci_memoization(6, {0: 0, 1: 1}))
print("With DP/Memoization : ", fibonacci_tabulation(6, {0: 0, 1: 1}))
print("Without DP/Memoization : ", fibonacci_recursion(6))

# With DP/Memoization :  8
# With DP/Memoization :  8
# Without DP/Memoization :  8


