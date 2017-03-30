def add(name_set, contact):
    name_set.append(contact)
    return name_set

def find_partial(name_set, partial):
    m=len(partial)
    count=0
    for name in name_set:
        if partial == name[0:m]:
            count+=1
    return count


name_set = []
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op=='add':
        name_set=add(name_set, contact)
    else:
        print find_partial(name_set, contact)
