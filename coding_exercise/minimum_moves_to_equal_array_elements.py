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


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # evaluate whether all elements are equal
        # if not, increment
        # if yes, return n_step required to do so

        def evaluate(array):
            if len(set(array)) == 1:
                return True

        ans = 0
        n = len(nums)
        while not evaluate(nums):
            nums = sorted(nums)
            nums = map(lambda x: x + 1, nums[0:n]) + [nums[-1]]
            print nums
            ans += 1
        return ans



x=Solution()
print x.minMoves([1,2,3])
# print x.minMoves([1,1,1])
# print x.minMoves([1,2147483647])
