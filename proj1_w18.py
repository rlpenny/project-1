import requests
import json

json_file = open('sample_json.json', 'r')
data = json_file.read()
json_dict = json.loads(data)


class Media:
	def __init__(self, title="No Title", author="No Author", release_year = "N/A", json = None):
		if json is None:
			self.title = title
			self.author = author
			self.year = release_year
			self.json = json
		else:
			self.process_json_dict(json_dict)

	def process_json_dict(self, json_dict):
		self.title = json_dict['trackName']
		self.author = json_dict['artistName']
		self.year = json_dict['releaseDate'][:4]

	def __str__(self):
		return(self.title + " by " + self.author + " (" + (self.year) + ")")


	def __len__(self):
		return(0)


class Song(Media):
	def __init__(self, title= "No Title", author = "No Author", release_year ="N/A", album = "No Album", genre = "Unknown", track_length= "N/A", json = None):
		if json is None:
			super().__init__(title, author, release_year)
			self.album = album
			self.genre = genre
			self.length = track_length
			self.json = json
		else:
			super().process_json_dict()
			self.year = json_dict["releaseDate"][:4]
			self.album = json_dict["collectionName"]
			self.genre = json_dict["primaryGenreName"]
			self.length = json_dict["trackTimeMillis"]


	def __str__(self):
		return(super().__str__() + "[" + self.genre + "]")

	def __len__(self):
		return(self.length)
		# need to convert


class Movies(Media):
	def __init__(self, title= "No Title", author = "No Author", release_year = "N/A", rating = "N/A", movie_length = "N/A", json = None):
		if json is None:
			super().__init__(title, author, release_year)
			self.rating = rating
			self.movie_length = movie_length
			self.json = json
		else:
			super().process_json_dict()
			self.rating = json_dict["contentAdvisoryRating"]
			self.movie_length= json_dict["trackTimeMillis"]

	def __str__(self):
		return(super().__str__() + "[" + self.rating + "]")

	def __len__(self):
		return((int(self.movie_length) / 1000) / 60)
	#might be wrong



a = Movies(json_dict)
print(a.title)
b = Song(json_dict)
print(b.title)




if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
#^^this file will sometimes be called as a module
