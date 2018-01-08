import fresh_tomatoes
# import fresh_tomatoes class from python library

import media
# imports the self made class movies

# various constructors or instances are created
sanam_teri_kasam = media.Movies("sanam_teri_kasam",
                                "a true love story of a boy and a girl",
                                "http://media.glamsham.com/download/poster/images/sanam-teri-kasam/02-sanam-teri-kasam.jpg",
                                "https://www.youtube.com/watch?v=1IpBoMWRjm8")

veer_zaara = media.Movies("Veer Zaara",
                          "a love story of two guys from india and pakistan",
                          "https://upload.wikimedia.org/wikipedia/en/c/cb/Veerzaara.jpg",
                          "https://www.youtube.com/watch?v=sd2bOhJTIlY")

victory = media.Movies("Victory", "a story of a cricketer",
                       "https://upload.wikimedia.org/wikipedia/en/1/19/Victory_hindi.jpg",
                       "https://www.youtube.com/watch?v=0Ii0fQ9Vydg")

msd = media.Movies("M.S.Dhoni The Untold Story",
                   "biopic of the most succesful captain of indian cricket team",
                   "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                   "https://www.youtube.com/watch?v=6L6XqWoS8tw")

ashiqui2 = media.Movies("ashiqui2", "a love story",
                        "https://upload.wikimedia.org/wikipedia/en/f/f3/Aashiqui_2_%28Poster%29.jpg",
                        "https://www.youtube.com/watch?v=FyXXgpPqe6w")

half_girlfriend = media.Movies("half girlfriend", "a love story",
                               "https://upload.wikimedia.org/wikipedia/en/6/6e/Half_Girlfriend_Poster.jpg",
                               "https://www.youtube.com/watch?v=KmlBnmyelHI")

movie = [sanam_teri_kasam, ashiqui2, half_girlfriend, veer_zaara, victory, msd]

# this function creates the webpage which contains all the movies.
fresh_tomatoes.open_movies_page(movie)
