class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # convert number, index into a {num: index}
        # iterate through n in nums:
        # return index if match is found

        dic = {num: i for i, num in enumerate(numbers)}
        for i, n in enumerate(numbers):
            if target - n in dic:
                return i + 1, dic[target - n] + 1


x=Solution()
print x.twoSum([2,7,11,15],9)
print x.twoSum([2,3,4],6)