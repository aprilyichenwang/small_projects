# Given a sorted array, remove the duplicates in place
# such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in
# place with constant memory.

# change nums in place
# return the number of unique letters

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i=1
        val=nums[0]
        while i<len(nums):
            if nums[i]==val:  # i walk through each element of the list and compare with val, if match is found, pop out the first one
                nums.pop(i)
            else:
                val=nums[i]  # if no match found, val goes to that index
                i+=1
        return len(nums)





x=Solution()
print x.removeDuplicates([1,1,1])
# print x.removeDuplicates([1,1,2])
#
# print x.removeDuplicates([1,2,2,3,4,1,2])

