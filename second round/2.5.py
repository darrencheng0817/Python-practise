#7-> 1 -> 6, 5 -> 9 
#Output: 2 -> 1 -> 7

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


#The first linked list
node1 = Node(7)
node2 = Node(1)
node3 = Node(6)

node1.nextNode = node2
node2.nextNode = node3

#The second linked list
node4 = Node(5)
node5 = Node(9)
#node6 = Node(2)

node4.nextNode = node5
#node5.nextNode = node6


def printn(node):
    while(node != None):
        print node.data,
        node = node.nextNode


#finding the number
counter = 0
#used for increment by 1
temp = 0

while node1 != None and node4 != None:
    #calculation
    number = node1.data + node4.data
    first_digit = number / 10
    second_digit = number % 10
    #print first_digit, second_digit

    #adding the nodes
    if counter == 0:
        root = Node(second_digit)
        start = root #for testing 
        counter = 1
    else: 
        new1 = Node(second_digit + temp)
        root.nextNode = new1
        root = new1
    temp = first_digit
    #increment
    node1 = node1.nextNode
    node4 = node4.nextNode

#extra checking for the corner cases
if node1 != None:
    new1 = Node(node1.data + temp)
    root.nextNode = new1
    root = new1
elif node4 != None:
    new1 = Node(node4.data + temp)
    root.nextNode = new1
    root = new1


printn(start)





