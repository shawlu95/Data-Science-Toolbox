class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0
        l1 = len(haystack)
        l2 = len(needle)

        if l2 == 0:
            return 0

        while i < l1:
            if haystack[i: i + l2] == needle:
                return i
            i += 1
        return -1