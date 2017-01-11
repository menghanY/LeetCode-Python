# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
from TreeNode import TreeNode
class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        if root :
            q = [root]
            i = 0

            while i < len(q) :
                level = []
                for j in range(len(q) - i) :
                    n = q[i]
                    level.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                    i += 1
                res.insert(0,level)

        return res
