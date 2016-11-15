# https://leetcode.com/problems/plus-one/
# Given a non-negative number represented as an arraydigit is at the head of the list. of digits, plus one to the number.
#
# The digits are stored such that the most significant

class Solution(object):
    def plusOne(self, digits):
        plusNum = 1
        for i in range(0, len(digits))[::-1]:
            temp = digits[i] + plusNum
            digits[i] = temp % 10
            plusNum = temp // 10
            if plusNum == 0 : return digits
        digits.insert(0,plusNum)
        return digits



s = Solution()
print(s.plusOne([8,9,9]))