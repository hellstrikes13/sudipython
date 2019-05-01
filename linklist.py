class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
n = Node('blahnode')
n1 = Node('blahnode1')
n2 = Node('blahnode2')
n3 = Node('blahnode3')
n.next = n2
n2.next = n3
print n,n1,n2,n3

