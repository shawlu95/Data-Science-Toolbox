# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)

        # initialize prev with dummy node
        # so when first element has duplicates, prev/dummy is connected to the first unique node
        prev = dummy
        dummy.next = head
        node = head
        while node and node.next:
            if node.val == node.next.val:
                while node and node.next and node.val == node.next.val:
                    node = node.next

                # move past last duplicate node
                node = node.next

                # splice
                prev.next = node
            else:
                prev = node
                node = node.next
        return dummy.next
