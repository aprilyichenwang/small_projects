class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        count_ls=[]
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if i==len(nums)-1:
                    count_ls.append(count)
            else:
                count_ls.append(count)
                count=0
        return max(count_ls)



class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans


x=Solution()
print x.findMaxConsecutiveOnes([1])  # 1
print x.findMaxConsecutiveOnes([1,1,0,1,1,1])  # 3
print x.findMaxConsecutiveOnes([0,1]) #1

