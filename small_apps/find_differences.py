class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t=list(t)
        for c in s:
            t.remove(c)
        return t[0]
x=Solution()
print x.findTheDifference('abcd','abcde')
print x.findTheDifference('a','aa')

