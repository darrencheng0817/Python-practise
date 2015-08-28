# Implement a linked list to support the enqueue, dequeueAny, dequeueDog, dequeueCat

#solution:
#1),this question is similar to OS state of process, we can do seperated queue for each kind of animal
#2), I prefer to to use one queue to avoid maintain timestamp
#3), we choose the first to dequeue, since it is the latest one


class Node(object):
    def __init__(self, data, kind):
        self.data = data
        self.kind = kind
        self.nextNode = None
    
def printn(node):
    index = 0
    while(node != None):
        print node.kind, "|", node.data
        node = node.nextNode
        index += 1

#reverse printing 
def printback(node):
    if node == None:
        return
    else:
        printback(node.nextNode)
        print node.data
        

def enqueue(node, number, kind):
    while(node.nextNode != None):
        node = node.nextNode    
    node.nextNode = Node(number, kind)
    
def dequeueAny(node):
    global head
    head = node.nextNode
    
def dequeueDog():
    global head
    start = head
    while(start != None):
        if start.kind == "dog":
            pre.nextNode = start.nextNode
            return
        else:
            pre = start
            start = start.nextNode    
    
    
    
    

    
        
       
   
node = Node("2", "cat")
node1 = Node("1", "cat")
node2 = Node("2", "dog")
node3 = Node("8", "dog")
node4 = Node("7", "cat")


node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4


head = node     
printn(node)
enqueue(node, "11", "dog")
print "------------"
dequeueAny(node)
printn(head)
print "------------"
dequeueDog()
printn(head)




