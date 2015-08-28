# You have two numbers represented by a linked list, where each node contains a sin- gle digit. The digits are stored in reverse order, such that the 1’s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

# EXAMPLE
# Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
# Output: 8 -> 0 -> 8

# 1), read two link list and store in two seperated list
# 2), output the number and do the plus operation
# 3), store it back to the linked list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

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
node = Node("1")
node1 = Node("1")
node2 = Node("2")

node.nextNode = node1
node1.nextNode = node2


#second linked list
node5 = Node("5")
node6 = Node("6")
node7 = Node("7")
node8 = Node("7")

node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8
a = []
b = []

get_number(node, a)
get_number(node5, b)
print a, b
result = get_add(a, b)
print result
