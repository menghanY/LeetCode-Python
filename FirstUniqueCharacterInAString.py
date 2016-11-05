class Solution(object):
    def firstUniqChar(self, s):
        numDict = {}
        for charS in s:
            if numDict.get(charS) : numDict[charS] += 1
            else :              numDict[charS] = 1
        num = 0
        for charS in s:
            if numDict.get(charS) == 1 :
                return num
            num += 1
        return -1

s =Solution()
print(s.firstUniqChar("loveleetcode"))