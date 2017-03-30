class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)


x=Solution()
print x.reverseBits(1)  #32
print x.reverseBits(00000010100101000001111010011100)
#964176192 (00111001011110000010100101000000)
