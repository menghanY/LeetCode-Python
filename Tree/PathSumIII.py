#https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
from TreeNode import TreeNode
class Solution(object):
    def pathSum1(self, root, target):
        self.count = 0
        preDict = {0:1}
        def dfs(subRoot,target,pathSum,preDict):
            if subRoot:
                pathSum += subRoot.val
                self.count += preDict.get(pathSum - target,0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(subRoot.left, target, pathSum, preDict)
                dfs(subRoot.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root,target,0,preDict)
        return self.count

    def pathSum2(self,root,target):
        if not root : return 0
        def dfs(root,target):
            if not root : return 0
            ret = 0
            if root.val == target : ret += 1
            ret += dfs(root.left,target - root.val) + dfs(root.right,target - root.val)
            return ret
        ret = dfs(root,target) + self.pathSum2(root.left,target) + self.pathSum2(root.right,target)
        return ret



# root = TreeNode(10)
#
# root1 = TreeNode(5)
#
# root2 = TreeNode(-3)
#
# root3 = TreeNode(3)
#
# root4 = TreeNode(2)
#
# root5 = TreeNode(11)
#
# root6 = TreeNode(3)
#
# root7 = TreeNode(-2)
#
# root8 = TreeNode(1)
# root.left = root1
# root.right = root2
# root1.left = root3
# root1.right = root4
# root2.right = root5
# root3.left = root6
# root3.right = root7
# root4.right = root8