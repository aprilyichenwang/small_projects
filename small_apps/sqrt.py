class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        find the square root of x, not using packages
        """
        l=0
        r=x
        while l<=r:
            mid = (l+r) // 2
            if mid**2 <= x <(mid+1)**2:
                return mid
            elif mid**2 > x:
                r=mid
            else:
                l+=1



x=Solution()
print x.mySqrt(26)
print x.mySqrt(35)
print x.mySqrt(49)
