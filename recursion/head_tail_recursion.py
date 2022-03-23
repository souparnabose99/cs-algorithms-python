
def tail(n):
    print("Calling tail with n = ", str(n))
    if n == 0:
        return
    print(n)
    tail(n-1)
    pass


# Head recursion makes twice as many operations as Tail recursion
def head(n):
    print("Calling head with n = ", str(n))
    if n == 0:
        return
    head(n-1)
    print(n)


tail(5)
head(5)

# Calling tail with n =  5
# 5
# Calling tail with n =  4
# 4
# Calling tail with n =  3
# 3
# Calling tail with n =  2
# 2
# Calling tail with n =  1
# 1
# Calling tail with n =  0
# Calling head with n =  5
# Calling head with n =  4
# Calling head with n =  3
# Calling head with n =  2
# Calling head with n =  1
# Calling head with n =  0
# 1
# 2
# 3
# 4
# 5

