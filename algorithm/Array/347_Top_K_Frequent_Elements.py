class Solution(object):
    def topKFrequent(self, nums, k):
        hs = {}
        frq = {}

        # counter, map element to frequency
        for i in range(0, len(nums)):
            hs[nums[i]] = hs.get(nums[i], 0) + 1

        # map frequency to index (one to many)
        for idx, v in hs.iteritems():
            frq[v] = frq.get(v, []) + [idx]
            # warning: the following line does not work
            # frq[v] = frq.get(v, []).append(idx)

        arr = []
        for x in range(len(nums), -1, -1):
            if x in frq:
                for i in frq[x]:
                    arr.append(i)
                    if len(arr) == k:
                        return arr