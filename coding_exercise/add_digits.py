# class Solution(object):
#     def add_str(self, num):
#         n_ls=list(str(num))
#         return sum(map(lambda x: int(x), n_ls))
#
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         while len(str(num))>1:
#             num=self.add_str(num)
#         return num



# Why this works much slower?
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num=sum(map(lambda x: int(x), str(num).split()))
        return num


x=Solution()
print x.addDigits(10)