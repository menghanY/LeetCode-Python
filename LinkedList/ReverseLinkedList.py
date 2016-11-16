https://leetcode.com/problems/reverse-linked-list/
# Reverse a singly linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList1(self, head):
        reversedHead,pPrev = None,None
        pNode = head
        while not pNode :
            pNext = pNode.next
            if not pNext :
                reversedHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext