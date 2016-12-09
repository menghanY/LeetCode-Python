def guess(num,x):
    pass
class Solution(object):
    def guessNumber(self, n):
        begin,end = 1,n
        while True:
        curNum = (begin + end) // 2
        curBool = guess(curNum)
        if curBool == 1:
            end = curNum - 1
        elif curBool == -1:
            begin = curNum + 1
        else:
            return curNum