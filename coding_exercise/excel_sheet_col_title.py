class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        # define a mapping {26:Z, 1:A}
        # iterate all numbers and find matching letters
        # join all together
        import string
        letters=string.ascii_uppercase
        mappings={i+1:l for i, l in enumerate(letters)}

        # EVERY digit is basically dividing by 26
        results=''
        while n>0:
            if n % 26==0:
                results=results+'Z'
                n=(n/26)-1
            else:
                results=results+mappings[n%26]
                n=int(n/26)
        return results[::-1]

x=Solution()
print x.convertToTitle(1)
print x.convertToTitle(26)
print x.convertToTitle(703)
print x.convertToTitle(1383)
