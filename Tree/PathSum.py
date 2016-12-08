from TreeNode import TreeNode

class Solution(object):
    def __init__(self):
        self.isFinish = False
    def hasPathSum(self, root, sumPath):
        return self.find_paths(root,[],sumPath) != None or self.isFinish
    def find_paths(self,node,current_path,sumPath):
        if self.isFinish : return True
        if node :
            current_path.append(node.val)
            if not node.left and not node.right:
               if sumPath == sum(current_path) : self.isFinish = True
            else:
                self.find_paths(node.left,current_path,sumPath)
                self.find_paths(node.right,current_path,sumPath)

            current_path.pop()
