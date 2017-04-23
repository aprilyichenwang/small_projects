import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0: return False
        i=0
        while 2**i<=n:
            if 2**i==n:
                return True
            i+=1
        return False


x=Solution()
print x.isPowerOfTwo(2)
print x.isPowerOfTwo(16)
print x.isPowerOfTwo(15)
print x.isPowerOfTwo(64)