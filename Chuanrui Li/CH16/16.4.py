#Given a dictionary of millions of words, 
#give an algorithm to find the largest possible rectangle of letters such that every row forms a word (reading left to right) and every column forms a word (reading top to bottom).


Step 1, Preprocess the dictionary into hashmap <length of words, [word1, word2,....]> 
Step 2, Approximately starts from 25 and search for the key.
Step 3, If the key exsit, iterate the list(brute force)
	---> ex: dog
			 who
			 two

			 dwt does not exsit, skip dog, starts at who again
Step 4, store the dimension M*N as Max