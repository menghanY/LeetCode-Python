class Solution(object):
    def findDuplicates(self, nums):
        li = []
    	for i,val in enumerate(nums):
    	    if nums[abs(val)-1] > 0:
                nums[abs(val)-1] = -abs(nums[abs(val)-1])
    	    else:
                li.append(abs(val))
    	return li