
def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    def evaluate(str):
        for i in range(len(str)/2):
            if str[i]!=str[-i-1]:
                return 0
        return 1

    result_set=[]
    for i, word in enumerate(words):
        for j in range(len(words)):
            if i!=j:
                str=words[i]+words[j]
                if evaluate(str):
                    result_set.append([i, j])
    return result_set


print palindromePairs(["bat", "tab", "cat"])
print palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])