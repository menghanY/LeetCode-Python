# https://leetcode.com/problems/binary-tree-right-side-view/
from TreeNode import TreeNode
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        res,q = [],deque()
        if root :
            q.append(root)
        while q :
            res.append(q[-1].val)
            for i in range(len(q)):
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        return res