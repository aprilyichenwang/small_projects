class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        ls=[]
        dic=Counter(s)
        for key in dic:
            if dic[key]==1:
                ls.append(list(s).index(key))
        if len(ls)>0:
            return min(ls)
        else:
            return -1


x=Solution()
print x.firstUniqChar('')
print x.firstUniqChar('leetcode')
print x.firstUniqChar('loveleetcode')