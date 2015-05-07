#implement a function to check if a linked list is a palidrome

# 1), first, we reverse the linked list, then check each element
# 2), Is it same as the original linked list


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

def palidrome(node):
    curr = node.nextNode
    node.nextNode = None
    while (curr != None):
        pre = curr
        curr = curr.nextNode
        pre.nextNode = node
        node = pre
    return node

def comparison(old, new):
    i = 0
    while(i < len(old)):
        if old[i] != new.data:
            print "no right"
            return
        else:
            i += 1
            new = new.nextNode
    print "yes"
    return


#first linked list
node = Node("0")
node1 = Node("1")
node2 = Node("2")
node3 = Node("1")
node4 = Node("0")


node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4



old = []
start = node
while(start != None):
    old.append(start.data)
    start = start.nextNode
print old
new_node = palidrome(node)
printn(new_node)
comparison(old, new_node)



