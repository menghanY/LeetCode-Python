# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution(object):
    def kthSmallest(self, matrix, k):
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right :
            mid = left + (right - left) // 2
            cnt = self.search_less_equal(matrix,mid)
            if cnt < k :
                left = mid + 1
            else:
                right = mid

        return left

    def search_less_equal(self,matrix,target):
        n = len(matrix)
        i = n - 1
        j = 0
        res = 0

        while i >= 0 and j < n :
            if matrix[i][j] <= target :
                res += i + 1
                j += 1
            else:
                i -= 1

        return res
