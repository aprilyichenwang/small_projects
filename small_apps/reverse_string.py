def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    return "".join([s[i] for i in range(len(s)-1, -1,-1)])

print reverseString('hello')