# brute force is the only solution. Nothing interesting
# time O(D)
# space O(D)
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def isSelfDivisible(n):
            x = n
            while x > 0:
                x, r = divmod(x, 10)
                if r == 0 or n % r > 0:
                    return False
            return True

        ans = []
        for n in range(left, right + 1):
            if isSelfDivisible(n):
                ans.append(n)
        return ans