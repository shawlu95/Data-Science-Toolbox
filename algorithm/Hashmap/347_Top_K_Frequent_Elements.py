class Solution(object):
    def topKFrequent(self, nums, k):
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            hs[nums[i]] = hs.get(nums[i], 0) + 1

        # frequency count: num as key, frequency as value
        # note: items() is equivalent to iteritems() in Python2
        # warning: enumerate() is different, cannot use here
        for z, v in hs.items():
            # frq[v] = frq.get(v, []).append(z)
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)

        arr = []
        # init with highest possible frequency and decrement
        # check if frequency is saved, append its frequency to array, ranked from high to low
        for x in range(len(nums), 0, -1):
            if x in frq:
                # many number may have same frequency, so each frequency corresponds to a list
                for i in frq[x]:
                    arr.append(i)

        # same frequency is considered as two counts, so k decrements by one regardless of identical frequency
        return [arr[x] for x in range(0, k)]


arr = [1,1,1,2,2,3]
k = 2

solver = Solution()
print(solver.topKFrequent(arr, k))