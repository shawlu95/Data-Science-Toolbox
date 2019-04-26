class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        m = {"I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000}

        num = 0
        for i in range(len(s) - 1):
            if m[s[i]] < m[s[i + 1]]:
                num -= m[s[i]]
            else:
                num += m[s[i]]
        num += m[s[-1]]
        return num

solver = Solution()
print(solver.romanToInt("MCMXCIV"))