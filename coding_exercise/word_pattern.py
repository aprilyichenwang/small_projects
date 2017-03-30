def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    s=str.split(' ')
    if len(s)!=len(pattern):
        return False
    return (len(set(zip(pattern, s)))==len(set(pattern))) & (len(set(zip(pattern, s)))==len(set(s)))



print wordPattern('abba','dog cat cat dog')
# print wordPattern('abba','dog cat cat fish')
# print wordPattern('aaaa','dog cat cat dog')
# print wordPattern('abba','dog dog dog dog')
print wordPattern('aba','cat cat cat dog')

