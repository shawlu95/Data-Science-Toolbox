class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return 0
        l = list(s)
        ans = 0
        for c in l:
            ans = (ord(c) - ord('A') + 1) + ans * 26
        return ans

    def titleToNumber2(s):
        s = s[::-1]
        ans = 0
        for exp, char in enumerate(s):
            ans += (ord(char) - ord('A') + 1) * (26 ** exp)
        return ans


    def titleToNumber3(self, s):
        ans = 0
        for idx, c in enumerate(s):
            ans = (ord(c) - ord('A') + 1) + ans * 26
        return ans