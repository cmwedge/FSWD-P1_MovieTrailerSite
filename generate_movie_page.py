from movie import Movie
import csv
import fresh_tomatoes

MOVIE_FILE = 'my_movies.csv'

def load_movies(movie_csv):
	"""creates and returns a list of movies pulled from the provided csv file"""
	movies = []
	try:
		with open(movie_csv, 'r') as f:
			rdr = csv.reader(f, delimiter=',', quotechar=r'"')
			movies = [Movie(*row) for row in rdr]
	except:
		print("A problem occurred reading movies from movie file.")

	return movies

def generate_webpage(movies):
	"""generates the webpage by utilizing fresh_tomatoes method"""
	fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
	movies = load_movies(MOVIE_FILE)
	generate_webpage(movies)