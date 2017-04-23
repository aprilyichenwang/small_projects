# Given a string, you need to reverse the order of characters
#  in each word within a sentence while still preserving whitespace and initial word order.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # break s into words
        # reverse by word
        # outout
        words_ls=s.split(' ')
        words_ls_rev = [x[::-1] for x in words_ls]
        return ' '.join(words_ls_rev)

x=Solution()
print x.reverseWords("Let's take LeetCode contest")
