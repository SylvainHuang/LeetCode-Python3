# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        pans = ans
        p1 = l1
        p2 = l2
        
        while p1 and p2:
            tmp = ListNode()
            if p1.val <= p2.val:
                tmp.val = p1.val
                p1 = p1.next
            else:
                tmp.val = p2.val
                p2 = p2.next
            pans.next = tmp
            pans = pans.next
            
        p = p1 if p1 else p2
        while p:
            tmp = ListNode()
            tmp.val = p.val
            p = p.next
            pans.next = tmp
            pans = pans.next
        return ans.next
