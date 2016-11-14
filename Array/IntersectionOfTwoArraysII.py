class Solution(object):
    def intersect(self, nums1, nums2):
        dict = {}
        resultArray = []
        for num in nums1:
            dict[num] = dict.get(num, 0) + 1
        print(dict)
        for num in nums2:
            if  dict.get(num,0) != 0 :
                dict[num] = dict.get(num, 0) - 1
                resultArray.append(num)
        return resultArray
s = Solution()
print(s.intersect([1,2,3,2,3],[1,1,2,2,2]))