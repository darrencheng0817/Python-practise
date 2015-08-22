
#loop detect, 
#easy approach, setting tags
#hard approach, slower chase faster runner

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
 def circle(node):
    #init state
    faster = node.nextNode
    slower = node
    
    #iteration
    #finding inside loop position for faster runner 
    #-> LOOP_SIZE - K
    while faster != slower:
        if faster == None or slower == None:
            print "no circle"
            return
        elif faster.nextNode == None:
            print "no circle"
            return
        faster = faster.nextNode.nextNode
        slower = slower.nextNode
    #print faster.data, slower.data

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
