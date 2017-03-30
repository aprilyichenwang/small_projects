class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        happy=0
        i=0
        j=0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
               happy+=1
               i+=1
               j+=1
            else:
                i+=1
        return happy


x=Solution()
print x.findContentChildren([1,2,3],[1,1])
