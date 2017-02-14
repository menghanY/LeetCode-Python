#https://leetcode.com/problems/find-mode-in-binary-search-tree/
import collections
class Solution(object):
    # https: // discuss.leetcode.com / topic / 77062 / simple - python - explanation
    def findMode(self, root):
        if not root: return []
        count = collections.Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == max_ct]


