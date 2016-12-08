# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Definition for a binary tree node.
from TreeNode import TreeNode
class Solution(object):
    def isBalanced1(self, root):
        def TreeDepth(nodeRoot):
            if not nodeRoot  : return 0
            tLeft = TreeDepth(root.left)
            tRight = TreeDepth(root.right)
            return tLeft + 1 if tLeft > tRight else tRight + 1
        if not root : return True
        tLeft = TreeDepth(root.left)
        tRight = TreeDepth(root.right)
        if abs(tLeft-tRight) > 1 : return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def isBalanced2(self, root):
        if not root:
            return True
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if abs(left-right)>1:
                raise Exception
            return max(left, right)+1
        try:
            return abs(depth(root.left)-depth(root.right))<=1
        except:
            return False



