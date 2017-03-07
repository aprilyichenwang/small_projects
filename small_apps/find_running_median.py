import sys

def find_median(a):
    if len(a)%2==1:
        return a[(len(a)-1)/2]
    else:
        return (a[len(a)/2 - 1]+a[len(a)/2])*1.0/2



n = int(raw_input().strip())  # total num
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)   # a_t is added to the list a
    median=find_median(a)
    print round(median, 1)




