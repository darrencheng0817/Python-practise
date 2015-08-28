# Given a circular linked list, implement an algorithm which returns node at the begin- ning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.traveled = 0

def printn(node):
    index = 0
    while(node != None):
        print node.data
        node = node.nextNode
        index += 1

#reverse printing
def printback(node):
    if node == None:
        return
    else:
        printback(node.nextNode)
        print node.data

def get_number(node, a):
    index = 0
    while(node != None):
        a.append(node.data)
        node = node.nextNode
        index += 1


def get_add(a, b):
    sum1 = 0
    index1 = 0
    sum2 = 0
    index2 = 0
    for i in a:
        sum1 += int(i) * pow(10, index1)
        index1 += 1
    print sum1
    for j in b:
        sum2 += int(j) * pow(10, index2)
        index2 += 1
    return sum1 + sum2


def deleteNode(node):
    if node.nextNode == None or node == None:
        print "no way to do it"
        return
    else:
        node.data = node.nextNode.data
        node.nextNode = node.nextNode.nextNode
        return



#first linked list
node = Node("0", )
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("1")

node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node2

def circle(node):
    while(node != None):
        if(node.traveled == 0):
            node.traveled = 1
        else:
            print "circle detect: " + pre
            break
        pre = node.data
        node = node.nextNode


circle(node)






