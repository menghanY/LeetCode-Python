# https://leetcode.com/problems/binary-tree-level-order-traversal/
from TreeNode import TreeNode
class Solution(object):
    def levelOrder(self, root):
        res = []
        if root :
            q = [root]
            i = 0
            while i < len(q) :
                level = []
                for j in range(len(q) - i) :
                    node = q[i]
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    i += 1
                res.append(level)
        return res