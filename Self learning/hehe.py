max(1, 2, 3)

abs(-23.23)

pow(2, 5) #this is equvalent
2**5 #this is equvalent
2^5

#string
storm_greeting = "you're here"

#string combination
#first way
'hehe' + 'haha' +'!'
first = 'hehe' 
second = 'haha'
third = '!'

#second way
result = first + second + third


#string multiple
('ha'+'xi') * 5
 
#I/O of python
print 'What is the number', 3434

#result: What is the number 3434


#Python 2
raw_input("give me a number")

#Python 3
input("give me a number")

#result: returns a string

print('''HOW
ARE
YOU?
''')

#result: 
#HOW 
#ARE 
#YOU?

print('3\t4\t5')

#result: 3   4    5


#helper function, gives detailed the info
help(abs)


#Not ans
1 == 2 #False
not (1==2) #true

#without (), the order of the operater is
not, and, or


#converting str, int and float
#convert int to string

str(3)
#result: '3'

'3' * 4
#result: '3333'

int('3')
#result: 3

#covert into a float number
fl('456')
#result: 456.0

#cast the input string
int(raw_input("give me a number"))


#comparision operator

"abc" > "abaaa" #because 'a' is smaller than 'c'

'a' > 'A' #True

#substring checking
'abc' in 'abcba'
#result -> True


len('abd')
#result -> 3

len('hehe' + 'jiji' *3)



#substring slice
0     1  2  3  4  5  6  7  8  9 10 
l     e  a  r  n     t  o     g  o
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1	  	

#single index
s = 'learn to go'
s[0] 
#Ans: 'l'
s[-1] = 'o'
#Ans: 'o'
s[-2] = 'g'
#Ans: 'g'

#for the substring slicing the exclude the last digit
s[0:5]
#Ans: 'learn' #exclude the last digit ' '
s[6:7] 
#Ans: 'to'
s[9:len(s)] 
#Ans:'go'
s[:] 
#Ans: 'learn to go'

s[6] = 'd'
#error happens
#string is immutable. They cannot change

#String methods
newString = 'I am late, I am late'

newString.find('late')
#ans 5

newString.find('late', 7)
#starting from pos 7
#ans 14

newString.find('Late', 7)
#if not find
#ans -1

newString.rfind('late')
#starting from pos 7
#ans 14

s = '   I love coding   '
s.lstrip()
#ans: 'I love coding   '

s.rstrip()
#ans: '	  I love coding'

s.strip()
#ans: 'I love coding'





