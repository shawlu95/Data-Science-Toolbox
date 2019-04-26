class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n+1)]

        # compute factorial up to n
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            id = k // fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            del nums[id]
        return ''.join(ans)
solver = Solution()
print(solver.getPermutation(4, 13))