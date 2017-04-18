# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

def evaluate(s):
    while len(s)>0:
        if s[0]==s[-1]:
           s=s[1:-1]
        else:
           return False
    return True



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        s=s.lower()
        s1=''.join((map(lambda x: x if x in (string.lowercase + string.digits) else '', s)))
        return evaluate(s1)


# Method2
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        s=s.lower()
        s=''.join(map(lambda x: x if x in (string.lowercase + string.digits) else '',s))
        return s==s[::-1]



x=Solution()
print x.isPalindrome('') # True
print x.isPalindrome(' ')  # True
print x.isPalindrome('a')
print x.isPalindrome('aa')
print x.isPalindrome('0p')