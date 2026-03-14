def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fib(n - 1) + fib(n - 2)


# Test fib from 0 to 10
for i in range(11):
    print(f"fib({i}) =", fib(i))
