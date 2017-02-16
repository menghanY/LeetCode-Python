# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
from collections import deque
class Solution(object):
    def largestValues(self, root):
        res,q = [],deque()
        if root:
            q.append(root)
        while q :
            nums = []
            for i in range(len(q)):
                top = q.popleft()
                nums.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            res.append(max(nums))
        return res