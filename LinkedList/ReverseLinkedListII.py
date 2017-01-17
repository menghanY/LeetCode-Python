# https://leetcode.com/problems/reverse-linked-list-ii/
from ListNode import ListNode
class Solution(object):
    def reverseBetween(self, head, m, n):
        hat = ListNode(0)
        hat.next = head
        start = hat

        for _ in range(m):
            beforeStart = start
            start = start.next

        for _ in range(n - m):
            beforeStart.next = start.next
            start.next =  start.next.next
            beforeStart.next.next =  beforeStart.next

        return hat.next