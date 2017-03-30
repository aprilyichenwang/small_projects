# import itertools
#
# def get_flavors(m, a, n):
#     '''
#
#     :param m: total money to be spent
#     :param a: a list of each flavor's cost
#     :param n: total number of flavors
#     :return: id1, id2
#     '''
#     combos=list(itertools.combinations(a,2))
#     combos_sum=[cost[0]+cost[1] for cost in combos]
#     cost_pair=combos[combos_sum.index(m)]
#     cost1,cost2=cost_pair[0],cost_pair[1]   # I need to return the id number, I am return the cost number
#     ids=[i for i in range(n) if a[i]==cost1 or a[i]==cost2]
#     ids.sort()
#     return ids[0],ids[1]
#
#
#
# t = int(raw_input().strip())   # num_trips
# for a0 in xrange(t):
#     m = int(raw_input().strip())  # m dollars
#     n = int(raw_input().strip())  # n flavors
#     a = map(int, raw_input().strip().split(' '))  # the cost list of each flavor
#
#     flavor_id1, flavor_id2=get_flavors(m, a,n)
#     print flavor_id1+1, flavor_id2+1



t = int(raw_input().strip())   # num_trips
for a0 in xrange(t):
    m = int(raw_input().strip())  # m dollars
    n = int(raw_input().strip())  # n flavors
    a = map(int, raw_input().strip().split(' '))  # the cost list of each flavor

    cost_map={}  # used to track index
    for i, cost in enumerate(a):
        # 1. use enumerator
        # 2. smaller ID prints first (id is basically index of the list)
        sunny=cost
        jonny=m-cost
        if jonny in cost_map:
            print cost_map[jonny]+1, i+1
        else:
            cost_map[sunny]=i

