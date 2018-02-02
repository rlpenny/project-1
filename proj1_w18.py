import requests
import json

json_file = open('sample_json.json', 'r')
data = json_file.read()
json_list = json.loads(data)


class Media:
	def __init__(self, title="No Title", author="No Author", release_year = "N/A", json = None):
		self.title = title
		self.author = author
		self.year = release_year
		self.json = json

	def __str__(self):
		#return(self.title + " by " + self.author + " (" + str(self.year) + ")")
		return(self.title + " by " + self.author + " (" + str(self.year) + ")")


	def __len__(self):
		return(0)

class Song(Media):
	def __init__(self, title= "No Title", author = "No Author", release_year ="N/A", album = "No Album", genre = "Unknown", track_length= "N/A", json = None):
		super().__init__(title, author, release_year)
		self.album = album
		self.genre = genre
		self.length = track_length
		self.json = json

	def __str__(self):
		return(super().__str__() + "[" + self.genre + "]")
		#return(self.title + " by " + self.author + "(" + self.year + ")" + " [" + self.genre + "]")

	def __len__(self):
		return(self.length)

class Movies(Media):
	def __init__(self, title= "No Title", author = "No Author", release_year = "N/A", rating = "N/A", movie_length = "N/A", json = None):
		super().__init__(title, author, release_year)
		self.rating = rating
		self.movie_length = movie_length
		self.json = json

	def __str__(self):
		return(super().__str__() + "[" + self.rating + "]")
		#return(self.title + " by " + self.author + " (" + self.year + ")" + "[" + self.rating + "]")

	def __len__(self):
		return((int(self.movie_length) / 1000) / 60)


print(json_list)




if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
#^^this file will sometimes be called as a module
