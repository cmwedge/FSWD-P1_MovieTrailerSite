class Movie:
	"""Encapsulates a movie along with some useful attributes."""
	def __init__(self, movie_title, movie_art_url, movie_trailer_url, us_release_date, rt_meter):
		self.title = movie_title
		self.poster_image_url = movie_art_url
		self.trailer_youtube_url = movie_trailer_url
		self.us_release_date = us_release_date
		self.rt_meter = rt_meter