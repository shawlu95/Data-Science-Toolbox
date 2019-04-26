class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        if not chars:
            return None
        # write your code here
        chars = list(chars)
        i = j = 0
        while j <= len(chars) - 1:
            if ord(chars[j]) in range(ord('a'), ord('z') + 1):
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
            j += 1
        return "".join(chars)

s = "abAcD"
solver = Solution()
print(solver.sortLetters(s))