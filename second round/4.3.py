#list of depth


class Node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

#binary tree
t = Node(1, Node(2, Node(4, Node(4), Node(10)), Node(5, Node(4), Node(5))), Node(3, Node(1, Node(4), Node(5)), Node(3, Node(4), Node(5))))
#list of list, will dynamically grow the list in the recursion
mLists = []


def printT(node):
	if node == None:
		return 
	printT(node.left)
	print node.data
	printT(node.right)
	
def printT1(mLists):
	for i in mLists:
		for j in i:
			print j.data,
		print 
	
	
	
#1, pre-order traverse
def list_depth(root, mLists, level):
	#the root is None
	if root == None:
		return

	#the level not exist, master list only reach level-1 sublists
	# len(mLists) <= level: easier to think, need more sublist to cover the level
	if len(mLists) == level:
		mLists.append([root.data])
	else:
		mLists[level].extend([root.data])

	list_depth(root.left, mLists, level+1)
	list_depth(root.right, mLists, level+1)
	
#2, BFS method 
#do have diff, bfs only one queue, this uses multi-level lists
def list_depth1(root, mlists, level):
	#prevent the empty tree
	current = []
	if root != None:
		current.append(root)
	while len(current) != 0:
		#insert into the master lists
		mlists.append(current)
		parents = current
		#new sub-list
		current = []
		for parent in parents:
			if parent.left != None:
				current.extend([parent.left])
			if parent.right != None:
				current.extend([parent.right])
						
			
		
		

list_depth1(t, mLists, 0)
printT1(mLists)









