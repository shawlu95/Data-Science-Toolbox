class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s = list(s)
        # t = list(t)

        if len(s) > len(t):
            return False

        i = 0  # slower pointer points to s
        j = 0  # faster pointer points to t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        return False