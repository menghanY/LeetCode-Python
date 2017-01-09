from ListNode import ListNode
class Solution(object):
    def isPalindrome1(self, head):
        if not head or not head.next :
            return True
        slow,fast = head,head

        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next

        last = slow.next
        pre = head
        while last.next :
            temp = last.next
            last.next = temp.next
            temp.next = slow.next
            slow.next = temp

        while slow.next :
            slow = slow.next
            if pre.val != slow.val :
                return False
            pre = pre.next

        return True


