
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
                # be careful, string replace will replace all occurances
                # while list remove function only removes the first occurance
            else:
                return False
        return True





x=Solution()
print x.canConstruct('a','b')
print x.canConstruct('aa','ab')
print x.canConstruct('aa','aab')
