class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 : return s
        if len(s) <= 1 : return s
        ret = []
        chars = list(s)
        cnt = len(chars)
        charsLen = len(chars)
        for i in range(numRows) :
            myLen = 2 * numRows - 2
            index = i
            while index < cnt :
                ret.append(chars[index])
                if i != 0 and i != numRows - 1 :
                    tmpIndex = index + 2 * (numRows - i - 1)
                    if tmpIndex < cnt :
                        ret.append(chars[tmpIndex])
                index += myLen
        return ''.join(ret)

a = Solution()
print(a.convert("abcdefg",5))
