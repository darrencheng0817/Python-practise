
#"thit"
#general idea check the all the combinations for the string and find the least invaild ans

sentence = "Iamadog"
def parser(start, end):
	global sentence
	if end > len(sentence):
		return end - start
	word = sentence[start: end]
	if dictionary_contain(word) == False:
		bestlen += len(word)
	
	#checkout the next combination
	#first check => t, hit
	#second check => th, it
	bestextend = parser(start, end+1)
	
	#return the least vaild combination for the result
	return min(bestlen, bestextend)

def main(): 
	parser(0, 0)
	
	
if __name__ == "__main__":
	main()

