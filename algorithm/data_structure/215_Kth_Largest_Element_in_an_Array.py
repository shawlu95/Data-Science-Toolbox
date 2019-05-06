import heapq
class Solution(object):
    def findKthLargestHeap(self, nums, k):
        print(nums)
        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k
        print(heap)
        for num in nums[k:]:
            # if a new number if larger than smallest among the top k
            # the new number makes it into the top k
            if num > heap[0]:
                # Pop and return the smallest item from the heap,
                # and also push the new item.
                heapq.heapreplace(heap, num)
            # or use:
            # heapq.heappushpop(heap, num)
        return heap[0]

    # quick select
    # O(n) time, quicksort-Partition method
    def findKthLargest(self, nums, k):
        # after one call, pos will be in correct position
        pos = self.partition(nums, 0, len(nums) - 1)

        if len(nums) - pos < k:
            # extend search region left (excluding pos), param k-(len(nums)-pos) > 0
            return self.findKthLargest(nums[:pos], k - (len(nums) - pos))
        elif len(nums) - pos > k:
            # search right, there are more than k elements behind pos
            return self.findKthLargest(nums[pos + 1:], k)
        else:
            return nums[pos]

    # Lomuto partition scheme
    def partition(self, nums, l, r):
        pivot = nums[r]

        # lo is not finalized until it's swapped with something
        lo = l
        # r is fixed as pivot, swap when loop exits
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo