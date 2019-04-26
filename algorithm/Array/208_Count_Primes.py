class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            # if res[i] is prime, all of its multiple less than n is not prime
            if res[i]:
                # be careful with + 1, which is excluded by range
                for j in range(2, (n-1) // i + 1):
                    res[i * j] = False
        return sum(res)