# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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