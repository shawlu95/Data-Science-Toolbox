import collections
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # check if valid palindrome can be formed
        kv = collections.Counter(s)
        mid = [k for k, v in kv.items() if v % 2]
        if len(mid) > 1:
            return []

        # palindrome can be odd/even length
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v // 2) for k, v in kv.items()])
        half = [c for c in half]

        def backtrack(n, tmp):
            if len(tmp) == n:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(n):
                    # -------------------- IMPORTANT ------------------
                    # condition 1: when the same index has been used in tmp, it cannot be reused
                    # condition 2: i - 1 had been marked false means i - 1 was used before
                    # --------------------------------------------------
                    if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    backtrack(n, tmp + [half[i]])
                    visited[i] = False # back track, mark current element as unused

        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans

solver = Solution()
print(solver.generatePalindromes("aaabaaa"))