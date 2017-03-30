# from collections import *
#
# def ransom_note(magazine, ransom):
#     '''
#
#     :param magazine: a list of words in the magzine
#     :param ransom: a list of words in the ransom
#     :return: 1 or 0
#     '''
#     # m, the num_words in magazine
#     # n, the num of words in random note
#     mag_dic=Counter(magazine)
#     random_dic=Counter(ransom)
#     for word in random_dic:
#         try:
#             count_mag=mag_dic[word]
#         except:
#             return 0
#         if count_mag < random_dic[word]:
#             return 0
#     return 1
#
#
#
# m, n = map(int, raw_input().strip().split(' '))
# magazine = raw_input().strip().split(' ')
# ransom = raw_input().strip().split(' ')
# answer = ransom_note(magazine, ransom)
# if (answer):
#     print "Yes"
# else:
#     print "No"


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote=list(ransomNote)
        magazine=list(magazine)
        for l in ransomNote:
            if l in magazine:
                magazine.remove(l)
            else:
                return False
        return True


x=Solution()
print x.canConstruct('a','b')
print x.canConstruct('aa','ab')
print x.canConstruct('aa','aab')
