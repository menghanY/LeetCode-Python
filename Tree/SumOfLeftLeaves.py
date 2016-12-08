# Definition for a binary tree node.
from TreeNode import TreeNode
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root : return 0
        num = 0
        if root.left and not root.left.left and not root.left.right : num = root.left.val
        return num + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)