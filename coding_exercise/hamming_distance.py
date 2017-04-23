class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # convert x, y into bits
        # compare two lists and find the total number of position difference

        x=bin(x)[2:]
        y=bin(y)[2:]

        x=x.zfill(max(len(x),len(y)))
        y=y.zfill(max(len(x),len(y)))

        df=0
        # start from right to left
        for i in range(len(x)):
            if x[i]!=y[i]:
                df+=1
        return df

x=Solution()
print x.hammingDistance(1,4)
print x.hammingDistance(4,14)
