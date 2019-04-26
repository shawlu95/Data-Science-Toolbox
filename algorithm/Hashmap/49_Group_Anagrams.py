# warning: tuple can be used as key
# list and set cannot be used as key!!!

class Solution(object):
    # sorting O(NKlogK) time
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mem = {}
        for str in strs:
            strS = tuple(sorted(str))
            mem[strS] = mem.get(strS, []) + [str]
        return mem.values()

    # aviud sorting, O(NK) time
    def groupAnagrams2(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

solver = Solution()
print(solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))