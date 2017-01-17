# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from TreeNode import TreeNode
class Solution(object):
    def kthSmallest(self, root, k):
        if not root : return None
        result = []
        self.in_order(root, result)
        return result[k-1]
    def in_order(self,root,result):
        if root:
            self.in_order(root.left, result)
            result.append(root.val)
            self.in_order(root.right,result)
