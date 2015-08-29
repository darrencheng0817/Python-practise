#write a method to sort an array of string so that all the anagrams are next to each other

#DS: dic <key, list of anagrams>



def anagrams(list1, hashmap):
	for item in list1:
		key = ''.join(sorted(item))
		if key not in hashmap:
			hashmap[key] = [item]
		else:
			hashmap[key].append(item)

	result = []
	for key in hashmap:
		result.extend(hashmap[key])
	print result



def main():
	list1 = ['hehe', 'xixi', 'eheh', 'lala']
	hashmap = {}
	anagrams(list1, hashmap)

if __name__ == "__main__":
	main()



