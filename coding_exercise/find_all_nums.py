class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        return list(set(range(1, n+1))-set(nums))


x=Solution()
print x.findDisappearedNumbers([4,3,2,7,8,2,3,1])
