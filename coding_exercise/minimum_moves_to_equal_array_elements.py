# class Solution(object):
#     def minMoves(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         num_moves=0
#         while True:
#             nums.sort()
#             if sum(nums[0:-1])==nums[0]*(len(nums)-1):
#                 num_moves+=nums[-1]-nums[0]
#                 return num_moves
#
#             else:
#                 if sum(nums)==len(nums)*nums[0]:
#                     return num_moves
#                 nums=[n+1 for n in nums[0:-1]]+[nums[-1]]
#                 num_moves+=1

# Incrementing all but one is equivalent to decrementing that one.
# So let's do that instead. How many single-element decrements to make all equal?
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)


x=Solution()
print x.minMoves([1,2,3])
print x.minMoves([1,1,1])
print x.minMoves([1,2147483647])
