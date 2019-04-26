class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(candidates, target, idx, path, ans):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return


            for i in range(idx, len(candidates)):
                # avoid duplicate path
                # without i > idx, will output '[[1,2,5],[1,7],[2,6]]' instead of '[[1,2,5],[1,7],[1,1,6],[2,6]]'
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                # to disallow reuse elements, start i with the same as idx
                dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], ans)
        dfs(candidates, target, 0, [], ans)
        return ans

solver = Solution()
ans = solver.combinationSum([10,1,2,7,6,1,5], 8)
print(ans)