# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        Remove all elements from a linked list of integers that have value val.
        Use the head to eliminite first n hits, and use pointer to eliminite the rest
        e.g 1->1->1->2->3->1, 1
        Head will be moved to 2, pointer will start from 3

        time complexity: O(n)
        space complexity: O(1)

        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # move the head to its next node if its value is equal to the input value
        while head is not None and head.val == val:
            head = head.next

        # handle null value after moving
        if head is None:
            return None

        # create a pointer reference to the head node, and loop to check its next node's value
        # if it is equal to the input val, skip that node
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


