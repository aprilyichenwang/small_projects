import sys
from collections import Counter

def lonely_integer(a):
    dic=Counter(a)
    for k, v in dic.items():
        if v==1:
            return k


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
print lonely_integer(a)
