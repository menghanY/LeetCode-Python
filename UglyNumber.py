class Solution(object):
    def isUgly(self, num):
        while True :
            if num == 0: return False
            if num == 1: return True
            if num % 2 == 0 :
                num = num // 2
                continue
            if num % 3 == 0 :
                num = num // 3
                continue
            if num % 5 == 0 :
                num = num // 5
                continue
            return False