class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # One is not allowed to remove elements from the list while looping
        # over it. however, we can simply make a copy of it
        for n in nums[:]:  # iterate through a copy of the array works
            if n==val:
                nums.remove(n)


x=Solution()
#x.removeElement([3,2,2,3],3)
x.removeElement([3,3],3)

