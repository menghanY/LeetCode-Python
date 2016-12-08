# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2]
# https://discuss.leetcode.com/topic/14640/simple-python-iterative-solution-by-using-a-visited-flag-o-n-56ms/2
from TreeNode import TreeNode
class Solution(object):
    def inorderTraversal(self, root):
        result,stack = [],[(root,False)]
        while stack:
            cur,visited = stack.pop()
            if cur :
                if visited :
                    result.append(cur.val)
                else:
                    stack.append((cur.right,False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return result