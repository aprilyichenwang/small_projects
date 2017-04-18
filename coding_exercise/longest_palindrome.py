# s consists upper and lower case
# find the longest palindrom that can be built with these letters

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls=[]
        count=0
        for i in range(len(s)):
            if s[i] not in ls:
                ls.append(s[i])
            else:
                ls.remove(s[i])
                count+=2
        if len(ls)>= 1: count+=1
        return count


x=Solution()
print x.longestPalindrome('abccccdd')
print x.longestPalindrome('abccbae')
