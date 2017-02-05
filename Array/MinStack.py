# https://leetcode.com/problems/min-stack/
# https://discuss.leetcode.com/topic/74505/simple-python-solution-with-o-1-time-complexity-and-o-n-space-complexity
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)

        if self.min and self.min[-1] < x:
            self.min.append(self.min[-1])
        else:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return False
        else:
            return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]