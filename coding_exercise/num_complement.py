# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # convert to binary
        # flip 0 and 1
        # convert back to num

        bstr=bin(num)
        bstr_flip=''.join([str(abs(int(x)-1)) for x in list(bstr[2:])])
        return int(bstr_flip,2)


x=Solution()
print x.findComplement(5)
print x.findComplement(1)
