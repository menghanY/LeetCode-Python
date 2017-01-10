# https://leetcode.com/problems/linked-list-cycle-ii/
from ListNode import ListNode
class Solution(object):
    def detectCycle(self, head):
        slow,fast = head,head
        while True:
            if fast == None or fast.next == None : return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                break
        while head != fast:
            head = head.next
            fast = fast.next
        return head