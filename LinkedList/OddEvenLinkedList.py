# iven a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def oddEvenList(self, head):
    #     oddListNode,evenListNode = None,None
    #     oddNode,evenNode = None,None
    #     while head :
    #         if head.val % 2 == 0 :
    #             if evenListNode :
    #                 evenNode.next = head
    #                 evenNode = evenNode.next
    #             else :
    #                 evenNode = head
    #                 evenListNode = evenNode
    #         else :
    #             if oddListNode :
    #                 oddNode.next = head
    #                 oddNode = oddNode.next
    #             else :
    #                 oddNode = head
    #                 oddListNode = oddNode
    #
    #         head = head.next
    #
    #     if oddNode : oddNode.next = evenListNode
    #     if evenNode : evenNode.next = None
    #     return oddListNode
    def oddEvenList(self, head):
        if head == None: return head
        if head.next == None : return head
        oddListNode,evenListNode = None,None
        oddNode,evenNode = None,None
        while head and head.next :
            print(head.val,head.next.val)
            if oddListNode :
                oddNode.next = head
                oddNode = oddNode.next
            else :
                oddNode = head
                oddListNode = oddNode
            if evenListNode :
                evenNode.next = head.next
                evenNode = evenNode.next
            else :
                evenNode = head.next
                evenListNode = evenNode
            head = head.next.next
        if head :
            oddNode.next = head
            oddNode = oddNode.next
        if oddNode : oddNode.next = evenListNode
        if evenNode : evenNode.next = None
        return oddListNode

