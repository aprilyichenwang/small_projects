"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# head is a node object, that points to the head of a linked list

def has_cycle(head):
    answer=1  # there is a cycle
    curr=head
    i=1
    while i <=100:
        if curr.next == None:
            return 0
        i+=1
    return answer


