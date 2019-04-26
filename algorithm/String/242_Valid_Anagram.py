class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = [0] * 26
        count_t = [0] * 26
        for c in s:
            count_s[ord(c) - ord('a')] += 1
        for c in t:
            count_t[ord(c) - ord('a')] += 1
        print(count_s)
        print(count_t)
        return count_s == count_t