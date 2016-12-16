# https://leetcode.com/problems/linked-list-cycle/
# Given a linked list, determine if it has a cycle in it.
from ListNode import ListNode
class Solution(object):
    # https: // leetcode.com / problems / linked - list - cycle /
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False