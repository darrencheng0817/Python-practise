#BFS
#This is a directed map
graph = {'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['E', 'C'], 'E': ['A', 'D']}
visited1 = set()
visited2 = set()

class Queue:
    def __init__(self):
        self.item = []
    def enqueue(self, item):
        self.item.extend(item)
    def dequeue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return len(self.item) == 0



#two bfs starts from the two nodes
def bfs():
    global graph, visited1, visited2
    queue1 = Queue()
    queue2 = Queue()
    
    #enqueue the data
    queue1.enqueue(graph.keys()[0])
    visited1.add(graph.keys()[0])
    
    queue2.enqueue('D')
    visited2.add('D')

    while queue1.isEmpty() == False:
        items = queue1.dequeue()
        items = queue2.dequeue()
        print items
        for key in graph[items]:
            if key not in visited1 and key in graph:
                queue1.enqueue(key)
                visited1.add(key)

        for key in graph[items]:
            if key not in visited2 and key in graph:
                queue2.enqueue(key)
                visited2.add(key)

        if visited1&visited2 != set([]):
            print 'Yes', visited1&visited2 
            return
    print "No"
    return

bfs()







