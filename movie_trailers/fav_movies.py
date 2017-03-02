import movielib
import fresh_tomatoes

gone_with_the_wind = movielib.Movie("Gone with the Wind", "A manipulative Southern belle carries on a turbulent affair with a blockade runner during the American Civil War.", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Poster_-_Gone_With_the_Wind_01.jpg/499px-Poster_-_Gone_With_the_Wind_01.jpg", "https://www.youtube.com/watch?v=0X94oZgJis4")

the_village = movielib.Movie("The Village", "A village is plagued by monsters in the forest, but is faced with a dark secret when a blind girl is forced to leave for medicine in the towns.", "https://upload.wikimedia.org/wikipedia/en/a/a0/The_Village_movie.jpg", "https://www.youtube.com/watch?v=lwq4oTboRi4")

toy_story = movielib.Movie("Toy Story", "Andy's toys come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = movielib.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","http://www.youtube.com/watch?v=-9ceBgWV8io")

batman_begins = movielib.Movie("Batman Begins", "Revenge of a rich boy","https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg", "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

dark_knight = movielib.Movie("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.","https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")

star_wars = movielib.Movie("Star Wars", "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.", "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg", "https://www.youtube.com/watch?v=vP_1T4ilm8M")

alien = movielib.Movie("Alien", "After a space merchant vessel perceives an unknown transmission as distress call, their landing on the source moon finds one of the crew attacked by a mysterious life-form, and soon realize that its life cycle has merely begun.", "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg", "https://www.youtube.com/watch?v=LjLamj-b0I8")

inception = movielib.Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_(2010)_theatrical_poster.jpg", "https://www.youtube.com/watch?v=V3-a58Wt2tk")

movie_list = [gone_with_the_wind, the_village, toy_story, avatar, batman_begins, dark_knight, star_wars, alien, inception]
fresh_tomatoes.open_movies_page(movie_list)