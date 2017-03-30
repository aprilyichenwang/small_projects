class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if (word.upper()==word) or (word.lower()==word):
            return True
        elif (word.capitalize()==word) & (len(word)>0):
            return True
        else:
            return False

