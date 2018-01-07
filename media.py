import webbrowser
#imports the webbrowser class from the python standard library
class Movies:
    #init function called when the instance is created for the class Movies and it requires various arguments such as movie_title etc.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    #this function opens the trailer of the movie which user wants to watch.
    def show_trailer(self):
        webbrowser.open(self.trailer)
