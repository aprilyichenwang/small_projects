class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while abs(3**i) <=n:
            if abs(3**i)==n:
                return True
            i+=1
        return False






