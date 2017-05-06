# class Solution(object):
#     def findRelativeRanks(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         sorted_nums=nums[:]
#         sorted_nums.sort(reverse=True)
#         dic={n: i for i, n in enumerate(sorted_nums)}
#         rank_ls=[dic[n]+1 for n in nums]
#         rank_ls2=[]
#         for n in rank_ls:
#             if n==1:
#                 rank_ls2.append('Gold Medal')
#             elif n==2:
#                 rank_ls2.append('Silver Medal')
#             elif n==3:
#                 rank_ls2.append('Bronze Medal')
#             else:
#                 rank_ls2.append(str(n))
#         return rank_ls2

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums=nums[:]
        sorted_nums.sort(reverse=True)

        rank_ls=['Gold Medal','Silver Medal','Bronze Medal'] + map(str, range(4, len(nums)+1))
        dic={n:index for (index, n) in zip(rank_ls,sorted_nums)}

        return map(dic.get, nums)



class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # return the rank index
        # replace rank index with medal

        sorted_nums = sorted(nums, reverse=True)
        dic = {}
        medal = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        for i, n in enumerate(sorted_nums):
            if i in medal:
                dic[n] = medal[i]
            else:
                dic[n] = str(i + 1)
        output = []
        for n in nums:
            output.append(dic[n])
        return output


x=Solution()
print x.findRelativeRanks([5,4,3,2,1])