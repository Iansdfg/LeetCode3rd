# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = curr = ListNode(0)
        val = 0
        
        while l1 or l2 or val:
            if l1: 
                val += l1.val 
                l1 = l1.next
            if l2: 
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val%10)
            
            val //= 10
            curr = curr.next
            
        return head.next
            
