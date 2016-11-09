class Solution(object):
    def firstUniqChar(self, s):
        numDict = {}
        for charS in s:
            numDict[charS] = numDict.get(charS,0) + 1
        num = 0
        for charS in s:
            if numDict.get(charS) == 1 :
                return num
            num += 1
        return -1

s =Solution()
print(s.firstUniqChar("loveleetcode"))