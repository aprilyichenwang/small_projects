class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # num dividable by 2, or 3 or 5
        # create a list to be divided
        # keep dividing if possible, until run out of all 2s
        # then try 3
        # if so, divided by them and keep iterating

        if num <= 0: return False
        else:
            num_to_be_divided=[2,3,5]
            for x in num_to_be_divided:
                while num % x == 0:
                    num = num / x
            return num == 1

