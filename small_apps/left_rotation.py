


def track_index(n, k):
    # given the length of the array,
    # return the next index

    # original list index = 0 1 2 3 4
    # now, 1 2 3 4 0
    # now 2 3 4 0 1
    # now 3 4 0 1 2

    l = range(n)
    for i in range(k):
        l.append(l[0])
        l=l[1:]
    return l


def track_index(n, k):
    l=range(n)
    return [l[(i + k) % n] for i in range(n)]



def array_left_rotation(a, n, k):
    l=track_index(n, k)
    b=[a[i]for i in l]
    return b


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str, answer))