
def is_matched(expression):
    dic = {'{': '}', '(': ')', '[': ']'}
    lst=[]
    for i in expression:  # no need to convert to a list
        if i in dic:  # if in left brackets
            lst.append(dic[i])  # append the paired one
        elif len(lst) > 0 and i == lst[-1]:
            # has some left pairs & right shows up, compare on the spot
            lst.pop()
            # if the right element in a list matches the last left,
            # matching, and remove the corresponding element in that left list
        else:
            return False
    return len(lst) == 0  # if all ls get matched up, than balanced, return 0, else return 1




t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"


