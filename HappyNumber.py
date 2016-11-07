class Solution(object):
    def isHappy(self, n):
        x = n
        inLoop = set()
        while x not in inLoop :
            inLoop.add(x)
            sumX = 0
            while x > 0:
                sumX += (x % 10) ** 2
                x //= 10
            if sumX == 1 : return True
            x = sumX
        return False