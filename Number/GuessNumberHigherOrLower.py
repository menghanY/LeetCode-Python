# https://leetcode.com/problems/guess-number-higher-or-lower/
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!

def guess(num,x):
    pass
class Solution(object):
    def guessNumber(self, n):
        begin,end = 1,n
        while True:
            curNum = (begin + end) // 2
            curBool = guess(curNum)
            if curBool == 1:
               end = curNum - 1
            elif curBool == -1:
               begin = curNum + 1
            else:
                return curNum