import string


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

# no two characters can be mapped into the same

    s=list(s)
    t=list(t)
    mapping={}
    chars=list(string.printable)
    for i in range(len(s)):
        if s[i] not in mapping:
            if t[i] in chars:   # value not assigned yet
                mapping[s[i]]=t[i]
                chars.remove(t[i])
            else:  # value already assigned
                return False
        elif mapping[s[i]]!=t[i]:
            return False
    return True



# print isIsomorphic('egg','add')
# print isIsomorphic('foo','bar')
# print isIsomorphic('paper','title')
# print isIsomorphic('ab','aa')
# print isIsomorphic('aab','aaa')



# All occurrences of a character must be replaced with another
# character while preserving the order of characters.
# No two characters may map to the same character but a character may
# map to itself.

# For example,
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.


def isIsomorphic2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return len(set(zip(s, t)))==len(set(s)) &  len(set(zip(s, t)))==len(set(t))

print isIsomorphic2('egg','add')
print isIsomorphic2('foo','bar')
print isIsomorphic2('paper','title')
print isIsomorphic2('ab','aa')
print isIsomorphic2('aab','aaa')