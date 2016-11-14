class Solution(object):
    def addDigits(self, num):
        if num < 10 : return num
        tNum = num
        tSum = 0
        while tNum > 0 :
            tSum += tNum % 10
            tNum = tNum // 10
        return self.addDigits(tSum)