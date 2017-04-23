class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # convert n into digits
        # build a while loop
        # creates a set to record all new n

        # this algorithm takes forever to stop

        track_set=set()
        while n!=1:
            n=sum(int(x)**2 for x in str(n))
            if n in track_set:
                return False
            else:
                track_set.add(n)
        return True

x=Solution()
print x.isHappy(19)
print x.isHappy(2)


