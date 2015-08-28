
# Given a directed graph, design an algorithm to find out whether there is a route be- tween two nodes.

#graph = {'A': ['B', 'C'],'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C'] }
graph = {'A': ['B', 'C'], 'D': ['E'], 'E': ['F'] }

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    

def search(begin, end):
    global graph
    q =Queue()
    q.enqueue(begin)
    while(q.isEmpty() == False):
        key = q.dequeue()
        if key not in graph:
            continue
        for j in graph[key]:
            if j == end:
                print "yes"
                return
            else:
                q.enqueue(j)
    print "no"
    return
                
                
            
            

search("A", "D")