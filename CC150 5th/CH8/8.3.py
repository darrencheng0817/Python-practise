#Design a musical juke box using object oriented principles.

playlist = []
counter = 0
class CDplayer:
	def __init__(self, CD_name):
		self.CD_name = CD_name
	def playlist_creation(self):
		global playlist
		playlist = [1, 2, 3]
	def display(self):
		global playlist
		global counter
		print "playing the song: " + str(playlist[counter]) 
	def next_song(self):
		global playlist
		global counter
		if counter < len(playlist)-1:
			counter += 1
			print "playing next song: " + str(playlist[counter])
		else:
			counter = 0
			print "playing next song: " + str(playlist[counter])
	def pre_song(self):
		global playlist
		global counter
		if counter > 0:
			counter -= 1
			print "playing pre song: " + str(playlist[counter])	
		else:
			counter = len(playlist)-1
			print "playing pre song: " + str(playlist[counter])
class user:
	def __init__(self, name):
		self.name = name

	def add_song(self, song):
		global playlist
		playlist.extend([song])


	def delete_song(self, song):
		global playlist
		for i in playlist:
			if song == i:
				playlist.remove(i)



CDplayer1 = CDplayer("testingCD")
CDplayer1.playlist_creation()
CDplayer1.display()


user1 = user("ric")
user1.add_song(4)
CDplayer1.pre_song()




  		  