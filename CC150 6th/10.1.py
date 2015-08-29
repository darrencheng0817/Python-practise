#Write a method to merge B into A in sorted order.
        
A = [1, 2, 3, 5, 6]
B = [0, 1, 2, 3, 4]

#1, two pointers for list A and B, compare and pop the smaller one
#2, pop rest of non empty list 

list1 = []
def merge(a, b):
	global list1
	i, j = 0, 0
	lena, lenb= len(a), len(b) 
	while i < lena and j < lenb:
		print i, len(a), j, len(b)
		if a[i] >= b[j]:
			list1.append(b[j])
			j += 1 
		elif a[i] < b[j]:
			list1.append(a[i])
			i += 1
	#rest of the list
	if j < lenb:
		while j < len(b):
			list1.append(b[j])
			j += 1 

	elif i < lena:
		while i < len(a):
			list1.append(a[i])
			i += 1
merge(A, B)
print list1, A, B
			



