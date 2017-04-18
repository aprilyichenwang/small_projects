class Solution(object):
    def isPalindrome(self, x):    # 66 77 111 121 232
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        i=0
        while len(x)>=1:
            if x[i]==x[-1-i]:
                x=x[1:-1]
            else:
                return False
        return True

x=Solution()
print x.isPalindrome(-2147483648)
print x.isPalindrome(214412)
print x.isPalindrome(21412)