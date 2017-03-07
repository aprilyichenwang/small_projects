n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

total_count=0
count=1  #initiate a non-zero number to  start the loop
while count>0:
    count=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            temp=a[i+1]
            a[i+1]=a[i]
            a[i]=temp
            count+=1
    total_count+=count
numSwaps=total_count
firstElement=a[0]
lastElement=a[-1]
print "Array is sorted in %s swaps." %numSwaps
print "First Element:",firstElement
print "Last Element:", lastElement