#Write a program to sort a stack in ascending order. You should not make any assump- tions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

#1), brute force

class Stack:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[len(self.items)-1]

     def size(self):
          return len(self.items)-1
     
     #s1.item > s2.item, then:s1.item -> push, 
     #else: s2.item-> pop and push back into the s1, until find a case one, s1.item ->push
     def sort(self, s2):
	  first = 0
          while self.items != []:
	       flag = 0
	       if first != 0:
		    print self.size(), s2.size()
		    while s2.peek() > self.peek(): 
#			 back = s2.pop()
			 #print back
			 current = self.pop()
			 flag = 1
			 if s2.items == []:
			      break
	       s2.push(self.pop())
	       if flag == 1:
		    self.push(back)
	       first = 1
          
               
                  
s1 = Stack()
s2 = Stack()
s1.push(7)
s1.push(10)
s1.push(5)
s1.push(11)
s1.sort(s2)
print s2.items




