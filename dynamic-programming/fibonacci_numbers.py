

def fibonacci_recursion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


# Top-down approach
def fibonacci_memoization(n, table):
    if n not in table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)

    # O(1) runtime complexity
    return table[n]


print("With DP/Memoization : ", fibonacci_memoization(5, {0: 1, 1: 1}))
print("Without DP/Memoization : ", fibonacci_recursion(5))



