# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 : return l2
        elif not l2 : return l1

        mergeList = None

        if(l1.val < l2.val) :
            mergeList = l1
            mergeList.next = self.mergeTwoLists(l1.next,l2)
        else :
            mergeList = l2
            mergeList.next = self.mergeTwoLists(l1,l2.next)

        return mergeList

listNode5 = ListNode(5)

listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode4 = ListNode(4)
listNode1.next = listNode2
listNode2.next = listNode4

s = Solution()
result = s.mergeTwoLists(listNode5,listNode1)

while result :
    print("result :{}".format(result.val))
    result = result.next