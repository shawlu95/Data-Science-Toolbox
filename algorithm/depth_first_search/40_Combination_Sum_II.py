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
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                # to allow reuse elements, start i with the same as idx
                dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], ans)
        dfs(candidates, target, 0, [], ans)
        return ans
