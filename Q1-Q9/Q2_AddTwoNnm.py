# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retList = cur = ListNode(0)
        c = 0
        while l1 or l2 or c:
        	if l1:
        		c += l1.val
        		l1 = l1.next
        	if l2:
        		c += l2.val
        		l2 = l2.next
        	cur.next = ListNode(c % 10)
        	cur = cur.next
        	c //= 10
        return retList.next
