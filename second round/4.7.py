#Topological sort

graph = {'A': ['E'], 'B': ['A', 'E'], 'C': ['A'], 'F': ['A', 'B', 'C'], 'D':['G']}
visited = set()

list1 = []

def dfs(item):
	global list1
	visited.add(item)

	#no key in the dic
	if item not in graph:
		list1.insert(0, [item])
		return 
	#go to the next level
	for adjacent in graph[item]:
		#have not check yet
		if adjacent not in visited:
			dfs(adjacent)
	list1.insert(0, [item])



def sort(graph):
	for i in graph:
		if i not in visited:
			dfs(i)


sort(graph)
print list1