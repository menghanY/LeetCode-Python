# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://discuss.leetcode.com/topic/58081/simple-python-solution
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val :
            return self.lowestCommonAncestor(q,p)
        while not p.val <= root.val <= q.val :
            root = root.left if q.val < root.val else root.right
