class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find max of nums
        # creates a list of 0- num
        # return the set difference
        s= list(set(range(len(nums)+1))-set(nums))
        return s[0]


x=Solution()
print x.missingNumber([0,1,3])
print x.missingNumber([0])
print x.missingNumber([0,1])
