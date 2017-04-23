class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # reach time limit
        ls=[]
        nums=sorted(nums)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (k== nums[j]-nums[i]) and ((set([nums[j],nums[i]]) not in ls)):
                    ls.append(set([nums[j],nums[i]]))
        return len(ls)


    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        if k==0:
            return len(set(filter(lambda x: collections.Counter(nums)[x]> 1, nums)))
        elif k>0:
            return len(set(nums) & set([k+x for x in nums]))
        else:
            return 0


x=Solution()
print x.findPairs([3,1,4,1,5],2) # 2
# print x.findPairs([1,2,3,4,5],1)  # 4
# print x.findPairs([1,1,1,1,1],0)
