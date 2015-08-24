#BFS
#This is a directed map 
graph = {'A': ['B', 'C'], 'B':['F'], 'C': ['D'], 'D': ['E'], 'E': ['F'], 'F':['A'] }
visited1 = set()
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
	global graph, visited1
	queue1 = Queue()

	#enqueue the data
	queue1.enqueue(graph.keys()[0])
	visited1.add(graph.keys()[0])

	while queue1.isEmpty() == False:

		items = queue1.dequeue()
		print items 
		for key in graph[items]:
			if key not in visited1 and key in graph:
				#print '---', key
				queue1.enqueue(key)
				visited1.add(key)

bfs()
print visited










