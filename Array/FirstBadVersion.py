# https://leetcode.com/problems/first-bad-version/
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def isBadVersion(version):
    return version > 2
def firstBadVersion(n):
    if n == 1: return 1
    beginV = 1
    endV = n
    while beginV < endV:
        currentV = (beginV + endV) // 2
        if isBadVersion(currentV):
            endV = currentV - 1
            if isBadVersion(endV) == False:
                return currentV

        else:
            beginV = currentV + 1
    return endV
