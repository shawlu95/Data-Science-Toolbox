import collections
class Solution(object):

    # brute force
    def partition2(self, s):
        res = []

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            # warning: index ends with len(s), not len(s) - 1
            # because s[:len(s)] is the whole string
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i:-1]:
                    dfs(s[i:], path + [s[:i]], res)

        dfs(s, [], res)
        return res

    # memo, backward
    # use a list of list, with index as implicit key
    # index i stores a list of palindromes made from first i characters
    def partitionDBRec(self, s):
        # we'll use string length as key to retrieve, so memo need one extra space
        self.memo = [None] * (len(s) + 1)

        # zero length string has an empoty list, which is used as base case
        self.memo[0] = [[]]

        def partition_core(s):
            s_len = len(s)
            if self.memo[s_len]:
                return self.memo[s_len]
            res = []
            for i in range(len(s) - 1, - 1, - 1):
                current = s[i:]
                if current == current[::-1]:
                    # pre_res = partition_core(s[:i])
                    # res += [r + [current] for r in pre_res]

                    for rem in partition_core(s[:i]):
                        res.append(rem + [current]) # concatenate two list, and concatenate list to res
            self.memo[s_len] = res
            return res

        return partition_core(s)

    # same logic as above, same recurson
    # def partitionDPRec2(self, s):
    #     def helper(s, h):
    #         if s in h:
    #             return h[s]
    #         h[s] = []
    #         for i in range(len(s)):
    #             if s[:i + 1] == s[:i + 1][::-1]:
    #                 if i + 1 == len(s):
    #                     h[s].append([s])
    #                 else:
    #                     for rest in self.helper(s[i + 1:], h):
    #                         h[s].append([s[:i + 1]] + rest)
    #         return h[s]
    #
    #     return helper(s, {})

    def partitionDP(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def make_results(index, pallindromes, result, results):
            if index >= len(s):
                results += result[:]
            else:
                for pallindrome in pallindromes[index]:
                    make_results(index + len(pallindrome), pallindromes, result + [pallindrome], results)

        n = len(s)
        is_pallindrome = set()
        pallindromes = collections.defaultdict(list)
        for i in range(0, len(s)):
            for j in range(i + 1):
                if s[i] == s[j] and ((i - j) <= 1 or (j + 1, i - 1) in is_pallindrome):
                    is_pallindrome.add((j, i))
                    substring = s[j:i + 1]
                    pallindromes[j] += substring

        results = []
        make_results(0, pallindromes, [], results)
        return results

solver = Solution()
print(solver.partitionDPRec2("aab"))