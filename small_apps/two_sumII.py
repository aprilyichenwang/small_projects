# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         result=[]
#         for j, key in enumerate(numbers):
#             for i in range(j+1,len(numbers)):
#                 if key+numbers[i]==target:
#                     result.append(j+1)
#                     result.append(i+1)
#                     return result
#
#
# x=Solution()
# print x.twoSum([2,7,11,15],9)
# print x.twoSum([2,3,4],6)


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1

x=Solution()
print x.twoSum([2,7,11,15],9)
print x.twoSum([2,3,4],6)