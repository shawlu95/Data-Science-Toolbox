class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        def isValid(c):
            c = ord(c)
            return (c in range(ord('a'), ord('z') + 1)
                    or c in range(ord('A'), ord('Z') + 1)
                    or c in range(ord('0'), ord('9') + 1))

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and isValid(s[i]) is False:
                i += 1
            while i < j and isValid(s[j]) is False:
                j -= 1

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True


s =  "A man, a plan, a canal: Panama"
solver = Solution()
print(solver.isPalindrome(s))