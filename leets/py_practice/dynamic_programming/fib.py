
# nth fib num w memoization using object ds
def fib(self, n: int) -> int:
    memo = {}
    t = 0
    while t <= n:
        if t == 0:
            memo[t] = 0
        elif t == 1 or t == 2:
            memo[t] = 1
        else:
            val = memo[t-1] + memo[t-2]
            memo[t] = val

        t += 1

    return memo[n]

# awesome tuple solution w memoization
def fib(self, n: int) -> int:
    if n == 0:
        return 0

    memo = (0, 1)
    for _ in range(2, n+1):
        memo = (memo[-1], memo[-1] + memo[-2])

    return memo[-1]
