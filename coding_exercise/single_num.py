from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=Counter(nums)
        return [n for n in nums if a[n]==1][0]


def singleNumber2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = Counter(nums)
    return [n for n in nums if a[n] == 1][0]


def singleNumber3(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = Counter(nums)
    return [n for n in nums if a[n] == 1]
