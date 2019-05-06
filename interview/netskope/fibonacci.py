# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
#
# Enjoy your interview!
#
# Hello
#
# Hi there!
#
# Python please.
# Can you call me at 650 283 6267? Ok! That works too. Nice to e-meet you!
# My first question is which language you prefer ?
# Did you get my email where I wrote we'll be doing text only?
# NP.  So let's switch to the python language (top right pulldown)
#
#
# You can click on the Run button to see how it works.
# OK, let me copy the exercise....

# got it!


#
# A simple coding exercise problem (no tricks here):
#
# Find the sum of (the fibonacci series) in any given range
# ---------------------------------------------------------
#
# First, the fibonacci series definition:
#
#   The n-th Fibonacci number fib(n) is a number in a series defined
#   recursively this way:
#
#       fib(0) may be defined as 0 (for convenience)
#       fib(1) the 1st number in the series, is 1
#       fib(n) is the sum of the previous 2 fibonacci numbers
#
# The first 10 numbers in the fib(n) series (fib(1), ..., fib(10)) are:
#
#   1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#
# Calculating fib(n) where n is a natural number can be solved
# in more than one way. Pick whichever you feel comfortable with
# Likewise, pick the programming language you feel comfortable with.
#
# Now to the problem we want to solve:
#   A sum of fibonacci numbers between two natural numbers M and N
#   Is the sum of the sub-series between fib(M) and fib(N) inclusive.
#
# The sum_fib(m, n) function returns the sum of fibonacci numbers
# between m and n (inclusive):
#
# Notes/tips:
#   - Try writing a few input->output examples first,
#     to make sure you understand the problem.
#   - Please pay attention to correctness above all
#   - Please pay attention to edge cases
#   - Bonus points if you can solve this efficiently
#   - Bonus points if your solution is clear/simple/straightforward
#   - Bonus points for style and neatliness, spacing, indentation
#   - Bonus points for modularity/refactoring (no code repetitions)
#   - Bonus points for good abstractions/APIs that makes the most sense
#   - Bonus points for good var/func naming (code does what it says)
#   - You must test your solution online by using a main() that will
#     call your solution in a convincing way to establish correctness.
#   - Most bonus points for GOOD self-testing (not just a particular case)
#     Feel free to add assertions to make sure what you write is correct.
#
# Feel free to ask any question at any time.
#

#
# NOTE: you are allowed to add as many functions as you need

"""
Let me write block comment to walk through the problem.
First make sure I get the question:
A series F is Fibonacci if F[1] = 1, F[2] = 1, F[3] = 2, ... F[n] = F[n - 1] + F[n - 2].
Given m, n where m <= n (equal allowed), we want to find sum(F[i] for i in range(m, n + 1)) (ending index exclusive).


A few example:
sum_fib(2, 4) = F[2] + F[3] + F[4] = 1 + 2 + 3 = 6

So we need to:
    (1) calculate Fibonacci number efficiently (F[n]). This can be done with dynamic programming.
    (2) sum them up in desired range. This step can be done by saving F[1] to F[n] in an array, or more efficiently, keep a running total for F[1] ... F[n], then take two snapshots at n = m and n = n. Subtract the two to get the sum between F[m], F[n].
"""

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
    if m > n:
        m, n = n, m

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

def main():
    # for ... :
    #     # THOROUGHLY test your solution
    #     ...
    # Test Fibonacci computation
    assert(F(0) == 0)
    assert(F(4) == 3)
    assert(F(5) == 5)
    assert(F(6) == 8)
    assert(F(7) == 13)

    # test Fibbonacci sum in range (pass test)
    assert(sum_fib(1, 1) == 1)
    assert(sum_fib(1, 2) == 2)
    assert(sum_fib(1, 3) == 4)
    assert(sum_fib(1, 5) == 12)

    # test DP against normal version
    assert(sum_fib(1, 1) == sum_fib_dp(1, 1))
    assert(sum_fib(1, 2) == sum_fib_dp(1, 2))
    assert(sum_fib(1, 3) == sum_fib_dp(1, 3))
    assert(sum_fib(1, 5) == sum_fib_dp(1, 5))

    # large m, n
    for n in range(1000, 1100):
        m = n + 10
        assert(sum_fib(n, m) == sum_fib_dp(n, m))

    # m == n
    for n in range(1000, 1100):
        assert(sum_fib(n, n) == sum_fib_dp(n, n))

main()
