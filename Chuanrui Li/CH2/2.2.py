

# Implement an algorithm to find the nth to last element of a singly linked list.

#check forward method, since we cannot use the temporary buffer
class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

def printn(node):
    while(node != None):
        print node.data
        node = node.nextNode

#reverse printing
def printback(node):
    if node == None:
        return
    else:
        printback(node.nextNode)
        print node.data

node = Node("2")
node1 = Node("1")
node2 = Node("2")
node3 = Node("8")
node4 = Node("7")
node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

index = 0
input = 3
while(node != None):
    if(index >= input):
        print node.data
    node = node.nextNode
    index += 1

printn(node)
