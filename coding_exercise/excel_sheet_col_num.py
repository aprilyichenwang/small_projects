class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        LETTERS=string.ascii_uppercase
        col_num = 0
        for i in s:
            col_num = col_num * 26 + (LETTERS.index(i)+1)
        return col_num




x=Solution()
print x.titleToNumber('A')  # 26*0+1
print x.titleToNumber('B')  # 26*0+1
print x.titleToNumber('AA')  # 26*1+1
print x.titleToNumber('AB')  # 28    = 26*1+2
print x.titleToNumber('BA')  # 26*2+1
print x.titleToNumber('AAA')  # this comes after 'ZZ' 26*26+1
