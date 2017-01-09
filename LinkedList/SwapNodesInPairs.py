from ListNode import ListNode
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next :
            return head
        resNode = head.next
        while head :
            pre = head
            head = head.next.next

