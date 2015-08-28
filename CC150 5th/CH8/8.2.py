# Imagine you have a call center with three levels of employees: 
# fresher, technical lead (TL), product manager (PM). 
# There can be multiple employees, but only one TL or PM. 
# An incoming telephone call must be allocated to a fresher who is free. 
# If a fresher can’t handle the call, he or she must escalate the call to technical lead. 
# If the TL is not free or not able to handle it, then the call should be escalated to PM. 
# Design the classes and data structures for this problem. 
# Implement a method getCallHandler().

#three level, In my code assumption, there are more than 1 technical lead (TL) and product manager (PM).
#First level, phone call only being passed to the second level, when the fresher cannot handler the call
#Otherwise it will be pass to the TL or PM
#there is two waiting queue, one for fresher and one for clients

#second and third level, if there are nobody is here, client waiting
#there is two waiting queue, one for fresher and one for clients


#two waiting queues for level one 
list_1 = [] #---> avaliable fresher queue
list_1_w = [] # --> working fresher queue
list_1_c = [] #---> waiting client queue

#two waiting queues for level two and level three
list_2 = []
list_2_w = []
list_2_c = []

#define the employees
class client:
	def __init__(self, ID, level):
		self.ID = ID
		self.level = level 
	#get a phone call
	def getCallHandler(self):
		#level_1 
		global list_1 #---> avaliable fresher queue
		global list_1_w  # --> working fresher queue
		global list_1_c #---> waiting client queue
		
		#level_2
		global list_2 #---> avaliable fresher queue
		global list_2_w  # --> working fresher queue
		global list_2_c #---> waiting client queue		
		
		#no body is avaliable, client waits -- level 1
		if len(list_1) == 0 and self.level == 0:
			list_1_c = [self.ID] + list_1_c
		#somebody is avaliable, client get call -- level 1
		elif len(list_1) != 0 and self.level == 0:
			working = list_1.pop()
			list_1_w += [(self.ID, working)]
		#somebody is avaliable, client waits-- level 1
		elif len(list_2) == 0 and self.level == 1:
			list_2_c = [self.ID] + list_2_c
		#somebody is avaliable, client get call -- level 1
		elif len(list_2) != 0 and self.level == 1:
			working = list_2.pop()
			list_2_w += [(self.ID, working)]

	#finish the call from one client
	def finishcallHandler(self):
		#Leaving the list first
		#level1
		global list_1 #---> avaliable fresher queue
		global list_1_w  # --> working fresher queue
		global list_1_c #---> waiting client queue
				
		#level_2
		global list_2 #---> avaliable fresher queue
		global list_2_w  # --> working fresher queue
		global list_2_c #---> waiting client queue		
		if self.level == 0:
			for i in list_1_w:
				#remove the item
				if self.ID == i[0]:
					free = i[1]				
					list_1_w.remove(i)
			
			if len(list_1_c) != 0:
				client = list_1_c.pop()
				list_1_w += [(client, free)]
			else:
				list_1 = [free] + list_1
				
				
		#level2
		elif self.level == 1:
			for i in list_2_w:
				#remove the item
				if self.ID == i[0]:
					free = i[1]
					list_2_w.remove(i)			
			if len(list_2_c) != 0:
				client = list_2_c.pop()
				list_2_w += [(client, free)]
			else:
				list_2 = [free] + list_2
			
		#pick up one client from the waiting queue
		
	
class fresher:
	def __init__(self, ID):
		global list_1 
		self.ID = ID
		list_1 = [self.ID] + list_1


class TL_and_PM:
	def __init__(self, ID):
		global list_2
		self.ID = ID
		list_2 = [ID] + list_2

#a list of client coming in
c1 = client("c1", 1)
c2 = client("c2", 1)
c3 = client("c3", 1)
c4 = client("c4", 1)
c5 = client("c5", 1)
c6 = client("c6", 1)


#fresher list
f1 = fresher("f1")


#senior list
s1 = TL_and_PM("s1")


#calling now
c1.getCallHandler()
c2.getCallHandler()
c3.getCallHandler()
c4.getCallHandler()
c5.getCallHandler()
c1.finishcallHandler()
c2.finishcallHandler()
#error checking
print list_1 #---> avaliable fresher queue
print list_1_w # --> working fresher queue
print list_1_c #---> waiting client queue

print list_2
print list_2_w
print list_2_c




