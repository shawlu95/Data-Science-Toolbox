class Solution(object):
    def reverseStringRecursive(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseStringRecursive(s[l//2:]) + self.reverseStringRecursive(s[:l//2])

    def reverseStringClassic(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

    def reverseStringPythonic(self, s):
        return s[::-1]

solver = Solution()
print(solver.reverseStringRecursive("hello"))