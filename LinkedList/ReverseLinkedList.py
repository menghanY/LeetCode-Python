# https://leetcode.com/problems/reverse-linked-list/
# Reverse a singly linked list.
from ListNode import ListNode
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