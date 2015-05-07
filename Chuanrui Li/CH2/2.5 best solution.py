# Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.

# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

# 1), assume we have two types of runners, first, slow runner(s1) and fast runner (s2). s1 increment by 1 and s2 increment by 2
# 2), s2 starts at kth position, which is bigger than 0, s1 starts at 0 position
# 3), if s1 can catch up s2, then that means the path is circle

# 4), s1 will be set at the starting node, s2 will be set at the previous meeting point


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

def circle(node):
    #init state
    faster = node.nextNode
    slower = node
    
    #iteration
    while faster != slower:
        if faster == None or slower == None:
            print "no circle"
            return
        elif faster.nextNode == None:
            print "no circle"
            return
        faster = faster.nextNode.nextNode
        slower = slower.nextNode
    #     print faster.data, slower.data

    #find the starting position of the cycle
    slower = node
    faster = faster.nextNode
    while faster != slower:
        print "hehe"
        faster = faster.nextNode
        slower = slower.nextNode

    print faster.data



#first linked list
node = Node("0")
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")

node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node1


circle(node)

#cannot handle one circle case

