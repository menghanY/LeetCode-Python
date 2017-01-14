# https://leetcode.com/problems/unique-binary-search-trees-ii/
from TreeNode import TreeNode
class Solution(object):
    def sol(self,start, end):
        if end < start:
            return [None]

        ans = []
        for i in range(start,end + 1):
            ls = self.sol(start,i - 1)
            rs = self.sol(i + 1,end)
            for l in ls:
                for r in rs:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ans.append(root)

        return ans

    def generateTrees(self, n):
        if not n:
            return []
        return self.sol(1, n)