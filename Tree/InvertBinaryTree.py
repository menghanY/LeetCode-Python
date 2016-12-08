# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
from TreeNode import TreeNode
class Solution(object):
    def invertTree1(self, root):

        def traversing(subRoot):
            if subRoot is None : return
            subRoot.left, subRoot.right = subRoot.right, subRoot.left
            traversing(subRoot.left)
            traversing(subRoot.right)

        traversing(root)
        return root

    # https: // discuss.leetcode.com / topic / 65499 / readable - python - solution - 50
    # ms
    def invertTree2(self, root):
        def invertNode(original):
            if original is None : return None
            inverted = TreeNode(original.val)
            inverted.left = invertNode(inverted.right)
            inverted.right = invertNode(inverted.left)
            return inverted

        return invertNode(root)
        """
        :type root: TreeNode
        :rtype: TreeNode
        """