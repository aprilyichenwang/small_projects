class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        str_ls=map(lambda x: tuple(x), strs)
        len_words=map(lambda x: len(x), str_ls)
        i=1
        track=0
        while i<=min(len_words):
            if map(lambda x: x[0:i], str_ls)==[str_ls[0][0:i]]*len(strs):
                track+=1
            i+=1
        return strs[0][0:track]





x=Solution()
# print x.longestCommonPrefix(['abcd','dafsd'])
# print x.longestCommonPrefix(['abcd','abfsd'])
print x.longestCommonPrefix(['a'])
print x.longestCommonPrefix(['c','c'])



