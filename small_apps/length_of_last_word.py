class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        w_ls=s.strip().split(' ')
        return len(w_ls[-1])