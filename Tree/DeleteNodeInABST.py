from TreeNode import TreeNode
class Solution(object):
# https: // discuss.leetcode.com / topic / 68920 / bottom - up - recursive - python - solution - o - log - n - time
    def deleteNode(self, root, key):
        if not root: return None
        if root.val > key :
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left:
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                left_right_most.right = root.right

                return root.left
            else:
                return root.right

        return root