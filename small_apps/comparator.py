

def sorted(data):
    '''

    :param data: a list of tuples
    :param cmp: method defined
    :return: a list of Player() object, which is like a tuple
    '''
    dic={}
    for i in range(len(data)):
        dic[data[i][0]]=data[i][1]  # convert tuples to a dictionary(subject to existing code)
    scores=dic.values()  #
    # sort names_ls, then mark the index
    scores.sort(reverse=True)

    # since we can have multiple users having the same users, we append user name given the same score
    reversed_dic={score:[] for name, score in dic.items()}
    for name, score in dic.items():
        reversed_dic[score].append(name)
        reversed_dic[score].sort()

    # sort the list by name (we also compare name alphabetically, for the same score)
    names_sorted=[reversed_dic[score] for score in scores] # return a list of name lists, given the sorted scores

    # return a list of unique names, while maintaining the order
    names_sorted_s=[]
    for x in names_sorted:
        if x not in names_sorted_s:
            names_sorted_s.append(x)

    # flatten the names_sorted_list
    names_sorted_s=[y for x in names_sorted_s for y in x]

    # return the sorted data
    data_sorted=[(names_sorted_s[i], dic[names_sorted_s[i]]) for i in range(len(scores))]
    return data_sorted



n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()   # name='amy', score=100
    score = int(score)
    data.append((name, score))   # a list of tuples

data = sorted(data)  # sort data(a list of tuples?)
print "-------- sorted result -------"
for i in data:
    print i[0],i[1]
