# Binary Tree Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes' values
from TreeNode import TreeNode
class Solution(object):
    def preorderTraversal(self, root):
        nodeList = []
        def dfs(treeNode):
            if treeNode :
                nodeList.append(treeNode.val)
                dfs(treeNode.left)
                dfs(treeNode.right)
        dfs(root)
        return nodeList

