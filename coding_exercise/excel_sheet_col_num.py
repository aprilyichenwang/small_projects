class Solution(object):
    # def titleToNumber(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     import string
    #     LETTERS=string.ascii_uppercase
    #     col_num = 0
    #     for i in s:
    #         col_num = col_num * 26 + (LETTERS.index(i)+1)
    #     return col_num


    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        LETTERS = string.ascii_uppercase
        mapping={l:(i+1) for i, l in enumerate(LETTERS)}
        col = 0
        for i in range(len(s)):
            m=len(s)-i  # reverse the index
            col=col+(mapping[s[i]])*(26**(m-1))
        return col


x=Solution()
print x.titleToNumber('A')  # 26*0+1
print x.titleToNumber('B')  # 26*0+2
print x.titleToNumber('AA')  # 26*1+1=27
print x.titleToNumber('AB')  # 28    = 26*1+2
print x.titleToNumber('BA')  # 26*2+1=53
print x.titleToNumber('AAA')  # 703
print x.titleToNumber('BAE')  #1383