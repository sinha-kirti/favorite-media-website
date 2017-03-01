import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                       "A story of a boy and his toys which come to life",
                       "https://i.ytimg.com/vi/8gL2nKAa9Q8/maxresdefault.jpg",
                       "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A marine on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#avatar.show_trailer()
movies = [toy_story,avatar]
#above line creates a list of movies to provide as argument to below line of code

fresh_tomatoes.open_movies_page(movies)

# Above commented out line of code creates a webpage have our favourite movies

#print(media.Movie.__name__)
#print(media.Movie.__module__)
#print(media.Movie.__doc__)      
# Above 3 lines are example of predefined class variables of python
