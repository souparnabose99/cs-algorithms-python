
def gcd(a, b):
    # If a/b without remainder, then gcd is b
    if a % b == 0:
        return b
    return gcd(b, a % b)


def gcd_iter(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


print(gcd(2455, 3965))
print(gcd_iter(2455, 3965))

# 5
# 5
