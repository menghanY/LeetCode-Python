from functools import reduce
class Solution(object):
    def addStrings(self, num1, num2):
        def charNum(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        def numChar(n):
            return {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}[n]
        def stringToNum(numStr):
            return reduce(lambda x,y:x * 10 + y,map(charNum,numStr))
        sumNum = stringToNum(num1) + stringToNum(num2)
        if sumNum == 0 : return "0"
        result = ''
        while sumNum > 0 :
            result = numChar(sumNum % 10) + result
            sumNum //= 10
        return result
s = Solution()
s.addStrings('0','0')


