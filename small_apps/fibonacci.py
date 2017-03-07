def fibonacci(n):
    # Write your code here.
    ls=[0,1]
    i=2
    while i<=n:
        ls.append(ls[-1]+ls[-2])
        i+=1
    return ls[-1]

n = int(raw_input())
print(fibonacci(n))