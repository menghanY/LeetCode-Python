# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given a linked list, remove the nth node from the end of list and return its head.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        tempHead = listNode = head
        for _ in range(n) :
            tempHead = tempHead.next
        if tempHead == None :
            return head.next
        while tempHead.next :
            listNode = listNode.next
            tempHead = tempHead.next
        listNode.next = listNode.next.next
        return head

