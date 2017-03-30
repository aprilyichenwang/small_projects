# discuss when n=1, 2, n>2

def evaluate_prime(n):
    if n>2:
        for i in range(2, n, 1):
            if n%i==0:
                return False
        return True
    elif n==2:
        return True
    else:
        return False




p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    if evaluate_prime(n):
        print "Prime"
    else:
        print "Not prime"








