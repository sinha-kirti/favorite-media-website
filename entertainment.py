import media
import web_layout
toy_story = media.Movie("Toy Story",
                       "A story of a boy and his toys which come to life",
                       "https://i.ytimg.com/vi/8gL2nKAa9Q8/maxresdefault.jpg",
                       "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

avatar=media.Movie("Avatar",
                   "A marine on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

beauty_and_the_beast_2017=media.Movie("Beauty and The Beast",
                   "An old fairytale",
                   "https://i2.wp.com/teaser-trailer.com/wp-content/uploads/Beauty-and-the-Beast-banner-poster.jpg?ssl=1",
                   "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

#TV Series

sherlock=media.TVSeries("Sherlock",
                   "A detective mastermind who solves mysterious cases with the help of his friend",
                   "https://www.gstatic.com/tv/thumb/tvbanners/13517391/p13517391_b_v8_aa.jpg",
                   "https://www.youtube.com/watch?v=cRdxXhPV9GNQ")
movies = [toy_story,avatar, beauty_and_the_beast_2017]
tvseries = [sherlock];
#above line creates a list of movies to provide as argument to
#below function

web_layout.open_movies_page(movies,tvseries)
# Creates a webpage have our favourite movies and tvseries
