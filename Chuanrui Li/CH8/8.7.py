# Explain how you would design a chat server. 
# In particular, provide details about the various backend components, classes, and methods. 
# What would be the hardest problems to solve?


class server:
	def __init__(self):
		#private userId matches name of user
		self.__userId = {1: "hehe", 2: "haha"}
		#private groupId matches group name
		self.__groupId = {001: "G1", 002: "G2"}
		#current online user in the chat system
		self.__online_user = ["hehe", "haha"]

	#this is to add a new user
	def add_user(self,username):
		self.__userId[dict.keys()[-1]+1] = username

	def approval_request(self, req):
		return True

	def refuse_request(self, req):
		return False

class user:

	def __init__(self, id, username, email):
		self.id = id
		self.__name = username
		self.__email = email 
		self.group = []
		self.friend = []

	def group_chat(self, group_id):
		self.group.extend([group_id])

	def add_friend_req(self, userId):
		self.friend.append[userId]

	def delete_friend_req(self, userId):
		for i in self.friend:
			if i == userId:
				self.friend.remove(userId)

	def approvel_request(self):
		return Ture


def main():
	pass
   

if __name__ == "__main__":
    main()



  		  