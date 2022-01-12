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
