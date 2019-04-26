class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        def rec(n):
            if n == 1:
                return True

            if n % 2 == 0:
                return rec(n / 2)
            elif n % 3 == 0:
                return rec(n / 3)
            elif n % 5 == 0:
                return rec(n / 5)
            else:
                return False

        return rec(num)

    def isUgly2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False
        return True
