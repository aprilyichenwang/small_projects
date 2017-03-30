from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic=Counter(nums)
        return list(set([n for n in nums if dic[n]==2]))



