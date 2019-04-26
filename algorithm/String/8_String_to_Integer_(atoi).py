class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        # if len(ls) == 0 : return 0

        ls = list(s.strip())
        if len(ls) == 0:
            return 0

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i] in "0123456789":
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        # if overflow, return max int
        # if underflow, return min int
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))