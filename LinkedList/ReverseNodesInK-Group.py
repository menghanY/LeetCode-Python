# https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or k < 2:
            return head

        next_head = head
        for i in range(k - 1):
            next_head = next_head.next
            if next_head is None:
                return head
        ret = next_head

        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                _next = current.next
                current.next = prev
                prev = current
                current = _next
            tail.next = next_head or current

        return ret