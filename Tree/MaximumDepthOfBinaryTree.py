# Definition for a binary tree node.
from TreeNode import TreeNode
class Solution(object):
    def maxDepth(self, root):
        tRoot = root
        if not tRoot : return 0
        return max(self.maxDepth(tRoot.left),self.maxDepth(tRoot.right)) + 1