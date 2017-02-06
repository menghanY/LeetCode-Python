# https://leetcode.com/problems/remove-linked-list-elements/
from ListNode import ListNode
class Solution(object):
    def removeElements(self, head, val):
        res = head
        pre = None
        while head :
            if head.val == val :
                if not pre :
                    res = head.next
                else:
                    pre.next = head.next
            else:
                pre = head
            head = head.next
        return res
