# The Hamming distance between two integers
# is the number of positions at which the corresponding
# bits are different.

# given two integers x, y, calcualte humming distance

# d1=min(x,y)
# d2=max(x,y)
# db1=binary(d1)[2:]
# db2=binary(d2)[2:]

# left pad db1 with 0s to match the binary length of db2
# zfill(xc, len(yc))

# diff=0
#for i in range(len(db1)):
# if db1[i]!=db2[i]:
#     diff+=1
# return diff




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
