#Write a method to sort an array of strings so that all the anagrams are next to each other.

#hastable, total time cost -> O(nlog(n))
def anagram(list1):
	dic = {}
	for elem in list1:
		key = ''.join(sorted(elem))
		#print key
		if key in dic:
			dic[key] = dic[key] + [elem]
	 	else:
			dic[key] = [elem]
	ans = []
	for elem in dic:
		ans = ans + dic[elem]
	print ans

	
def main():
	list1 = ["hehe", "xixi", "haha", "eheh", "ixix" ]
	print list1
	#anagram
	anagram(list1)


  
  

if __name__ == "__main__":
	main()



