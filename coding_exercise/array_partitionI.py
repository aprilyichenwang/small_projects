# Given an array of 2n integers, your task is to group these integers
# into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn)
# which makes sum of min(ai, bi) for all i from 1 to n as large as possible.




# sort the array
# sum=0
# for i in range(n):
    # if i%2==0:
        # sum=sum+=array[i]
# return sum





class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        ls=[]
        for i in range(len(nums)):
            if i%2==0:
                ls.append(nums[i])
        return sum(ls)


x=Solution()
print x.arrayPairSum([1,4,3,2])
