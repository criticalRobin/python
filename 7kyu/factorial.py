def factorial(n):
    if n < 0 or n > 12:
        return ValueError
    else:
        return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


print(factorial(30))
