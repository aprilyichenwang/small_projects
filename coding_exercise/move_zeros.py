class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(lambda x, y: 0 if y else -1)
        return nums





class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)



# A few notes:
# when using while loop, it is important to set up the stopping point
# .pop() involve the concept of pointer
# see whether ls.remove() will perform the same task first


x=Solution()
print x.moveZeroes([3,-1,0,2,8,0,4])