class Solution(object):
    def titleToNumber(self, s):
        sLen = len(s) - 1
        num = 0
        for charS in s :
            num += 26 ** sLen * (ord(charS) - 64)
            sLen -= 1
        return num


