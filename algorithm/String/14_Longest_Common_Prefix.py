class Solution:
    # horizontal scan
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]
        lenPrefix = len(prefix)
        for s in strs[1:]:
            i, common = 0, 0
            while i < len(prefix) and i < len(s):
                if prefix[i] == s[i]:
                    common += 1
                    i += 1
                else:
                    break
            lenPrefix = min(common, lenPrefix)
        return prefix[:lenPrefix]

    # vertical scan
    def longestCommonPrefixVertical(self, strs):
        if not strs:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                # when i == len(s) - 1, has reached the last element of s
                if i > len(s) - 1 or c != s[i]:
                    return strs[0][:i]
        return strs[0]