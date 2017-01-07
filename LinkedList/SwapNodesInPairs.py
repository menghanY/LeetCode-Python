# https://leetcode.com/problems/swap-nodes-in-pairs/
from ListNode import ListNode
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return []
        if not head.next:
            return head

        r_head = ListNode(0)
        l = r_head

        l.next = head
        m = head
        r = head.next

        while m or r:
            if not r:
                return r_head.next
            else:
                m.next = r.next
                r.next = m
                l.next = r

                m = m.next
                r = r.next.next
                l = l.next.next

                if r:
                    r = r.next

        return r_head.next


four = ListNode(4)
three = ListNode(3)
two = ListNode(2)
one = ListNode(1)

one.next = two
two.next = three
three.next = four

# while one :
#     print(one.val)
#     one = one.next

Solution().swapPairs(one)