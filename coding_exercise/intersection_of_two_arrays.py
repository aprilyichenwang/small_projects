# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         return list(set(nums1) & set(nums2))

def remove(l1, l2):
    ls=[]
    for l in l1:
        if l in l2:
            ls.append(l)
            l2.remove(l)
    return ls


# interaction of two array II - METHOD1
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len1=len(nums1)
        len2=len(nums2)
        if len1<=len2:
            return remove(nums1, nums2)
        else:
            return remove(nums2, nums1)


# interaction of two array II - METHOD2
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ls=[]
        a, b =map(Counter, (nums1, nums2))
        for num in a & b:
            ls.extend([num]*min(a[num],b[num]))
        return ls


x=Solution()
print x.intersect([1,2,2,1],[2,2])
print x.intersect([3,1,2],[1,1])