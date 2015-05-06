# Write code to remove duplicates from an unsorted linked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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
node3 = Node("1")
node4 = Node("1")
node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4




node1 = node
while(node1 != None):
    node2 = node1
    while(node2 != None):

        pre = node2
        node2 = node2.nextNode
        if(node2 == None):
            break
        curr = node2
        if(node1.data == node2.data):
            pre.nextNode = curr.nextNode
            node2 = pre
    node1 = node1.nextNode

printn(node)
    
            