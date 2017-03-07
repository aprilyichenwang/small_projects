class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for word in words for row in (set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')) if set(word.lower())<= row]

# set(['qwertyuiop'])
# set(['asdfghjkl'])
# set(['zxcvbnm'])


Solution.findWords(["Hello", "Alaska", "Dad", "Peace"])


# please note (different)
# set('qwertyuiop')  # {'e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y'}
# set(['qwertyuiop']) # {'qwertyuiop'}
