# s = int(raw_input().strip())
# for a0 in xrange(s):
#     n = int(raw_input().strip())

# 1 - 1
# 2 - (1, 1) , (2)
# 3 - (1, 1, 1) (1, 2) (2, 1) (3, 0)
# 4 = num_ways(3)+num_ways(2)+num_ways(1)


memory = {1:1, 2:2, 3:4}
def num_ways(n):
    if not n in memory.keys():
        memory[n] = num_ways(n-1) + num_ways(n-2) + num_ways(n-3)
    return memory[n]


print num_ways(1)
print num_ways(3)
print num_ways(7)





