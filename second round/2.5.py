#6 -> 1 -> 7, 5 -> 9 -> 2
#Output: 2 -> 1 -> 9

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


#The first linked list
node1 = Node(6)
node2 = Node(1)
node3 = Node(7)

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
start1 = node1
start2 = node2


while node1 != None and node2 != None:
    number = node1.data + node2.data
    first_digit = number / 10
    second_digit = number % 10

    new1 = Node(second_digit)
    new1.nextNode = 


    node2 = node2.nextNode
    node1 = node1.nextNode







