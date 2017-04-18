class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        if len(s)==1:
            return 1
        string_ls=[]
        string=''
        for i in range(0,len(s)):
            if s[i] not in string:
                string+=s[i]
                if i==len(s)-1:
                    string_ls.append(string)
            else:
                string_ls.append(string)
                string=s[i]
        string_lenth=map(lambda x: len(x), string_ls)
        return max(string_lenth)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=max_length=0
        dic={}
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:  # this makes sure that i-start>0
                start=dic[s[i]]+1
            else:
                max_length = max(max_length, i - start+1)
            dic[s[i]]=i
        return max_length


x=Solution()
print x.lengthOfLongestSubstring('abcabcbb')  # 3
print x.lengthOfLongestSubstring('bbbbb')  # 1
print x.lengthOfLongestSubstring('pwwkew') # 3
print x.lengthOfLongestSubstring('') # 0
print x.lengthOfLongestSubstring('s') # 1
print x.lengthOfLongestSubstring('au')# 2
print x.lengthOfLongestSubstring('dvdf') # 3
print x.lengthOfLongestSubstring('tmmzuxt') # 6