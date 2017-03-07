from collections import *

def get_diffs(l):
    # given the list of number
    # calculate the total numbers needed to drop
    return sum([abs(l[i]) for i in range(len(l)) if l[i]!=0])

def number_needed(l1, l2):

    dic1=Counter(l1)
    dic2=Counter(l2)
    total_keys=set(dic1.keys()) | set(dic2.keys())
    total_dic={k:(dic1.get(k, 0), dic2.get(k, 0)) for k in total_keys}
    total_dic_diff={k:(total_dic[k][0] - total_dic[k][1]) for k in total_keys}
    total_num_to_drop=get_diffs(total_dic_diff.values())

    return total_num_to_drop



a = raw_input().strip()
b = raw_input().strip()
print number_needed(a, b)





