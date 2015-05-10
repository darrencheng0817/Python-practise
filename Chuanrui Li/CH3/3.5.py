#Implement a MyQueue class which implements a queue using two stacks.

#1), input into the first stack
#2), refresh the second stack by storing the value back to the second stack
#3), second stack is a quene now, it follows the rule: first in first out

stack1 = []
stack2 = []

def push(num):
    global stack1
    global stack2
    stack1.append(num)
    del stack2[:]
    i  = 1
    while i <= len(stack1):
        stack2.append(stack1[len(stack1)-i])
        i += 1
def pop():
    return stack2.pop()
push(1)
push(2)
push(3)
push(11)
push(13)
print pop()
print pop()
print pop()

print stack1, stack2
        
        
    