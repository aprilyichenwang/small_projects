

def find_next_match(n, nums):
    for i in range(len(nums)):
        if n == nums[i]:
            for j in range(i + 1, len(nums)):
                if nums[j] > n:
                    x= nums[j]
                    return x
    return -1


def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result_ls=[]
    for n in findNums:
        result_ls.append(find_next_match(n, nums))
    return result_ls

# print nextGreaterElement([-1, 1,2],[1,3,4,2])
# print nextGreaterElement([2, 4],[1,2,3, 4])


# this solution TIMED OUT

def get_next_greater_num(i, nums, curr):
    n=len(nums)
    for j in range(i+1, n):
        if nums[j]>curr:
            return nums[j]
    for j in range(0, i):
        if nums[j]> curr:
            return nums[j]
    return -1

def nextGreaterElement2(nums):
    result=[]
    for i in range(len(nums)):
        curr=nums[i]
        result.append(get_next_greater_num(i, nums, curr))
    return result


def nextGreaterElement2(nums):
    # by doubling the array,
    # I should be able to apply the method in nextGreaterElement1
    # to solve the problem. although i am seeing a bug there

    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result_ls=[]
    for n in nums:
        result_ls.append(find_next_match(n, nums*2))
    return result_ls


def nextGreaterElement(self, findNums, nums):
    def helper(num):
        for tmp in nums[nums.index(num):]:
            if tmp > num:
                return tmp
        return -1

    return map(helper, findNums)


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        for n in findNums:
            i=nums.index(n)
            ls_right=nums[i+1:]
            nu=-1
            for x in ls_right:
                if x>n:
                    nu=x
                    break
            ls.append(nu)
        return ls



# how to deal with the list circulation
print nextGreaterElement2([1,2,1])