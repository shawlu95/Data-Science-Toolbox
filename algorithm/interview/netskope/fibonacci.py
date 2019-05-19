def F(m):
    """
    Write a function that compute Fibbo number at index m.
    """
    large, small = 1, 0
    # dynamically update the two variables
    for i in range(m):
        large, small = large + small, large
    return small

def sum_fib(m, n):
    """
    Let me start simple. Just call F() for n in a range and see if we can simplify further.
    I Believe we can simplify it. Because when computing F[n] (larger number), we have computed F[n-1], F[n-2] ... F[m].
    """
    if m > n:
        m, n = n, m
    return sum(F(i) for i in range(m, n + 1)) # inclusive.

def sum_fib_dp(m, n):
    """
    A dynamic programming version.
    """
    if m > n: m, n = n, m

    large, small = 1, 0

    # a running sum for Fibbo m ~ n + 1
    running = 0

    # dynamically update the two variables
    for i in range(n):
        large, small = large + small, large

        # note that (i + 1) -> small is basically mapping m -> F[m]
        if m <= i + 1 <= n:
            running += small
    return running
