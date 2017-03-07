
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    dic = {'a': 'u', 'e': 'o', 'o': 'e', 'u': 'a'}
    return ''.join([dic.get(s[i], s[i]) if s[-i-1] in dic else s[i] for i in range(len(s))])


print reverseVowels('hello')
print reverseVowels('leetcode')