from TreeNode import TreeNode
class Solution(object):
    def isSymmetric(self, root):
        if root :
            return self.isMirror(root.left,root.right)
        else:
            return True
    def isMirror(self,left,right):
        if left == None and right == None:
            return True
        elif left != None and right != None :
            return left.val == right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
        else:
            return False

