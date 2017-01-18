from TreeNode import TreeNode
class BSTIterator(object):
    def __init__(self, root):
        def _dfs(node):
            if not node:
                return
            for x in _dfs(node.left):
                yield x
            yield node.val
            for x in _dfs(node.right):
                yield x

        self.iterator = _dfs(root)
        self._next = None

    def hasNext(self):
        try:
            self._next = next(self.iterator)
            return True
        except StopIteration:
            return False
    def next(self):
        return self._next
