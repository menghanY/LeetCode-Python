class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t) : return False
        sDict = {}
        tDict = {}
        for xChar in s :
            if xChar == "" : continue
            sDict[xChar] = sDict.get(xChar,0) + 1
        for xChar in t :
            if xChar == "" : continue
            tDict[xChar] = tDict.get(xChar, 0) + 1
        for i in sDict:
            if  sDict.get(i) != tDict.get(i) : return False
        return True