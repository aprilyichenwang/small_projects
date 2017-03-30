class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for W in range(int(area**0.5),0,-1):
            L=area/W
            if W*L==area:
                return [L, W]

x=Solution()
print x.constructRectangle(4)
