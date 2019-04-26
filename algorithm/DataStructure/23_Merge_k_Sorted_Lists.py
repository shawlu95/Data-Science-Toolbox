# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
import heapq

class Solution(object):
    # sort and compare heads
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [l for l in lists if l]
        head = ListNode(0)
        node = head
        while lists:
            lists.sort(key = lambda n : n.val)
            nxt = lists.pop(0)
            node.next = nxt
            node = node.next
            if nxt.next:
                lists.append(nxt.next)
        return head.next

    # priority queue
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = node = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, nxt = q.get()
            node.next = nxt
            node = node.next
            if nxt.next:
                q.put((nxt.next.val, nxt.next))
        return head.next

    # heapq
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, l) for l in lists if l]
        heapq.heapify(h)
        head = node = ListNode(0)
        while h:
            val, nxt = heapq.heappop(h)
            node.next = nxt
            node = node.next
            if nxt.next:
                heapq.heappush(h, (nxt.next.val, nxt.next))
        return head.next