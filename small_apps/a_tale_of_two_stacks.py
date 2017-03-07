class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):  # print the element at the front of the queue
        return str(self.first)

    def pop(self):  # 2 dequeue the value at the head of the queue
        if len(self.second)>0:
            self.first=self.second[0]
            self.second=self.second[1:]
        else:
            self.first=[]

    def put(self, value):  # 1, enqueue element to the end of the queue
        # define a put function
        if self.first==[]:
            self.first.append(value)
        else:
            self.second.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()




