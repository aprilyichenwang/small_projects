from itertools import combinations

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # all from top
        # all from bottom
        # pair
        time=[]
        r0=min(4, num)
        for x in range(r0+1):
            hs=tuple(combinations([1,2,4,8], x))
            r1=min(6, num-x)
            for m in range(r1+1):
                ms=(tuple(combinations([32,16,8,4,2,1], m)))
            hours=[sum(h) for h in hs]
            mins=[sum(t) for t in ms]
            time.extend(['%s:%s'%(h,str(m).zfill(2)) for m in mins for h in hours ])
        return list(set(time))


x=Solution()
print x.readBinaryWatch(2)