from ListNode import ListNode
class Solution(object):
    def sortList(self, head):
        h = head
        vals = []
        while h :
            vals.append(h.val)
            h = h.next
        vals.sort()
        h1 = head
        count = 0
        while h1:
            h1.val = vals[count]
            count += 1
            h1 = h1.next
        return head