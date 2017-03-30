class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # note, range(2, 2)=[]
        dic={}
        for i, n in enumerate(nums):
            if n not in dic:
                dic[n]=i
            else:
                if i-dic[n]<=k:
                    return True
                else:
                    dic[n]=i

        return False


x=Solution()
print x.containsNearbyDuplicate([1,0,1,1],1)  # true
