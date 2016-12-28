from TreeNode import TreeNode
from collections import deque
class Solution(object):
    def minDepthDFS(self, root):
        def helper(root):
            if root is None:
                #正无穷
                return float('inf')
            elif root.left is None and root.right is None:
                return 1
            return 1 + min(helper(root.left),helper(root.right))
        if root is None: return 0
        return helper(root)
    def minDepthBFS(self,root):
        q,depth = deque(),0
        if root :
            q.append(root)
        while len(q) :
            depth += 1
            for _ in range(len(q)):
                x = q.popleft()
                if x.left is None and x.right is None :
                    return depth
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return depth

print(float('inf'))