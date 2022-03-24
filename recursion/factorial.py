
def factorial_head(n):
    if n == 0:
        return 1
    sub_result_1 = factorial_head(n-1)
    result = n*sub_result_1
    return result


num = factorial_head(5)
print(num)
