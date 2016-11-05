class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t) : return False
        sDict = {}
        tDict = {}
        for xChar in s :
            if xChar == "" : continue
            if sDict.get(xChar) : sDict[xChar] += 1
            else :               sDict[xChar] = 1
        for xChar in t :
            if xChar == "" : continue
            if tDict.get(xChar) : tDict[xChar] += 1
            else :               tDict[xChar] = 1
        for i in sDict:
            if  sDict.get(i) != tDict.get(i) : return False
        return True