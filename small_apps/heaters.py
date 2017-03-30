
# For each house find distance to closest heater.
# Take the max distance of these which is the radius needed.


class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        j,radius = 0,0
        for house in houses:
            while j+1 < len(heaters) and abs(heaters[j+1]-house) <= abs(heaters[j]-house):
                j += 1
            radius = max(radius,abs(heaters[j]-house))
        return radius





x=Solution()
# print x.findRadius([1,2,3],[2])
# print x.findRadius([1,2,3,4],[1,4])
print x.findRadius([4,5],[2])