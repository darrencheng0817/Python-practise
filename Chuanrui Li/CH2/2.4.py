

# Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.

# EXAMPLE
# Input: the node ‘c’ from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e

#Input is a node, We delete that node in the linked list


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
def printn(node):
    index = 0
    while(node != None):
        print index, "|", node.data
        node = node.nextNode
        index += 1

#reverse printing 
def printback(node):
    if node == None:
        return
    else:
        printback(node.nextNode)
        print node.data
        
        
def deleteNode(node):
    if node.nextNode == None or node == None:
        print "no way to do it"
        return
    else:
        node.data = node.nextNode.data
        node.nextNode = node.nextNode.nextNode    
        return
        
        
        
        
node = Node("2")
node1 = Node("1")
node2 = Node("2")
node3 = Node("8")
node4 = Node("7")


node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

deleteNode(node3)
printn(node)



#questions: how to deal with multi-deletions