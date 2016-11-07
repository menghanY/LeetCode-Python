import math
class Solution(object):
    def isPowerOfThree1(self, n):
        return math.log10(n) // math.log10(3) % 1 == 0
    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        if n == 1: return True

        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3

        return True