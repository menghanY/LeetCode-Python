# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        tRoot = root
        if not tRoot : return 0
        return max(self.maxDepth(tRoot.left),self.maxDepth(tRoot.right)) + 1