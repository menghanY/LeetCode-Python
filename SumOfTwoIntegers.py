class Solution(object):
    def getSum(self, a, b):
        xa = a
        xb = b
        while xb != 0 :
            (xa,xb) = (xa^xb,(xa&xb)<<1)
        return xa
s = Solution()
print(s.getSum(10,15))