import collections
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        keys = count.keys()
        keys.sort(key = lambda w : [-count[w], w])
        return keys[:k]

    def topKFrequent2(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()] # iterrate dict

        # heapify takes a list of tuple as input
        heapq.heapify(heap) # O(n)
        return [heapq.heappop(heap)[1] for _ in range(k)]

solver = Solution()
ans = solver.topKFrequent2(["i", "love", "leetcode", "i", "love", "coding"], k = 2)
print(ans)