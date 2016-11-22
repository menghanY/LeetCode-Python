# Definition for a binary tree node.

# https://discuss.leetcode.com/topic/50229/python-simple-non-dfs-solution-commented
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.result = []
    def binaryTreePaths(self, root):
        self.find_paths(root,[])
        return self.result
    def find_paths(self,node,current_path):
        if node :
            current_path.append(node.val)
            print(current_path)
            if not node.left and not node.right:
                print('none')
                self.result.append("->".join([str(x) for x in current_path]))
            else:
                print('left')
                self.find_paths(node.left,current_path)

                print('right')
                self.find_paths(node.right, current_path)
            print("pop")
            current_path.pop()


treeNode5 = TreeNode(5)
treeNode2 = TreeNode(2)
treeNode1 = TreeNode(1)
treeNode3 = TreeNode(3)

treeNode1.left = treeNode2
treeNode1.right = treeNode3
treeNode2.right = treeNode5

s =Solution()
print(s.binaryTreePaths(treeNode1))

