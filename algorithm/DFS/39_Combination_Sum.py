class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        # sort from small to large, so when target < 0, no need to check further
        candidates.sort()

        def dfs(candidates, target, idx, path, ans):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return

            # to allow reuse element, start i with the same as idx
            for i in range(idx, len(candidates)):
                # no need to prune tree, as input contians no duplicates
                # if i > idx and candidates[i] == candidates[i - 1]:
                #     continue
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], ans)
        dfs(candidates, target, 0, [], ans)
        return ans

solver = Solution()
ans = solver.combinationSum([2,3,6,7], 7)
print(ans)