class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False

        numberList = list(str(x))
        print(numberList)

        for i in range(len(numberList) // 2):
            if numberList[i] != numberList[len(numberList) - 1 - i] :
                return False
        return True

a = Solution()
print(a.isPalindrome(1011))
