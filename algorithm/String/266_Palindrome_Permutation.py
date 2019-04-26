class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = [0] * 128
        for c in s:
            counter[ord(c)] += 1

        balancer = 0
        for n in counter:
            balancer += n % 2
        return balancer <= 1